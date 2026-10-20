"""Export Cymbal Aerospace counter-proposal & deviation matrix and upload full deal package to SharePoint."""

from __future__ import annotations

import shutil
from pathlib import Path
import httpx

from boeing_clm.export.docx_generator import generate_counter_proposal_docx
from boeing_clm.export.xlsx_generator import generate_deviation_matrix_xlsx
from boeing_clm.storage.repository import BigQueryCLMRepository

FIXTURES_DIR = Path(__file__).resolve().parent / "specs" / "04_golden_fixtures"
ENV_PATH = Path("/Users/rahulsankrut/Desktop/code/Cymbal/spark-demo/.env")

SITE_ID = "36zrbd.sharepoint.com,d1515f3c-a939-4021-ad08-54685f2a8b4e,16bfad20-745e-449e-885e-4fa91d4926a6"
DRIVE_ID = "b!PF9R0TmpIUCtCFRoXyqLTiCtvxZedJ5EiF5PqR1JJqYL-miSQnAlTqOjt3p6ITnO"
DEAL_FOLDER = "BA-2026-AV-8921"


def load_env(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def get_graph_token(env: dict[str, str]) -> str:
    tenant_id = env["AZURE_TENANT_ID"]
    client_id = env["AZURE_CLIENT_ID"]
    client_secret = env["AZURE_CLIENT_SECRET"]
    resp = httpx.post(
        f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token",
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": "https://graph.microsoft.com/.default",
            "grant_type": "client_credentials",
        },
        timeout=30.0,
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


def generate_export_fixtures() -> None:
    repo = BigQueryCLMRepository()
    deal = repo.get_deal_workbench_state("BA-2026-AV-8921")

    cymbal_counter = FIXTURES_DIR / "BA-2026-AV-8921_Cymbal_Counter_Proposal.docx"
    boeing_counter = FIXTURES_DIR / "BA-2026-AV-8921_Boeing_Counter_Proposal.docx"
    matrix_xlsx = FIXTURES_DIR / "BA-2026-AV-8921_SharePoint_Deviation_Matrix.xlsx"

    generate_counter_proposal_docx(deal, cymbal_counter)
    shutil.copyfile(cymbal_counter, boeing_counter)
    generate_deviation_matrix_xlsx(deal, matrix_xlsx)

    print(f"[export] Wrote {cymbal_counter.name} ({cymbal_counter.stat().st_size:,} bytes)")
    print(f"[export] Wrote {matrix_xlsx.name} ({matrix_xlsx.stat().st_size:,} bytes)")


def upload_to_sharepoint() -> None:
    env = load_env(ENV_PATH)
    token = get_graph_token(env)
    headers = {"Authorization": f"Bearer {token}"}

    files_to_upload = [
        FIXTURES_DIR / "Cymbal_GP1_Standard.docx",
        FIXTURES_DIR / "Vendor_Redlined_GP1.docx",
        FIXTURES_DIR / "Cymbal_SOW_Schedule_A_Pricing.docx",
        FIXTURES_DIR / "Apex_AeroSystems_Redline_Transmittal_Memo.docx",
        FIXTURES_DIR / "BA-2026-AV-8921_SharePoint_Deviation_Matrix.xlsx",
        FIXTURES_DIR / "BA-2026-AV-8921_Cymbal_Counter_Proposal.docx",
    ]

    with httpx.Client(timeout=60.0) as client:
        for file_path in files_to_upload:
            url = (
                f"https://graph.microsoft.com/v1.0/drives/{DRIVE_ID}"
                f"/root:/{DEAL_FOLDER}/{file_path.name}:/content"
            )
            content = file_path.read_bytes()
            resp = client.put(
                url,
                headers={
                    **headers,
                    "Content-Type": "application/octet-stream",
                },
                content=content,
            )
            resp.raise_for_status()
            item = resp.json()
            print(
                f"[sharepoint] Uploaded {item['name']} ({item['size']:,} bytes) -> {item['webUrl']}"
            )

        # Also upload Cymbal_GP1_Standard.docx at root of Shared Documents as master template
        master_path = FIXTURES_DIR / "Cymbal_GP1_Standard.docx"
        resp_root = client.put(
            f"https://graph.microsoft.com/v1.0/drives/{DRIVE_ID}/root:/Templates/{master_path.name}:/content",
            headers={**headers, "Content-Type": "application/octet-stream"},
            content=master_path.read_bytes(),
        )
        resp_root.raise_for_status()
        root_item = resp_root.json()
        print(
            f"[sharepoint] Uploaded Master Template {root_item['name']} -> {root_item['webUrl']}"
        )

        # Verify children of BA-2026-AV-8921 folder
        children_resp = client.get(
            f"https://graph.microsoft.com/v1.0/drives/{DRIVE_ID}/root:/{DEAL_FOLDER}:/children",
            headers=headers,
        )
        children_resp.raise_for_status()
        children = children_resp.json().get("value", [])
        print(f"\n[sharepoint] Verified {len(children)} files in /sites/CymbalAerospace/Shared Documents/{DEAL_FOLDER}:")
        for c in children:
            print(f"  - {c['name']} ({c['size']:,} bytes): {c['webUrl']}")


if __name__ == "__main__":
    generate_export_fixtures()
    upload_to_sharepoint()
