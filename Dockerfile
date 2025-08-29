# FastAPI on Python 3.11
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# System deps for building wheels (bcrypt, cryptography, asyncpg, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libffi-dev libssl-dev curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Dependencies
COPY requirements.txt ./requirements.txt

# Convert UTF-16 -> UTF-8 if detected (BuildKit not required)
RUN python -c "import pathlib; p=pathlib.Path('requirements.txt'); b=p.read_bytes(); \
is_utf16 = b.startswith(b'\xff\xfe') or b.startswith(b'\xfe\xff'); \
(p.write_bytes(b.decode('utf-16').encode('utf-8')) if is_utf16 else None)"

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

# App code
COPY . .

# Default upload temp dir (compose mounts a volume here)
ENV UPLOAD_TMP_DIR=/data/tmp
RUN mkdir -p \"${UPLOAD_TMP_DIR}\"

EXPOSE 8000

# If you're behind nginx, proxy headers help
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--forwarded-allow-ips", "*"]
