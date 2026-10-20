"""
install_gemini_enterprise_skills.py

Packages the 5 CLM skills (`clm-*`) as specification-compliant ZIP archives (`SKILL.md` at archive root + `scripts/clm_cli.py`),
removes legacy `boeing-*` skill directories, and installs + activates the 5 skills across:
1. Gemini Enterprise (Argolis) Desktop App local workspace (`/Users/rahulsankrut/ge_spark_workspace/skills/<skill_id>/`)
2. Antigravity local skill directories (`~/.gemini/config/skills/`, `~/.agents/skills/`, `.agents/skills/`)
3. Gemini Enterprise Agent Platform Skill Registry (`aiplatform.googleapis.com/v1beta1/.../skills`)
4. Google Cloud Agent Registry (`agentregistry.googleapis.com/v1alpha/.../skills`) -> promoted to TARGET_STATE_ACTIVE
5. Gemini Enterprise Discovery Engine Assistant Agents (`connectors-demo_1787861880280/assistants/default_assistant/agents`)
"""
from __future__ import annotations

import base64
import io
import json
from pathlib import Path
import shutil
import subprocess
import time
import urllib.error
import urllib.request
import zipfile

PROJECT_ID = "vertex-ai-demos-468803"
LOCATION = "us-central1"
SKILLS_DIR = Path(__file__).resolve().parent / "skills"
CLI_HELPER_SRC = SKILLS_DIR / "clm_cli.py"

LOCAL_SKILL_TARGETS = [
    Path.home() / "ge_spark_workspace" / "skills",
    Path.home() / ".gemini" / "config" / "skills",
    Path.home() / ".agents" / "skills",
    Path(__file__).resolve().parent / ".agents" / "skills",
]

SKILLS_METADATA = [
    {
        "skill_id": "clm-contract-intake",
        "display_name": "clm-contract-intake",
        "description": (
            "Deterministically parses vendor-redlined aerospace contracts (.docx) with Word Track Changes "
            "(<w:ins>, <w:del>, <w:comment>) using the CLM Engine MCP tool (ingest_vendor_redline), "
            "persists clause deviations in BigQuery, renders the Triage Matrix in Canvas, and dispatches "
            "Microsoft Teams SME alerts."
        ),
    },
    {
        "skill_id": "clm-legal-ip-review",
        "display_name": "clm-legal-ip-review",
        "description": (
            "Conducts Corporate Legal & IP review on GP1 §19 & §24 (Limitation of Liability & IP Indemnity) "
            "using the CLM Engine MCP tools (analyze_clause_precedents and record_sme_position) backed by "
            "live BigQuery Vector Search and Gemini Agent Canvas."
        ),
    },
    {
        "skill_id": "clm-tax-tariff-review",
        "display_name": "clm-tax-tariff-review",
        "description": (
            "Conducts Global Tax & Trade review on SP3 §4.1 (Customs, Duties & Section 232/301 Tariffs), "
            "enforces deterministic cross-clause conflict detection against GP1 §3.1 (Firm-Fixed-Price SOW Cap) "
            "via CLM Engine MCP tools (analyze_clause_precedents, record_sme_position, harmonize_clause_conflict), "
            "and commits the harmonized cap in BigQuery."
        ),
    },
    {
        "skill_id": "clm-eng-faa-review",
        "display_name": "clm-eng-faa-review",
        "description": (
            "Conducts Engineering/QA (FAA DER) and Supplier Cyber Defense review on GP1 §12.2 "
            "(Warranty & FAA Source Inspection) and SP5 §3.2 (Cyber Incident Reporting) using CLM Engine MCP tools "
            "(analyze_clause_precedents and record_sme_position) to enforce FAA 14 CFR Part 21 and "
            "DFARS 252.204-7012 regulatory lockouts."
        ),
    },
    {
        "skill_id": "clm-contract-consolidation",
        "display_name": "clm-contract-consolidation",
        "description": (
            "Consolidates all SME clause reviews in BigQuery, verifies zero active conflicts, calls "
            "export_counter_proposal_package to deterministically generate the 12-clause Counter-Proposal .docx "
            "with native Word Track Changes (<w:ins>/<w:del>) & margin comments (<w:comment>) plus the 4-tab "
            "SharePoint Deviation Matrix .xlsx, renders the contract in Canvas, and dispatches via M365 connectors."
        ),
    },
]


def get_access_token() -> str:
    """Obtain an OAuth2 access token via gcloud CLI with mandatory resource attribution."""
    env = dict(subprocess.os.environ)
    existing = env.get("CLOUDSDK_METRICS_ENVIRONMENT", "")
    env["CLOUDSDK_METRICS_ENVIRONMENT"] = f"{existing} datacloud.antigravity".strip()
    out = subprocess.check_output(
        ["gcloud", "auth", "print-access-token"],
        env=env,
        text=True,
    ).strip()
    return out


def api_request(
    method: str,
    url: str,
    token: str,
    body: dict | None = None,
    timeout: int = 20,
) -> tuple[int, dict | str]:
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "x-goog-user-project": PROJECT_ID,
    }
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8")
            try:
                return resp.status, json.loads(raw)
            except json.JSONDecodeError:
                return resp.status, raw
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", errors="replace")
        try:
            return e.code, json.loads(raw)
        except json.JSONDecodeError:
            return e.code, raw


def cleanup_legacy_boeing_skill_dirs() -> None:
    for root in [SKILLS_DIR, *LOCAL_SKILL_TARGETS]:
        if not root.exists():
            continue
        for item in root.iterdir():
            if item.name.startswith("boeing-"):
                if item.is_dir():
                    shutil.rmtree(item)
                    print(f"[CLEANUP] Removed legacy skill directory: {item}")
                else:
                    item.unlink()
                    print(f"[CLEANUP] Removed legacy skill file: {item}")


def install_into_local_workspaces(skill_id: str) -> None:
    """Install `SKILL.md` and `scripts/clm_cli.py` into source `skills/` and all local Desktop App skill folders."""
    skill_src_dir = SKILLS_DIR / skill_id
    skill_md_path = skill_src_dir / "SKILL.md"
    if not skill_md_path.exists():
        raise FileNotFoundError(f"Missing SKILL.md at {skill_md_path}")

    # Ensure scripts/clm_cli.py is inside the source skill directory
    if CLI_HELPER_SRC.exists():
        scripts_dir = skill_src_dir / "scripts"
        scripts_dir.mkdir(parents=True, exist_ok=True)
        target_cli = scripts_dir / "clm_cli.py"
        shutil.copy2(CLI_HELPER_SRC, target_cli)
        target_cli.chmod(0o755)

    for target_root in LOCAL_SKILL_TARGETS:
        target_root.mkdir(parents=True, exist_ok=True)
        dest_skill_dir = target_root / skill_id
        dest_skill_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(skill_md_path, dest_skill_dir / "SKILL.md")
        if CLI_HELPER_SRC.exists():
            dest_scripts = dest_skill_dir / "scripts"
            dest_scripts.mkdir(parents=True, exist_ok=True)
            dest_cli = dest_scripts / "clm_cli.py"
            shutil.copy2(CLI_HELPER_SRC, dest_cli)
            dest_cli.chmod(0o755)
        print(f"[LOCAL DESKTOP SKILL] Installed {skill_id} -> {dest_skill_dir}")


def build_skill_zip(skill_id: str) -> tuple[Path, str]:
    skill_md_path = SKILLS_DIR / skill_id / "SKILL.md"
    if not skill_md_path.exists():
        raise FileNotFoundError(f"Missing SKILL.md at {skill_md_path}")

    zip_path = SKILLS_DIR / f"{skill_id}.zip"
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(skill_md_path, arcname="SKILL.md")
        cli_script = SKILLS_DIR / skill_id / "scripts" / "clm_cli.py"
        if cli_script.exists():
            zf.write(cli_script, arcname="scripts/clm_cli.py")
    zip_bytes = buf.getvalue()
    zip_path.write_bytes(zip_bytes)
    b64_str = base64.b64encode(zip_bytes).decode("ascii")
    return zip_path, b64_str


def install_in_vertex_skill_registry(token: str, skill: dict, b64_zip: str) -> dict:
    skill_id = skill["skill_id"]
    base_url = f"https://{LOCATION}-aiplatform.googleapis.com/v1beta1/projects/{PROJECT_ID}/locations/{LOCATION}/skills"

    status, existing = api_request("GET", f"{base_url}/{skill_id}", token)
    if status == 200 and isinstance(existing, dict):
        print(f"[AIPLATFORM SKILL REGISTRY] {skill_id} state={existing.get('state')} (resource={existing.get('name')})")
        return {"status": status, "response": existing}

    create_url = f"{base_url}?skillId={skill_id}"
    payload = {
        "displayName": skill["display_name"],
        "description": skill["description"],
        "zippedFilesystem": b64_zip,
    }
    st, resp = api_request("POST", create_url, token, payload)
    print(f"[AIPLATFORM SKILL REGISTRY] POST {skill_id} -> status={st}: {json.dumps(resp)[:300]}")
    return {"status": st, "response": resp}


def install_and_activate_in_agent_registry(token: str, skill: dict, b64_zip: str, location: str = "global") -> None:
    skill_id = skill["skill_id"]
    base_url = f"https://agentregistry.googleapis.com/v1alpha/projects/{PROJECT_ID}/locations/{location}/skills"
    private_id = f"private-{skill_id}"

    status, existing = api_request("GET", f"{base_url}/{private_id}", token)
    if status != 200:
        create_url = f"{base_url}?skillId={skill_id}"
        payload = {
            "displayName": skill["display_name"],
            "description": skill["description"],
            "type": "SIMPLE",
            "targetState": "TARGET_STATE_DRAFT",
            "initialRevision": {
                "archiveUploadSource": {
                    "archiveContent": b64_zip,
                }
            },
        }
        st, resp = api_request("POST", create_url, token, payload)
        print(f"[AGENT REGISTRY ({location})] POST {skill_id} -> status={st}")
        time.sleep(4)

    # Fetch revisions to find the active revision resource name
    st_r, revs = api_request("GET", f"{base_url}/{private_id}/revisions", token)
    if st_r == 200 and isinstance(revs, dict) and revs.get("skillRevisions"):
        rev_name = revs["skillRevisions"][0]["name"]
        patch_url = f"{base_url}/{private_id}?updateMask=targetState,defaultRevision"
        st_p, resp_p = api_request(
            "PATCH",
            patch_url,
            token,
            {"targetState": "TARGET_STATE_ACTIVE", "defaultRevision": rev_name},
        )
        print(f"[AGENT REGISTRY ({location})] PATCH {private_id} (ACTIVE) -> status={st_p}")
        time.sleep(1)
        st_g, info = api_request("GET", f"{base_url}/{private_id}", token)
        if isinstance(info, dict):
            print(
                f"  -> {private_id}: state={info.get('state')} | targetState={info.get('targetState')} "
                f"| skillId={info.get('skillId')} | defaultRevision={info.get('defaultRevision')}"
            )


def install_in_gemini_enterprise_engine(
    token: str,
    skill: dict,
    engine_id: str = "connectors-demo_1787861880280",
) -> dict:
    """Install or update the skill as a `skillAgentDefinition` agent inside the Gemini Enterprise Engine (`default_assistant`)."""
    skill_id = skill["skill_id"]
    skill_md_path = SKILLS_DIR / skill_id / "SKILL.md"
    instruction = skill_md_path.read_text(encoding="utf-8")

    agents_url = (
        f"https://discoveryengine.googleapis.com/v1alpha/projects/{PROJECT_ID}"
        f"/locations/global/collections/default_collection/engines/{engine_id}"
        f"/assistants/default_assistant/agents"
    )

    st_list, list_resp = api_request("GET", agents_url, token)
    existing_agent = None
    if st_list == 200 and isinstance(list_resp, dict):
        for ag in list_resp.get("agents", []):
            if ag.get("displayName") == skill["display_name"]:
                existing_agent = ag
                break

    payload = {
        "displayName": skill["display_name"],
        "description": skill["description"],
        "sharingConfig": {
            "scope": "ALL_USERS",
        },
        "skillAgentDefinition": {
            "instruction": instruction,
        },
    }

    if existing_agent:
        agent_name = existing_agent["name"]
        patch_url = f"https://discoveryengine.googleapis.com/v1alpha/{agent_name}?updateMask=displayName,description,sharingConfig,skillAgentDefinition.instruction"
        st_p, resp_p = api_request("PATCH", patch_url, token, payload)
        print(
            f"[GEMINI ENTERPRISE ENGINE ({engine_id})] PATCH {skill_id} -> status={st_p} (name={agent_name})"
        )
        return {"status": st_p, "response": resp_p}

    st_c, resp_c = api_request("POST", agents_url, token, payload)
    created_name = resp_c.get("name") if isinstance(resp_c, dict) else ""
    gcs_uri = (
        resp_c.get("skillAgentDefinition", {}).get("gcsUri")
        if isinstance(resp_c, dict)
        else ""
    )
    print(
        f"[GEMINI ENTERPRISE ENGINE ({engine_id})] POST {skill_id} -> status={st_c} (name={created_name} | gcsUri={gcs_uri})"
    )
    return {"status": st_c, "response": resp_c}


def main() -> None:
    cleanup_legacy_boeing_skill_dirs()
    token = get_access_token()

    print("--- Installing & Activating 5 CLM Skills (Local Desktop + Cloud Registries) ---")
    for skill in SKILLS_METADATA:
        install_into_local_workspaces(skill["skill_id"])
        _, b64_zip = build_skill_zip(skill["skill_id"])
        install_in_vertex_skill_registry(token, skill, b64_zip)
        install_and_activate_in_agent_registry(token, skill, b64_zip, location="global")
        install_in_gemini_enterprise_engine(token, skill, engine_id="connectors-demo_1787861880280")


if __name__ == "__main__":
    main()
