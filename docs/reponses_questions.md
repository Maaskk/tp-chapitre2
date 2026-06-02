# Réponses aux questions du TP — Chapitre 2

## 1. En quoi ce pipeline est-il plus structuré qu’un notebook unique ?

Ce pipeline est plus structuré qu’un notebook unique parce que chaque étape est séparée dans un fichier ou un outil précis : l’ingestion est dans `ingest.py`, la validation dans `validate.py`, la transformation dans dbt, les tests dans `schema.yml`, et l’orchestration dans Dagster.  
Dans un notebook, tout est souvent mélangé dans une seule page : lecture des données, nettoyage, calculs, tests et résultats. Ici, le projet est plus propre, plus lisible, plus maintenable et plus facile à faire évoluer.

## 2. Quel est le rôle de Git dans ce projet ?

Git sert à versionner le projet. Il permet de garder l’historique des modifications, de faire des commits à chaque étape importante, de revenir en arrière en cas d’erreur et de montrer l’évolution du pipeline. Dans ce TP, Git est important car il prouve que le pipeline a été construit progressivement.

## 3. Quel est le rôle de requirements.txt ?

Le fichier `requirements.txt` contient la liste des bibliothèques Python nécessaires au projet, par exemple `pandas`, `duckdb`, `dbt-core`, `dbt-duckdb`, `dagster` et `dlt`.  
Son rôle est de rendre l’environnement reproductible : une autre personne peut installer les mêmes dépendances avec la commande :

```bash
pip install -r requirements.txt
```

## 4. Pourquoi ajouter une étape validate.py ?

L’étape `validate.py` sert à vérifier la qualité minimale des données avant de continuer le pipeline. Elle contrôle par exemple que les colonnes obligatoires existent et que certaines valeurs importantes ne sont pas nulles.  
C’est important parce qu’un pipeline ne doit pas transformer des données incorrectes sans contrôle.

## 5. Quel est le rôle de dbt test ?

`dbt test` permet d’exécuter des tests automatiques sur les modèles dbt. Dans ce TP, il vérifie par exemple que certaines colonnes ne contiennent pas de valeurs nulles grâce au test `not_null`.  
Son rôle est d’ajouter un contrôle qualité automatique après la transformation des données.

## 6. Qu’apporte Dagster par rapport à une exécution manuelle ?

Dagster apporte une orchestration. Au lieu de lancer les commandes une par une à la main, Dagster organise l’ordre d’exécution : ingestion, validation, transformation, puis tests.  
Cela rend le pipeline plus professionnel, plus clair, plus contrôlable et plus proche d’un vrai pipeline DataOps/MLOps.

## 7. Qu’apporte la CI ?

La CI, ici avec GitHub Actions, permet d’automatiser des vérifications à chaque changement envoyé sur GitHub. Par exemple, elle peut installer les dépendances et vérifier que les fichiers Python n’ont pas d’erreurs de syntaxe.  
Cela évite d’intégrer du code cassé dans le projet.

## 8. Que manque-t-il encore pour un pipeline pleinement industrialisé ?

Pour avoir un pipeline pleinement industrialisé, il manquerait encore plusieurs éléments :

- une vraie source de données externe ou une base de données distante ;
- plus de tests de qualité des données ;
- une gestion des erreurs plus complète ;
- des logs détaillés ;
- un monitoring du pipeline ;
- un déploiement automatique ;
- une gestion des secrets et des variables d’environnement ;
- une documentation technique complète ;
- éventuellement un environnement cloud ou Docker.

Donc ce TP représente une première version locale et pédagogique d’un pipeline structuré, mais pas encore une version totalement industrialisée.
