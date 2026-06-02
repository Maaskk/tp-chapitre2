#!/usr/bin/env bash
set -e

echo "1) Ingestion"
python pipeline/ingest.py

echo "2) Validation"
python pipeline/validate.py

echo "3) dbt debug/run/test"
cd dbt_pipeline
dbt debug --profiles-dir .
dbt run --profiles-dir .
dbt test --profiles-dir .
cd ..

echo "✅ Pipeline terminé avec succès. Pour Dagster, lance :"
echo "dagster dev -f pipeline/orchestrate.py"
