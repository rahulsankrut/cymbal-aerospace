"""
connect_ge_environment.py

Connects the BigQuery instance (`vertex-ai-demos-468803.boeing_clm`) and the Cloud Run MCP Server
(`https://boeing-clm-engine-5udif2v3cq-uc.a.run.app/mcp`) to the Gemini Enterprise environment
`connectors-demo_1787861880280` (`Connectors Demo`).
"""
from __future__ import annotations

import json
from pathlib import Path
import time
import urllib.parse

from install_gemini_enterprise_skills import PROJECT_ID, api_request, get_access_token

ENGINE_ID = "connectors-demo_1787861880280"
MCP_SERVER_URL = "https://boeing-clm-engine-5udif2v3cq-uc.a.run.app/mcp"
BQ_DATASET_URI = "bigquery://vertex-ai-demos-468803.boeing_clm"
BQ_COLLECTION_ID = "clm-bq-connector"
MCP_COLLECTION_ID = "clm-mcp-connector"
TOOLSPEC_PATH = Path(__file__).resolve().parent / "toolspec.json"


def register_mcp_server_in_agent_registry(token: str) -> dict[str, str]:
    """Verify or register the Cloud Run MCP Server (`clm-mcp-server`) in Agent Registry (`global` and `us-central1`)."""
    toolspec_dict = json.loads(TOOLSPEC_PATH.read_text())

    registry_mcp_names: dict[str, str] = {}
    for loc in ["global", "us-central1"]:
        base_url = f"https://agentregistry.googleapis.com/v1alpha/projects/{PROJECT_ID}/locations/{loc}/services"
        st, existing = api_request("GET", f"{base_url}/clm-mcp-server", token, timeout=15)
        if st == 200 and isinstance(existing, dict):
            mcp_res = existing.get("mcpServer", "")
            print(f"[AGENT REGISTRY ({loc})] Service clm-mcp-server ACTIVE -> mcpServer={mcp_res}")
            if mcp_res:
                registry_mcp_names[loc] = mcp_res
            continue

        payload = {
            "displayName": "CLM Engine MCP Server",
            "description": (
                "Deterministic OOXML Track-Changes (.docx/.xlsx), BigQuery Vector Search (text-embedding-005), "
                "and Cross-Clause Conflict & Regulatory Lockout MCP Server for Contract Lifecycle Management."
            ),
            "interfaces": [
                {
                    "url": MCP_SERVER_URL,
                    "protocolBinding": "JSONRPC",
                }
            ],
            "mcpServerSpec": {
                "type": "TOOL_SPEC",
                "content": toolspec_dict,
            },
        }
        st_c, resp_c = api_request("POST", f"{base_url}?serviceId=clm-mcp-server", token, payload, timeout=20)
        print(f"[AGENT REGISTRY ({loc})] POST clm-mcp-server -> status={st_c}: {json.dumps(resp_c)[:350]}")
        time.sleep(3)
        st_g, created = api_request("GET", f"{base_url}/clm-mcp-server", token, timeout=15)
        if st_g == 200 and isinstance(created, dict):
            mcp_res = created.get("mcpServer", "")
            print(f"  -> {loc} mcpServer resource: {mcp_res}")
            if mcp_res:
                registry_mcp_names[loc] = mcp_res

    return registry_mcp_names


def setup_bigquery_connector(token: str) -> list[str]:
    """Verify the `clm-bq-connector` DataConnector for `vertex-ai-demos-468803.boeing_clm`."""
    dc_url = (
        f"https://discoveryengine.googleapis.com/v1alpha/projects/{PROJECT_ID}/"
        f"locations/global/collections/{BQ_COLLECTION_ID}/dataConnector"
    )
    st, existing = api_request("GET", dc_url, token, timeout=15)
    ds_ids: list[str] = []
    if st == 200 and isinstance(existing, dict):
        print(f"[DISCOVERY ENGINE] {BQ_COLLECTION_ID} state={existing.get('state')}")
        for ent in existing.get("entities", []):
            ds_full = ent.get("dataStore", "")
            if ds_full:
                ds_id = ds_full.split("/")[-1]
                ds_ids.append(ds_id)
                print(f"  - Entity {ent.get('entityName')} -> dataStoreId: {ds_id}")
    return ds_ids


def setup_custom_mcp_connector(token: str, registry_mcp_names: dict[str, str]) -> list[str]:
    """Create the `clm-mcp-connector` Custom MCP DataConnector for Cloud Run `/mcp`."""
    dc_url = (
        f"https://discoveryengine.googleapis.com/v1alpha/projects/{PROJECT_ID}/"
        f"locations/global/collections/{MCP_COLLECTION_ID}/dataConnector"
    )
    st, existing = api_request("GET", dc_url, token, timeout=15)
    if st != 200:
        reg_name = registry_mcp_names.get("us-central1") or registry_mcp_names.get("global")
        action_params: dict = {
            "instance_uri": MCP_SERVER_URL,
            "auth_type": "NO_AUTH",
            "mcp_server_source": "REGISTRY_MCP" if reg_name else "BYO_MCP",
            "use_agent_gateway_egress": False,
        }
        if reg_name:
            action_params["registry_mcp_server_name"] = reg_name

        # Try setUpDataConnectorV2 first, then setUpDataConnector with oauth_access_token
        q = urllib.parse.urlencode(
            {
                "collectionId": MCP_COLLECTION_ID,
                "collectionDisplayName": "CLM Engine MCP Connector",
            }
        )
        v2_url = f"https://discoveryengine.googleapis.com/v1alpha/projects/{PROJECT_ID}/locations/global:setUpDataConnectorV2?{q}"
        dc_body = {
            "dataSource": "custom_mcp",
            "params": {
                "oauth_access_token": token,
            },
            "refreshInterval": "86400s",
            "entities": [
                {
                    "entityName": "mcp_data",
                }
            ],
            "actionConfig": {
                "actionParams": action_params,
                "createBapConnection": True,
            },
            "bapConfig": {
                "enabledActions": [
                    "ingest_vendor_redline",
                    "analyze_clause_precedents",
                    "record_sme_position",
                    "harmonize_clause_conflict",
                    "export_counter_proposal_package",
                    "reset_deal_workbench",
                ]
            },
            "connectorType": "THIRD_PARTY_FEDERATED",
            "connectorModes": ["FEDERATED"],
            "connectorSourceId": "custom_mcp",
        }
        st_s, resp_s = api_request("POST", v2_url, token, dc_body, timeout=30)
        print(f"[DISCOVERY ENGINE] POST setUpDataConnectorV2 ({MCP_COLLECTION_ID}) -> status={st_s}: {json.dumps(resp_s)[:500]}")
        time.sleep(8)
        st, existing = api_request("GET", dc_url, token, timeout=15)

    ds_ids: list[str] = []
    if st == 200 and isinstance(existing, dict):
        print(f"[DISCOVERY ENGINE] {MCP_COLLECTION_ID} state={existing.get('state')}")
        for ent in existing.get("entities", []):
            ds_full = ent.get("dataStore", "")
            if ds_full:
                ds_id = ds_full.split("/")[-1]
                ds_ids.append(ds_id)
                print(f"  - Entity {ent.get('entityName')} -> dataStoreId: {ds_id}")
    return ds_ids


def attach_datastores_to_engine(token: str, new_ds_ids: list[str]) -> None:
    """Attach the new BigQuery and MCP dataStoreIds to `connectors-demo_1787861880280`."""
    if not new_ds_ids:
        print("[ENGINE] No new dataStoreIds to attach.")
        return

    eng_url = (
        f"https://discoveryengine.googleapis.com/v1alpha/projects/{PROJECT_ID}/"
        f"locations/global/collections/default_collection/engines/{ENGINE_ID}"
    )
    st, eng = api_request("GET", eng_url, token, timeout=15)
    if st != 200 or not isinstance(eng, dict):
        print(f"[ENGINE] Failed to GET engine {ENGINE_ID}: status={st}")
        return

    current_ids: list[str] = list(eng.get("dataStoreIds", []))
    merged_ids = list(current_ids)
    for dsid in new_ds_ids:
        if dsid not in merged_ids:
            merged_ids.append(dsid)

    if merged_ids == current_ids:
        print(f"[ENGINE] All dataStoreIds already attached to {ENGINE_ID}: {new_ds_ids}")
        return

    patch_url = f"{eng_url}?updateMask=dataStoreIds"
    st_p, resp_p = api_request("PATCH", patch_url, token, {"dataStoreIds": merged_ids}, timeout=30)
    print(f"[ENGINE] PATCH {ENGINE_ID} dataStoreIds -> status={st_p}: {json.dumps(resp_p)[:400]}")


def main() -> None:
    token = get_access_token()
    print("=== 1. Registering Cloud Run MCP Server in Agent Registry ===")
    registry_mcp_names = register_mcp_server_in_agent_registry(token)

    print("\n=== 2. Verifying BigQuery Connector (clm-bq-connector) ===")
    bq_ds_ids = setup_bigquery_connector(token)

    print("\n=== 3. Setting Up Custom MCP Connector (clm-mcp-connector) ===")
    mcp_ds_ids = setup_custom_mcp_connector(token, registry_mcp_names)

    print("\n=== 4. Attaching Connectors to Engine connectors-demo_1787861880280 ===")
    attach_datastores_to_engine(token, bq_ds_ids + mcp_ds_ids)


if __name__ == "__main__":
    main()
