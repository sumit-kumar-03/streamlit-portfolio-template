FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# Dependencies first, so code changes don't invalidate this layer
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# App code (docker-compose mounts over this for live editing)
COPY . .

EXPOSE 8501

ENTRYPOINT ["/usr/src/app/scripts/entrypoint.sh"]
