#! /usr/bin/env bash
set -e

uvicorn app.main:app --host 0.0.0.0 --port 9024 --backlog 8192 --workers 10 --forwarded-allow-ips '*'
