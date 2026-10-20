FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080 \
    BOEING_CLM_ROOT=/app \
    PYTHONPATH=/app/src:/app \
    GCP_PROJECT_ID=vertex-ai-demos-468803 \
    BQ_DATASET=boeing_clm

WORKDIR /app

COPY pyproject.toml ./
COPY src ./src
COPY specs ./specs
COPY skills ./skills

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -e . && \
    mkdir -p /app/data/exports

EXPOSE 8080

CMD ["sh", "-c", "uvicorn boeing_clm.server.api_server:app --host 0.0.0.0 --port ${PORT:-8080}"]
