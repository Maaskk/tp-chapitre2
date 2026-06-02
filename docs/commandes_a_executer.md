# Commandes à exécuter sur ton PC

Ces commandes servent à générer les vrais résultats et les captures d’écran demandées par le professeur.

## 1. Ouvrir le dossier

```bash
cd tp_chapitre2_pipeline
```

## 2. Créer et activer l’environnement virtuel

Sur macOS / Linux :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Sur Windows PowerShell :

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3. Installer les dépendances

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Lancer l’ingestion

```bash
python pipeline/ingest.py
```

## 5. Lancer la validation

```bash
python pipeline/validate.py
```

## 6. Lancer dbt

```bash
cd dbt_pipeline
dbt debug --profiles-dir .
dbt run --profiles-dir .
dbt test --profiles-dir .
cd ..
```

## 7. Lancer Dagster

```bash
dagster dev -f pipeline/orchestrate.py
```

Après cette commande, Dagster affiche normalement un lien local du type :

```text
http://127.0.0.1:3000
```

Ouvre ce lien dans ton navigateur et lance le job `ventes_pipeline`.

## 8. Voir l’historique Git

```bash
git log --oneline --graph --all
```

## 9. Vérifier l’état Git

```bash
git status
```
