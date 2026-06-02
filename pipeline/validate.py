"""Étape 2 : validation minimale des données chargées dans DuckDB."""

from pathlib import Path

import duckdb

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "ventes.duckdb"

REQUIRED_COLUMNS = {"date", "produit", "categorie", "quantite", "prix_unitaire", "ville"}


def main() -> None:
    if not DB_PATH.exists():
        raise FileNotFoundError("Base DuckDB introuvable. Lancez d'abord : python pipeline/ingest.py")

    with duckdb.connect(str(DB_PATH)) as con:
        tables = {row[0] for row in con.execute("SHOW TABLES").fetchall()}
        if "ventes_raw" not in tables:
            raise ValueError("Table ventes_raw introuvable. Lancez d'abord l'étape d'ingestion.")

        columns = con.execute("DESCRIBE ventes_raw").fetchall()
        existing_columns = {col[0] for col in columns}
        missing = REQUIRED_COLUMNS - existing_columns

        if missing:
            raise ValueError(f"Colonnes manquantes : {missing}")

        null_count = con.execute(
            """
            SELECT COUNT(*)
            FROM ventes_raw
            WHERE produit IS NULL
               OR quantite IS NULL
               OR prix_unitaire IS NULL
            """
        ).fetchone()[0]

    if null_count > 0:
        raise ValueError(f"Données invalides : {null_count} lignes incomplètes")

    print("✅ Validation réussie : schéma et qualité minimale OK")


if __name__ == "__main__":
    main()
