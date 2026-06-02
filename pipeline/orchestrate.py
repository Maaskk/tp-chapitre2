"""Étape 5 : orchestration du pipeline avec Dagster.

L'ordre exécuté est : ingestion -> validation -> transformation dbt -> tests dbt.
"""

from pathlib import Path
import subprocess

from dagster import job, op

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run_command(command: list[str], cwd: Path = PROJECT_ROOT) -> str:
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(
            "Commande échouée : " + " ".join(command) + "\n" + result.stdout + "\n" + result.stderr
        )
    print(result.stdout)
    return "ok"


@op
def ingest() -> str:
    return run_command(["python", "pipeline/ingest.py"])


@op
def validate(_ingestion_status: str) -> str:
    return run_command(["python", "pipeline/validate.py"])


@op
def transform(_validation_status: str) -> str:
    return run_command(["dbt", "run", "--profiles-dir", "."], cwd=PROJECT_ROOT / "dbt_pipeline")


@op
def test_data(_transformation_status: str) -> str:
    return run_command(["dbt", "test", "--profiles-dir", "."], cwd=PROJECT_ROOT / "dbt_pipeline")


@job
def ventes_pipeline():
    test_data(transform(validate(ingest())))
