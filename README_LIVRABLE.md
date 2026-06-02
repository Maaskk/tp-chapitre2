# TP Chapitre 2 — Pipelines agiles, versionnement et orchestration

## Objectif

Ce projet construit un mini pipeline DataOps/MLOps local à partir d’un fichier CSV de ventes.

Pipeline :

```text
CSV local -> ingestion -> DuckDB -> validation -> dbt -> dbt test -> Dagster -> CI
```

## Structure du projet

```text
tp_chapitre2_pipeline/
├── data/
│   └── ventes.csv
├── pipeline/
│   ├── ingest.py
│   ├── validate.py
│   └── orchestrate.py
├── dbt_pipeline/
│   ├── dbt_project.yml
│   ├── profiles.yml
│   └── models/
│       ├── ventes_clean.sql
│       ├── ventes_resume.sql
│       └── schema.yml
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── reponses_questions.md
│   ├── schema_pipeline.md
│   ├── commandes_a_executer.md
│   └── captures_a_faire.md
├── expected_outputs/
│   └── ventes_resume_expected.csv
├── requirements.txt
├── .gitignore
└── README_LIVRABLE.md
```

## Commandes principales

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python pipeline/ingest.py
python pipeline/validate.py
cd dbt_pipeline
dbt debug --profiles-dir .
dbt run --profiles-dir .
dbt test --profiles-dir .
cd ..
dagster dev -f pipeline/orchestrate.py
```

## Livrables inclus dans ce dossier

- Dossier du projet.
- Scripts Python du pipeline.
- Modèles dbt.
- Fichier CI GitHub Actions.
- Schéma simple du pipeline.
- Réponses aux questions.
- Fichier de commandes à exécuter.
- Liste des captures d’écran à faire.
- Historique Git local inclus dans le dossier si le dossier est ouvert avec Git.

## À ajouter avant dépôt final

Les captures d’écran doivent être faites sur ton PC après exécution réelle des commandes.
