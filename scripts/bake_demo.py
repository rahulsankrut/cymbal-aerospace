#!/usr/bin/env python3
"""Pre-Demo Baker & M365 Outlook Mail/Calendar Seeder for Cymbal Aerospace CLM Demo ("Bake CLM demo").

What this script does before a live Cymbal Aerospace CLM customer demo:
  1. Resets Deal `BA-2026-AV-8921` in BigQuery (`vertex-ai-demos-468803.boeing_clm`), Cloud Run
     (`https://boeing-clm-engine-5udif2v3cq-uc.a.run.app`), and local Spark state
     (`~/ge_spark_workspace/skills/cymbal_clm_state.json`) back to pristine intake state.
  2. Syncs all 5 Cymbal Aerospace CLM skills (`clm-contract-intake`, `clm-eng-faa-review`,
     `clm-legal-ip-review`, `clm-tax-tariff-review`, `clm-contract-consolidation`) + `clm_cli.py`
     and `cymbal_clm_seed.json` to `~/ge_spark_workspace/skills/`.
  3. Cleans up ONLY Microsoft Outlook Mail (`Inbox` and `Drafts` folders) and Outlook Calendar (`events`)
     across the M365 demo tenant (`m365-admin@rahulsankrut.demo.altostrat.com` and SME roster accounts).
     Leaves SharePoint (`CymbalAerospace` and `CybmalFinance`), OneDrive, Jira, and Confluence untouched.
  4. Seeds 5 fresh Cymbal Aerospace CLM emails (rolled to TODAY's date) into Outlook `Inbox`, including
     Adele Vance's urgent vendor redline email with `Vendor_Redlined_GP1.docx` and
     `Apex_AeroSystems_Redline_Transmittal_Memo.docx` attached.
  5. Seeds 6 fresh Cymbal Aerospace CLM meetings (rolled to TODAY and CURRENT WEEK) onto the Outlook
     Calendar so the generic `chief-of-staff` skill ("What are my top priorities today?") naturally
     synthesizes the BA-2026-AV-8921 contract redline crisis and today's 1:30 PM & 4:00 PM decision gates.
  6. Prints a live verification summary of Outlook Inbox, Outlook Drafts, Outlook Calendar, SharePoint,
     and BigQuery.

Usage:
  "/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.venv/bin/python" "/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/scripts/bake_demo.py" [--quick | --full]
"""

from __future__ import annotations

import argparse
import base64
from datetime import date, datetime, timedelta, timezone
import json
import os
import pathlib
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
SPARK_WORKSPACE = pathlib.Path.home() / "ge_spark_workspace"
ENV_PATH = pathlib.Path("/Users/rahulsankrut/Desktop/code/Cymbal/spark-demo/.env")

ADMIN_UPN = "m365-admin@rahulsankrut.demo.altostrat.com"
ROSTER_UPNS = [
    ADMIN_UPN,
    "AdeleV@36zrbd.onmicrosoft.com",
    "MeganB@36zrbd.onmicrosoft.com",
    "LeeG@36zrbd.onmicrosoft.com",
    "PradeepG@36zrbd.onmicrosoft.com",
    "AlexW@36zrbd.onmicrosoft.com",
    "PattiF@36zrbd.onmicrosoft.com",
    "MiriamG@36zrbd.onmicrosoft.com",
    "JohannaL@36zrbd.onmicrosoft.com",
    "LidiaH@36zrbd.onmicrosoft.com",
    "JoniS@36zrbd.onmicrosoft.com",
    "NestorW@36zrbd.onmicrosoft.com",
]

CLM_SKILLS = [
    "clm-contract-intake",
    "clm-comms",
    "clm-tax-tariff-review",
    "clm-contract-consolidation",
]

REDUNDANT_SKILLS_TO_REMOVE = [
    "clm-eng-faa-review",
    "clm-legal-ip-review",
    "cymbal-capital-allocation",
    "cymbal-capital-execution",
    "cymbal-capital-intake",
    "cymbal-capital-stress-test",
    "financial-model-audit",
    "portfolio-optimization",
    "task-execution-Monitor",
]


def ensure_host_loopback_bridge() -> None:
    """
    Ensures the lightweight CLM Host Loopback Bridge is listening on http://127.0.0.1:58921
    running the latest `clm_cli.py` (which serves `/run` and `/api/review`).
    """
    subprocess.run(["pkill", "-f", "clm_cli.py --serve-bridge"], check=False)
    time.sleep(0.3)

    health_url = "http://127.0.0.1:58921/health"
    cli_src = ROOT / "skills" / "clm_cli.py"
    log_path = pathlib.Path("/tmp/cymbal_clm_bridge.log")
    with log_path.open("a", encoding="utf-8") as log_file:
        subprocess.Popen(
            [sys.executable, str(cli_src), "--serve-bridge"],
            cwd=str(ROOT),
            stdout=log_file,
            stderr=log_file,
            start_new_session=True,
        )
    time.sleep(0.8)
    try:
        with urllib.request.urlopen(health_url, timeout=2.0) as r:
            if r.status == 200:
                print("  ✓ Started CLM Host Loopback Bridge on http://127.0.0.1:58921 (serves /run & /api/review)")
    except Exception as exc:
        print(f"  ! Warning starting Loopback Bridge: {exc}")


def _banner(step: int, title: str) -> None:
    print(f"\n{'=' * 78}")
    print(f"  STAGE {step}: {title}")
    print(f"{'=' * 78}")


def _load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    for candidate in [ROOT / ".env", ENV_PATH]:
        if candidate.exists():
            for line in candidate.read_text(encoding="utf-8").splitlines():
                s = line.strip()
                if s and not s.startswith("#") and "=" in s:
                    k, v = s.split("=", 1)
                    env.setdefault(k.strip(), v.strip().strip('"').strip("'"))
    return env


def _get_graph_token() -> str:
    env = _load_env()
    tenant_id = (
        os.environ.get("AZURE_TENANT_ID")
        or env.get("AZURE_TENANT_ID")
        or env.get("GRAPH_TENANT_ID")
        or "bb18058e-2958-4250-8593-c746406ac1c1"
    )
    client_id = (
        os.environ.get("AZURE_CLIENT_ID")
        or env.get("AZURE_CLIENT_ID")
        or env.get("GRAPH_CLIENT_ID")
        or "d32dbab7-b9f8-48c5-95d7-53b50fdda2e9"
    )
    client_secret = (
        os.environ.get("AZURE_CLIENT_SECRET")
        or env.get("AZURE_CLIENT_SECRET")
        or env.get("GRAPH_CLIENT_SECRET")
        or ""
    )

    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    data = urllib.parse.urlencode(
        {
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": "https://graph.microsoft.com/.default",
            "grant_type": "client_credentials",
        }
    ).encode("utf-8")
    req = urllib.request.Request(token_url, data=data, method="POST")
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))["access_token"]


def _graph_req(
    token: str,
    method: str,
    path: str,
    payload: dict | None = None,
) -> dict:
    url = path if path.startswith("https://") else f"https://graph.microsoft.com/v1.0{path}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers = {"Authorization": f"Bearer {token}"}
    if payload is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()
        return json.loads(raw.decode("utf-8")) if raw else {}


def stage_1_reset_deal_and_sync_skills() -> None:
    _banner(1, "Reset Deal BA-2026-AV-8921 State, Start Loopback Bridge & Sync 4 Focused CLM Skills")
    cli_src = ROOT / "skills" / "clm_cli.py"
    seed_src = ROOT / "skills" / "cymbal_clm_seed.json"

    if SPARK_WORKSPACE.exists():
        skills_dst = SPARK_WORKSPACE / "skills"
        skills_dst.mkdir(parents=True, exist_ok=True)
        shutil.copy2(cli_src, skills_dst / "clm_cli.py")
        shutil.copy2(seed_src, skills_dst / "cymbal_clm_seed.json")

        for rem in REDUNDANT_SKILLS_TO_REMOVE:
            for base_dir in (skills_dst / rem, ROOT / ".agents" / "skills" / rem):
                if base_dir.exists():
                    shutil.rmtree(base_dir, ignore_errors=True)

        for s in CLM_SKILLS:
            skill_md_src = ROOT / "skills" / s / "SKILL.md"
            for base_dir in (ROOT / "skills" / s, ROOT / ".agents" / "skills" / s, skills_dst / s):
                scripts_dir = base_dir / "scripts"
                scripts_dir.mkdir(parents=True, exist_ok=True)
                if skill_md_src.exists() and (base_dir / "SKILL.md") != skill_md_src:
                    shutil.copy2(skill_md_src, base_dir / "SKILL.md")
                shutil.copy2(cli_src, scripts_dir / "clm_cli.py")
                shutil.copy2(seed_src, scripts_dir / "cymbal_clm_seed.json")
        print(f"  ✓ Synced {len(CLM_SKILLS)} focused CLM skills ({', '.join(CLM_SKILLS)}) to {skills_dst}")

    ensure_host_loopback_bridge()

    res = subprocess.run(
        [sys.executable, str(cli_src), "reset", "--deal-id", "BA-2026-AV-8921"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    if res.returncode == 0:
        print("  ✓ Reset Deal BA-2026-AV-8921 in Cloud Run / BigQuery and local Spark state (`status = INGESTED`)")
    else:
        print(f"  ! Deal reset warning: {res.stderr or res.stdout}")


def stage_2_purge_outlook_mail_and_calendar(token: str) -> None:
    _banner(2, "Clean Up ONLY Microsoft Outlook Mail (Inbox & Drafts) and Calendar Events")
    print("  • Note: Leaving SharePoint (`CymbalAerospace` & `CybmalFinance`), OneDrive, Jira, and Confluence untouched.")

    for folder in ("Inbox", "Drafts"):
        try:
            resp = _graph_req(
                token,
                "GET",
                f"/users/{ADMIN_UPN}/mailFolders/{folder}/messages?$top=100&$select=id,subject",
            )
            msgs = resp.get("value", [])
            print(f"  • Purging {len(msgs)} existing messages from {ADMIN_UPN} `{folder}`...")
            for m in msgs:
                try:
                    _graph_req(token, "DELETE", f"/users/{ADMIN_UPN}/messages/{m['id']}")
                except Exception:
                    pass
        except Exception as exc:
            print(f"  ! Warning cleaning {folder}: {exc}")

    total_events_deleted = 0
    for upn in ROSTER_UPNS:
        try:
            resp = _graph_req(token, "GET", f"/users/{upn}/events?$top=100&$select=id,subject")
            evts = resp.get("value", [])
            if evts:
                for e in evts:
                    try:
                        _graph_req(token, "DELETE", f"/users/{upn}/events/{e['id']}")
                        total_events_deleted += 1
                    except Exception:
                        pass
        except Exception:
            pass
    print(f"  ✓ Purged {total_events_deleted} calendar events across {len(ROSTER_UPNS)} tenant mailboxes")


def stage_3_seed_clm_outlook_inbox(token: str) -> None:
    _banner(3, "Seed Fresh Cymbal Aerospace CLM Emails (with Today's Dates & Attachments) into Outlook Inbox")
    today = date.today()
    yesterday = today - timedelta(days=1)

    vendor_docx = ROOT / "specs" / "04_golden_fixtures" / "Vendor_Redlined_GP1.docx"
    memo_docx = ROOT / "specs" / "04_golden_fixtures" / "Apex_AeroSystems_Redline_Transmittal_Memo.docx"

    attachments = []
    for path in (vendor_docx, memo_docx):
        if path.exists():
            attachments.append(
                {
                    "@odata.type": "#microsoft.graph.fileAttachment",
                    "name": path.name,
                    "contentType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    "contentBytes": base64.b64encode(path.read_bytes()).decode("ascii"),
                }
            )

    emails = [
        {
            "key": "clm-001-apex-redline-submission",
            "subject": "[URGENT REDLINE] Deal BA-2026-AV-8921 — Apex AeroSystems Markup of Cymbal GP1 / SP3 / SP5 ($45,000,000 FCC-900 Flight Control Subsystem)",
            "importance": "high",
            "is_read": False,
            "from_name": "Adele Vance (Apex AeroSystems)",
            "from_addr": "AdeleV@36zrbd.onmicrosoft.com",
            "to": [{"name": "Rahul Kasanagottu", "address": ADMIN_UPN}],
            "cc": [
                {"name": "Megan Bowen", "address": "MeganB@36zrbd.onmicrosoft.com"},
                {"name": "Lee Gu", "address": "LeeG@36zrbd.onmicrosoft.com"},
                {"name": "Pradeep Gupta", "address": "PradeepG@36zrbd.onmicrosoft.com"},
                {"name": "Alex Wilber", "address": "AlexW@36zrbd.onmicrosoft.com"},
            ],
            "sent_at": f"{today.isoformat()}T12:42:00Z",
            "received_at": f"{today.isoformat()}T12:42:10Z",
            "attachments": attachments,
            "body_html": f"""
<div style="font-family: Calibri, Arial, sans-serif; font-size: 11pt; color: #1e293b; line-height: 1.55;">
  <p>Rahul,</p>
  <p>Please find attached <strong>Apex AeroSystems Inc.'s formal Track-Changes markup (<code>Vendor_Redlined_GP1.docx</code>)</strong> and our accompanying <strong>Redline Transmittal Memo (<code>Apex_AeroSystems_Redline_Transmittal_Memo.docx</code>)</strong> for <strong>Deal BA-2026-AV-8921</strong> covering the <strong>$45,000,000 Firm-Fixed-Price procurement of the FCC-900 Triple-Redundant Fly-By-Wire Flight Control Computer Subsystem</strong>.</p>
  <p style="background:#fef2f2;border-left:4px solid #dc2626;padding:10px 14px;color:#991b1b;">
    <strong>⏰ 48-Hour Pricing &amp; Lead-Time Validity Notice:</strong> To lock in our titanium forging and radiation-hardened wafer allocation for Cymbal Aerospace's Q3 Everett Final Assembly Line schedule, we require Cymbal's consolidated counter-proposal or execution sign-off prior to your <strong>4:00 PM PT Executive Sign-Off Gate today ({today.isoformat()})</strong>.
  </p>
  <p>Out of the 12 clauses in Cymbal's Master Terms &amp; Conditions package (<code>Cymbal_GP1_Standard.docx</code>), <strong>we have accepted 8 clauses untouched</strong> and proposed targeted commercial and operational redlines on <strong>4 clauses</strong>:</p>
  <ol>
    <li><strong><code>GP1 §12.2</code> (Warranty &amp; FAA Source Inspection):</strong> Adjusted warranty to our standard commercial <strong>12 months from ex-works factory shipment</strong> (from 36 months post-aircraft delivery) and requested <strong>30 days' prior written notice</strong> for source inspections to prevent cleanroom shift disruptions.</li>
    <li><strong><code>GP1 §19.1 &amp; §24.1</code> (Limitation of Liability &amp; IP Indemnity):</strong> Capped direct contractual liability at <strong>100% (1.0x) of the Purchase Order value ($45,000,000)</strong> and carved out IP infringement claims arising from combination or integration of the FCC-900 with Cymbal's system-level avionics bus.</li>
    <li><strong><code>SP3 §4.1</code> (Customs, Duties &amp; Section 232/301 Tariffs):</strong> Added a <strong>100% pass-through to Buyer</strong> for any new or increased Section 232 or Section 301 tariffs exceeding <strong>5.0%</strong> on specialty titanium forgings or radiation-hardened semiconductor wafers.</li>
    <li><strong><code>SP5 §3.2</code> (Cybersecurity Incident Reporting):</strong> Adjusted cyber incident reporting to <strong>10 business days following internal confirmation of a material breach</strong> (from 72 hours of discovery) and limited disclosures to an executive summary rather than raw forensic log images.</li>
  </ol>
  <p>Both files have also been uploaded to the shared deal room folder in SharePoint (<code>sites/CymbalAerospace/Shared Documents/BA-2026-AV-8921</code>). Please let me know once your Engineering, Legal, Tax, and Cyber SMEs complete their review.</p>
  <p>Best regards,<br/>
  <strong>Adele Vance</strong><br/>
  VP of Contracts &amp; Legal Counsel | Apex AeroSystems Inc.<br/>
  <code>AdeleV@36zrbd.onmicrosoft.com</code></p>
</div>
""",
        },
        {
            "key": "clm-002-patti-exec-escalation",
            "subject": "URGENT: Close Apex AeroSystems FCC-900 Contract Redlines (BA-2026-AV-8921) Before Today's 4:00 PM Executive Gate",
            "importance": "high",
            "is_read": False,
            "from_name": "Patti Fernandez",
            "from_addr": "PattiF@36zrbd.onmicrosoft.com",
            "to": [{"name": "Rahul Kasanagottu", "address": ADMIN_UPN}],
            "cc": [
                {"name": "Megan Bowen", "address": "MeganB@36zrbd.onmicrosoft.com"},
                {"name": "Lee Gu", "address": "LeeG@36zrbd.onmicrosoft.com"},
                {"name": "Pradeep Gupta", "address": "PradeepG@36zrbd.onmicrosoft.com"},
                {"name": "Alex Wilber", "address": "AlexW@36zrbd.onmicrosoft.com"},
            ],
            "sent_at": f"{today.isoformat()}T13:05:00Z",
            "received_at": f"{today.isoformat()}T13:05:10Z",
            "attachments": [],
            "body_html": f"""
<div style="font-family: Calibri, Arial, sans-serif; font-size: 11pt; color: #1e293b; line-height: 1.55;">
  <p>Rahul,</p>
  <p>Closing <strong>Deal BA-2026-AV-8921 ($45,000,000 FCC-900 Flight Control Computer Subsystem with Apex AeroSystems)</strong> is our <strong>#1 Supply Chain &amp; Procurement priority today</strong>. If we miss the 4:00 PM executive sign-off gate, our Next-Gen Narrowbody flight test instrumentation milestone slips by 6 weeks.</p>
  <p>Here is what I need from you prior to our <strong>1:30 PM Cross-Functional SME Redline Review</strong>:</p>
  <ul>
    <li><strong>Step 1 (Intake &amp; Triage):</strong> Pull Apex AeroSystems' redlined Word contract (<code>Vendor_Redlined_GP1.docx</code>), separate the untouched clauses from the 4 redlined clauses in a clear clause-by-clause diff view, and prepare routing emails for our 4 SME leads.</li>
    <li><strong>Step 2 (FAA &amp; DFARS Non-Negotiables):</strong> Coordinate with <strong>Megan Bowen</strong> (FAA DER) on <code>GP1 §12.2</code> and <strong>Alex Wilber</strong> (CISO) on <code>SP5 §3.2</code> — we cannot violate our FAA Part 21 Production Certificate PC-700 or DoD DFARS 252.204-7012 72-hour cyber reporting mandate.</li>
    <li><strong>Step 3 (Legal &amp; Tariff Harmonization):</strong> Work with <strong>Lee Gu</strong> (Legal) on our Tier-1 Playbook 2.0x PO ($90M) super-cap for <code>GP1 §19 &amp; §24</code>, and with <strong>Pradeep Gupta</strong> (Global Tax) to ensure Apex's <code>SP3 §4.1</code> tariff pass-through does not break our <code>GP1 §3.1</code> $45M Firm-Fixed-Price SOW ceiling.</li>
    <li><strong>Step 4 (Final Counter-Proposal Package):</strong> Generate the official redlined Counter-Proposal <code>.docx</code> and SharePoint Deviation Matrix <code>.xlsx</code> and stage the reply draft back to Adele Vance before our <strong>4:00 PM Executive Contract Sign-Off Gate</strong>.</li>
  </ul>
  <p>Thanks,<br/>
  <strong>Patti Fernandez</strong><br/>
  EVP, Global Supply Chain &amp; Commercial Aircraft Programs | Cymbal Aerospace Corporation</p>
</div>
""",
        },
        {
            "key": "clm-003-megan-faa-der-advisory",
            "subject": "FAA MIDO Audit Alert — Zero Waivers on GP1 §12.2 Source Inspection & 36-Month Avionics Warranty (PC-700)",
            "importance": "high",
            "is_read": False,
            "from_name": "Megan Bowen",
            "from_addr": "MeganB@36zrbd.onmicrosoft.com",
            "to": [{"name": "Rahul Kasanagottu", "address": ADMIN_UPN}],
            "cc": [{"name": "Alex Wilber", "address": "AlexW@36zrbd.onmicrosoft.com"}],
            "sent_at": f"{today.isoformat()}T12:52:00Z",
            "received_at": f"{today.isoformat()}T12:52:10Z",
            "attachments": [],
            "body_html": """
<div style="font-family: Calibri, Arial, sans-serif; font-size: 11pt; color: #1e293b; line-height: 1.55;">
  <p>Rahul,</p>
  <p>Ahead of today's review on <strong>Deal BA-2026-AV-8921 (Apex AeroSystems — FCC-900 Flight Control Subsystem)</strong>, I want to flag a mandatory regulatory lockout from yesterday's FAA Manufacturing Inspection District Office (MIDO) briefing:</p>
  <ul>
    <li>Under <strong>14 CFR Part 21.140 / §21.303</strong> and <strong>AS9100 Rev D</strong>, Cymbal Aerospace's Production Certificate <strong>PC-700</strong> requires unfettered, <strong>unannounced source inspection and quality audit access</strong> at all Tier-1 DAL-A flight control suppliers. Accepting Apex's request for 30 days' prior written notice in <code>GP1 §12.2</code> would trigger an immediate FAA Level-1 non-conformance finding.</li>
    <li>Similarly, Alex Wilber confirmed that under <strong>DoD DFARS 252.204-7012</strong>, we must hold firm on the <strong>72-hour cyber incident reporting window</strong> and forensic log preservation in <code>SP5 §3.2</code> (88% and 94% Held Firm precedent rates in BigQuery across our prior 16 Tier-1 avionics deals).</li>
  </ul>
  <p>Best,<br/>
  <strong>Megan Bowen</strong><br/>
  Chief Airworthiness Engineer &amp; FAA Designated Engineering Representative (DER) | Cymbal Aerospace</p>
</div>
""",
        },
        {
            "key": "clm-004-pradeep-tariff-conflict-note",
            "subject": "Section 232 Titanium & Semiconductor Tariff Exposure vs. GP1 §3.1 Firm-Fixed-Price SOW Cap (BA-2026-AV-8921)",
            "importance": "normal",
            "is_read": False,
            "from_name": "Pradeep Gupta",
            "from_addr": "PradeepG@36zrbd.onmicrosoft.com",
            "to": [{"name": "Rahul Kasanagottu", "address": ADMIN_UPN}],
            "cc": [{"name": "Lee Gu", "address": "LeeG@36zrbd.onmicrosoft.com"}],
            "sent_at": f"{today.isoformat()}T12:30:00Z",
            "received_at": f"{today.isoformat()}T12:30:10Z",
            "attachments": [],
            "body_html": """
<div style="font-family: Calibri, Arial, sans-serif; font-size: 11pt; color: #1e293b; line-height: 1.55;">
  <p>Rahul,</p>
  <p>Quick heads-up on <strong>Apex AeroSystems' redline to <code>SP3 §4.1</code> (Customs, Duties &amp; International Tariffs)</strong>: they are asking to pass through <strong>100% of any Section 232 or Section 301 tariffs above 5%</strong> on titanium forgings and radiation-hardened wafers.</p>
  <p>If Tax accepts an uncapped tariff pass-through in <code>SP3 §4.1</code>, it creates a direct <strong>Cross-Clause Conflict (<code>CONFLICT-SP3-04-GP1-03</code>)</strong> against Procurement's <strong>$45,000,000 Firm-Fixed-Price SOW ceiling in <code>GP1 §3.1</code></strong>. In <strong>63% (10/16) of our Tier-1 Avionics precedents in BigQuery</strong> (including Safran, Spirit AeroSystems, and Honeywell), we resolved this with a <strong>50/50 shared tariff split above 5%, strictly capped at a maximum +2.0% ($900,000) adjustment to the GP1 §3.1 FFP unit price</strong>.</p>
  <p>Regards,<br/>
  <strong>Pradeep Gupta</strong><br/>
  VP Global Tax, Customs &amp; Trade Compliance | Cymbal Aerospace</p>
</div>
""",
        },
        {
            "key": "clm-005-nestor-fal-weekly-digest",
            "subject": f"[FYI] Everett & Renton Final Assembly Line (FAL) Supplier Readiness Digest — Week of {today.isoformat()}",
            "importance": "normal",
            "is_read": True,
            "from_name": "Nestor Wilke",
            "from_addr": "NestorW@36zrbd.onmicrosoft.com",
            "to": [{"name": "Rahul Kasanagottu", "address": ADMIN_UPN}],
            "cc": [],
            "sent_at": f"{yesterday.isoformat()}T21:30:00Z",
            "received_at": f"{yesterday.isoformat()}T21:30:10Z",
            "attachments": [],
            "body_html": """
<div style="font-family: Calibri, Arial, sans-serif; font-size: 11pt; color: #1e293b; line-height: 1.55;">
  <p>Team,</p>
  <p>Weekly Everett &amp; Renton Final Assembly Line (FAL) material readiness summary:</p>
  <ul>
    <li><strong>Green (14/15 Subsystems):</strong> Composite wing spars, landing gear assemblies, APU generators, and cabin environmental control systems are on dock and cleared.</li>
    <li><strong>Red / Critical Path (1/15 Subsystems):</strong> <strong>Deal BA-2026-AV-8921 (Apex AeroSystems — FCC-900 Flight Control Computer Subsystem, $45M)</strong> is awaiting final CLM contract redline reconciliation and counter-proposal signature today.</li>
  </ul>
  <p>— <strong>Nestor Wilke</strong>, Director of Supply Chain Operations, Cymbal Aerospace</p>
</div>
""",
        },
    ]

    # Seed oldest-to-newest so Adele Vance's [URGENT REDLINE] email sits at #1 top of Inbox
    for msg in reversed(emails):
        msg_flag = "1" if msg["is_read"] else "0"
        payload = {
            "subject": msg["subject"],
            "importance": msg["importance"],
            "body": {"contentType": "HTML", "content": msg["body_html"]},
            "from": {"emailAddress": {"name": msg["from_name"], "address": msg["from_addr"]}},
            "sender": {"emailAddress": {"name": msg["from_name"], "address": msg["from_addr"]}},
            "toRecipients": [{"emailAddress": u} for u in msg["to"]],
            "ccRecipients": [{"emailAddress": u} for u in msg["cc"]],
            "sentDateTime": msg["sent_at"],
            "receivedDateTime": msg["received_at"],
            "isDraft": False,
            "isRead": msg["is_read"],
            "singleValueExtendedProperties": [
                {"id": "Integer 0x0E07", "value": msg_flag},
            ],
        }
        if msg["attachments"]:
            payload["attachments"] = msg["attachments"]
        _graph_req(token, "POST", f"/users/{ADMIN_UPN}/mailFolders/Inbox/messages", payload)
        time.sleep(0.5)
        print(
            f"  ✓ [MAIL] Seeded `{msg['key']}` (From: {msg['from_name']}, Read: {msg['is_read']}, Attachments: {len(msg['attachments'])})"
        )


def stage_4_seed_clm_outlook_calendar(token: str) -> None:
    _banner(4, "Seed Fresh Cymbal Aerospace CLM Meetings (Today & Current Week) onto Outlook Calendar")
    today = date.today()
    tomorrow = today + timedelta(days=1)
    monday = today - timedelta(days=today.weekday())
    thursday = monday + timedelta(days=3)
    friday = monday + timedelta(days=4)
    if thursday <= today:
        thursday = today + timedelta(days=2)
    if friday <= today:
        friday = today + timedelta(days=3)

    events = [
        {
            "key": "clm-cal-01-morning-standup",
            "subject": "Cymbal Aerospace Procurement & Supply Chain Morning Standup",
            "start": f"{today.isoformat()}T08:30:00",
            "end": f"{today.isoformat()}T09:00:00",
            "location": "Everett Plant — Bldg 40-88 / Microsoft Teams",
            "body": "Daily procurement standup reviewing Everett & Renton Final Assembly Line critical-path supplier contracts, with primary focus on Deal BA-2026-AV-8921 (Apex AeroSystems $45M FCC-900 Flight Control Subsystem).",
            "attendees": [ADMIN_UPN, "NestorW@36zrbd.onmicrosoft.com", "PattiF@36zrbd.onmicrosoft.com"],
        },
        {
            "key": "clm-cal-02-sme-redline-review",
            "subject": "Cross-Functional SME Redline Review: Deal BA-2026-AV-8921 (Apex AeroSystems $45M FCC-900)",
            "start": f"{today.isoformat()}T13:30:00",
            "end": f"{today.isoformat()}T14:30:00",
            "location": "Everett Executive Briefing Room 3A / Microsoft Teams",
            "body": (
                "Decision Required: Reconcile the 4 material vendor redlines on Deal BA-2026-AV-8921 ($45M FCC-900 Flight Control Computer Subsystem):\n"
                "1. GP1 §12.2 Warranty & FAA Source Inspection (Megan Bowen — Engineering/FAA DER)\n"
                "2. GP1 §19 & §24 Limitation of Liability & IP Indemnity (Lee Gu — Corporate Legal)\n"
                "3. SP3 §4.1 Section 232/301 Tariffs vs. GP1 §3.1 FFP SOW Cap (Pradeep Gupta — Global Tax & Procurement)\n"
                "4. SP5 §3.2 Cybersecurity 72-Hour Incident Reporting (Alex Wilber — Supplier Cyber Defense)"
            ),
            "attendees": [
                ADMIN_UPN,
                "MeganB@36zrbd.onmicrosoft.com",
                "LeeG@36zrbd.onmicrosoft.com",
                "PradeepG@36zrbd.onmicrosoft.com",
                "AlexW@36zrbd.onmicrosoft.com",
            ],
        },
        {
            "key": "clm-cal-03-exec-signoff-gate",
            "subject": "Executive Contract Sign-Off Gate: BA-2026-AV-8921 Counter-Proposal Dispatch",
            "start": f"{today.isoformat()}T16:00:00",
            "end": f"{today.isoformat()}T16:45:00",
            "location": "Everett Executive Boardroom / Microsoft Teams",
            "body": "Decision Required: Final executive sign-off with EVP Patti Fernandez and AGC Lee Gu to dispatch Cymbal Aerospace's official redlined Counter-Proposal (.docx) and SharePoint Deviation Matrix (.xlsx) to Adele Vance at Apex AeroSystems prior to the 48-hour pricing validity cutoff.",
            "attendees": [
                ADMIN_UPN,
                "PattiF@36zrbd.onmicrosoft.com",
                "LeeG@36zrbd.onmicrosoft.com",
                "AdeleV@36zrbd.onmicrosoft.com",
            ],
        },
        {
            "key": "clm-cal-04-faa-mido-audit-prep",
            "subject": "FAA MIDO Production Certificate PC-700 Airworthiness & Supplier Quality Audit Prep",
            "start": f"{tomorrow.isoformat()}T10:00:00",
            "end": f"{tomorrow.isoformat()}T11:00:00",
            "location": "Everett Quality Assurance Lab 2B",
            "body": "Verify 14 CFR Part 21.140 unannounced supplier source inspection compliance and AS9100 Rev D traceability across all Tier-1 DAL-A flight control contracts (including BA-2026-AV-8921).",
            "attendees": [ADMIN_UPN, "MeganB@36zrbd.onmicrosoft.com", "AlexW@36zrbd.onmicrosoft.com"],
        },
        {
            "key": "clm-cal-05-legal-playbook-committee",
            "subject": "Cymbal Aerospace Legal & IP Playbook Committee — Tier-1 Avionics Super-Cap Review",
            "start": f"{thursday.isoformat()}T11:00:00",
            "end": f"{thursday.isoformat()}T12:00:00",
            "location": "Corporate Legal Conference Room / Teams",
            "body": "Review BigQuery historical precedent outcomes (69% Tier-1 Compromise rate at 2.0x PO / $90M super-cap with uncapped AD recall & IP carveouts) for GP1 §19 & §24.",
            "attendees": [ADMIN_UPN, "LeeG@36zrbd.onmicrosoft.com", "JoniS@36zrbd.onmicrosoft.com"],
        },
        {
            "key": "clm-cal-06-tax-tariff-committee",
            "subject": "Global Tax & Procurement Section 232/301 Tariff Risk & FFP SOW Harmonization Sync",
            "start": f"{friday.isoformat()}T14:00:00",
            "end": f"{friday.isoformat()}T15:00:00",
            "location": "Renton Supply Chain Hub / Teams",
            "body": "Review 50/50 shared tariff cap (+2.0% FFP ceiling) across Tier-1 titanium forging and radiation-hardened semiconductor suppliers.",
            "attendees": [ADMIN_UPN, "PradeepG@36zrbd.onmicrosoft.com", "PattiF@36zrbd.onmicrosoft.com"],
        },
    ]

    for evt in events:
        for upn in evt["attendees"]:
            payload = {
                "subject": evt["subject"],
                "body": {"contentType": "Text", "content": evt["body"]},
                "start": {"dateTime": evt["start"], "timeZone": "Central Standard Time"},
                "end": {"dateTime": evt["end"], "timeZone": "Central Standard Time"},
                "location": {"displayName": evt["location"]},
                "isOnlineMeeting": False,
            }
            _graph_req(token, "POST", f"/users/{upn}/events", payload)
        print(f"  ✓ [CALENDAR] Created `{evt['subject']}` ({evt['start']} -> {evt['end']}) for {len(evt['attendees'])} attendees")


def stage_5_verify_environment(token: str) -> None:
    _banner(5, "Live Verification Summary (Outlook Inbox, Drafts, Calendar, SharePoint, BigQuery)")
    inbox = _graph_req(
        token,
        "GET",
        f"/users/{ADMIN_UPN}/mailFolders/Inbox/messages?$top=15&$select=subject,from,receivedDateTime,isRead,hasAttachments&$orderby=receivedDateTime%20desc",
    ).get("value", [])
    print(f"\n  📬 Outlook Inbox (`{ADMIN_UPN}`) — {len(inbox)} messages:")
    for m in inbox:
        sender = m.get("from", {}).get("emailAddress", {}).get("address", "")
        print(
            f"    • [{m.get('receivedDateTime')}] Read={str(m.get('isRead')):<5} Att={str(m.get('hasAttachments')):<5} | {m.get('subject')[:72]} ({sender})"
        )

    drafts = _graph_req(
        token,
        "GET",
        f"/users/{ADMIN_UPN}/mailFolders/Drafts/messages?$top=15&$select=subject",
    ).get("value", [])
    print(f"\n  📝 Outlook Drafts (`{ADMIN_UPN}`) — {len(drafts)} messages (Clean slate ready for Demo Steps 1 & 5)")

    evts = _graph_req(
        token,
        "GET",
        f"/users/{ADMIN_UPN}/events?$top=15&$select=subject,start,end,location&$orderby=start/dateTime%20asc",
    ).get("value", [])
    print(f"\n  📅 Outlook Calendar (`{ADMIN_UPN}`) — {len(evts)} events:")
    for e in evts:
        st = e.get("start", {}).get("dateTime", "")[:16]
        en = e.get("end", {}).get("dateTime", "")[:16]
        loc = e.get("location", {}).get("displayName", "")
        print(f"    • [{st} -> {en}] {e.get('subject')} @ {loc}")

    try:
        site = _graph_req(token, "GET", "/sites/36zrbd.sharepoint.com:/sites/CymbalAerospace")
        drive = _graph_req(token, "GET", f"/sites/{site['id']}/drive")
        children = _graph_req(
            token,
            "GET",
            f"/drives/{drive['id']}/root:/BA-2026-AV-8921:/children?$select=name,size,lastModifiedDateTime",
        ).get("value", [])
        print(f"\n  📁 SharePoint (`sites/CymbalAerospace/Shared Documents/BA-2026-AV-8921`) — {len(children)} files ready:")
        for c in children:
            print(f"    • {c['name']} ({c['size']} bytes, modified={c['lastModifiedDateTime']})")
    except Exception as exc:
        print(f"\n  ! SharePoint check note: {exc}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Bake the Cymbal Aerospace CLM Demo environment (Outlook Mail & Calendar + Deal Reset).")
    parser.add_argument("--quick", action="store_true", help="Fast bake (same as full: cleans & seeds Outlook Mail/Calendar + resets CLM deal)")
    parser.add_argument("--full", action="store_true", help="Full bake (default)")
    parser.parse_args()

    t0 = time.time()
    print("##############################################################################")
    print("#  CYMBAL AEROSPACE CLM DEMO — BAKE SCRIPT (OUTLOOK MAIL + CALENDAR + CLM)   #")
    print("##############################################################################")

    token = _get_graph_token()
    stage_1_reset_deal_and_sync_skills()
    stage_2_purge_outlook_mail_and_calendar(token)
    stage_3_seed_clm_outlook_inbox(token)
    stage_4_seed_clm_outlook_calendar(token)
    stage_5_verify_environment(token)

    elapsed = time.time() - t0
    print(f"\n{'=' * 78}")
    print(f"  CYMBAL AEROSPACE CLM DEMO BAKE COMPLETE in {elapsed:.1f}s — READY FOR LIVE DEMO!")
    print(f"{'=' * 78}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
