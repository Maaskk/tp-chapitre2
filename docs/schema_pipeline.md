# Schéma simple du pipeline

```mermaid
flowchart LR
    A[CSV local<br/>data/ventes.csv] --> B[Ingestion<br/>pipeline/ingest.py]
    B --> C[Stockage local<br/>DuckDB: ventes_raw]
    C --> D[Validation<br/>pipeline/validate.py]
    D --> E[Transformation dbt<br/>ventes_clean.sql]
    E --> F[Agrégation dbt<br/>ventes_resume.sql]
    F --> G[Tests dbt<br/>schema.yml]
    G --> H[Orchestration<br/>Dagster]
    H --> I[CI<br/>GitHub Actions]
```

## Lecture simple du schéma

1. Le fichier `data/ventes.csv` est la donnée de départ.
2. `pipeline/ingest.py` charge le CSV dans DuckDB.
3. La table `ventes_raw` contient les données brutes.
4. `pipeline/validate.py` contrôle les colonnes et les valeurs nulles.
5. dbt crée une table nettoyée `ventes_clean`.
6. dbt crée une table résumée `ventes_resume`.
7. `dbt test` vérifie des contraintes simples comme `not_null`.
8. Dagster organise l’ordre d’exécution.
9. GitHub Actions automatise des vérifications simples.
