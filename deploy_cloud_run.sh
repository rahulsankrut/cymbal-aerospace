#!/usr/bin/env bash
set -euo pipefail

# Enforce mandatory resource attribution for all gcloud CLI operations
export CLOUDSDK_METRICS_ENVIRONMENT="${CLOUDSDK_METRICS_ENVIRONMENT:+$CLOUDSDK_METRICS_ENVIRONMENT }datacloud.antigravity"

PROJECT_ID="${GCP_PROJECT_ID:-vertex-ai-demos-468803}"
REGION="${GCP_REGION:-us-central1}"
SERVICE_NAME="${SERVICE_NAME:-boeing-clm-engine}"
BQ_DATASET="${BQ_DATASET:-boeing_clm}"

echo "================================================================================"
echo "Deploying ${SERVICE_NAME} to Cloud Run in project ${PROJECT_ID} (${REGION})"
echo "BigQuery Dataset: ${PROJECT_ID}.${BQ_DATASET}"
echo "================================================================================"

gcloud run deploy "${SERVICE_NAME}" \
  --project="${PROJECT_ID}" \
  --region="${REGION}" \
  --source="." \
  --allow-unauthenticated \
  --port=8080 \
  --memory=1Gi \
  --cpu=2 \
  --set-env-vars="GCP_PROJECT_ID=${PROJECT_ID},BQ_DATASET=${BQ_DATASET}" \
  --labels="datacloud=antigravity,app=boeing-clm" \
  --quiet

SERVICE_URL="$(gcloud run services describe "${SERVICE_NAME}" \
  --project="${PROJECT_ID}" \
  --region="${REGION}" \
  --format='value(status.url)')"

echo "================================================================================"
echo "Cloud Run Deployment Complete!"
echo "Experience Layer UI : ${SERVICE_URL}/"
echo "REST API Base       : ${SERVICE_URL}/api/deals/BA-2026-AV-8921"
echo "FastMCP Endpoint    : ${SERVICE_URL}/mcp"
echo "================================================================================"
