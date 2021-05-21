# Stage 1 - Base
FROM python:3.7-slim as base

# Stage 2 - Build
FROM base as builder
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean
COPY requirements.txt /app/requirements.txt
WORKDIR app
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 3 - Production Image
FROM base
COPY --from=builder /root/.local /usr/local
COPY . app

WORKDIR app
# ENV PATH=/root/.local/bin:$PATH
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080", "--header", "server:bangkitws"]