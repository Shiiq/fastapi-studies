#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

alembic upgrade head
sleep .5
python data_storage/upload.py
sleep .5
uvicorn fastapi_studies.main:app --host 0.0.0.0
