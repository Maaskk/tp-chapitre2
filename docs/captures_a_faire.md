# Captures d’écran à faire pour le rendu

Le professeur demande des captures d’écran des commandes importantes. Fais ces captures sur ton PC après avoir exécuté les commandes.

## Captures recommandées

1. Capture de l’installation des dépendances :

```bash
pip install -r requirements.txt
```

2. Capture de l’ingestion réussie :

```bash
python pipeline/ingest.py
```

3. Capture de la validation réussie :

```bash
python pipeline/validate.py
```

4. Capture de dbt debug :

```bash
dbt debug --profiles-dir .
```

5. Capture de dbt run :

```bash
dbt run --profiles-dir .
```

6. Capture de dbt test :

```bash
dbt test --profiles-dir .
```

7. Capture de Dagster ouvert dans le navigateur avec le job `ventes_pipeline`.

8. Capture de l’historique Git :

```bash
git log --oneline --graph --all
```

9. Capture de la structure du projet dans VS Code ou dans le terminal :

```bash
tree -a -I '.venv|__pycache__|target|dbt_packages'
```

Si la commande `tree` n’existe pas sur ton Mac :

```bash
find . -maxdepth 3 -type f | sort
```
