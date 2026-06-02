"""Étape 1 : ingestion des données CSV vers DuckDB.

Le TP demande de charger un fichier CSV de ventes dans une table DuckDB nommée
ventes_raw. Cette étape représente l'entrée du pipeline.
"""

from pathlib import Path

import duckdb
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = PROJECT_ROOT / "data" / "ventes.csv"
DB_PATH = PROJECT_ROOT / "ventes.duckdb"


def main() -> None:
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"Fichier CSV introuvable : {CSV_PATH}")

    df = pd.read_csv(CSV_PATH)

    with duckdb.connect(str(DB_PATH)) as con:
        con.execute("CREATE OR REPLACE TABLE ventes_raw AS SELECT * FROM df")

    print("✅ Ingestion terminée : table ventes_raw créée dans ventes.duckdb")
    print(f"Nombre de lignes chargées : {len(df)}")


if __name__ == "__main__":
    main()
