# 🚀 Apache Airflow Tutorial

Un projet pratique et complet pour apprendre Apache Airflow, des concepts de base aux planifications avancées avec Cron, Delta, Branches et XComs.

Le projet utilise Docker pour l'environnement d'exécution et uv pour la gestion des dépendances Python.

## 📌 Description du projet

Ce dépôt est un laboratoire d'apprentissage contenant une collection de DAGs (Directed Acyclic Graphs) qui démontrent les fonctionnalités clés d'Apache Airflow.

Il sert de référence pratique pour comprendre l'orchestration de workflows avec Airflow.

### 🎯 Ce que vous allez apprendre

- La structure de base d'un DAG
- Le versioning des DAGs
- L'utilisation des opérateurs comme `PythonOperator` et `BashOperator`
- La communication entre tâches avec XComs
- Le passage de valeurs et de `kwargs`
- L'exécution de tâches en parallèle
- Le branchement conditionnel avec Branching
- Les différentes méthodes de planification
- Les presets de planification
- Les expressions Cron
- Les intervalles avec Delta

## 🛠️ Stack technique

- **Apache Airflow** — Orchestrateur de workflows
- **Docker & Docker Compose** — Environnement d'exécution
- **PostgreSQL** — Base de données Airflow
- **Redis** — Broker pour l'exécution distribuée
- **Python 3.x** — Langage de programmation
- **uv** — Gestionnaire de paquets et d'environnements Python
- **VS Code** — Environnement de développement recommandé

## 📂 Structure du projet

```text
AIRFLOW TUTORIAL/
├── config/                  # Fichiers de configuration Airflow
├── dags/                    # DAGs d'exemple
│   ├── 1_first_dag.py       # DAG de base
│   ├── 2_dag_versioning.py  # Versioning des DAGs
│   ├── 3_Operators.py       # Types d'opérateurs
│   ├── 4_XCORS_auto.py      # XComs automatiques
│   ├── 5_XCORS_kwargs.py    # XComs avec kwargs
│   ├── 6_parellel_tasks.py  # Tâches parallèles
│   ├── 7_branches.py        # Branchement conditionnel
│   ├── 8_schedule_preset.py # Planification avec presets
│   ├── 9_schedule_cron.py   # Planification avec Cron
│   └── 10_schedule_delta.py # Planification avec Delta
├── logs/                    # Logs d'exécution
├── plugins/                 # Plugins personnalisés
├── src/                     # Code source Python
├── .env                     # Variables d'environnement
├── .gitignore               # Fichiers ignorés par Git
├── docker-compose.yaml      # Configuration Docker Compose
├── pyproject.toml           # Dépendances Python
├── uv.lock                  # Versions verrouillées par uv
└── README.md                # Documentation du projet
```

## 🚀 Installation et démarrage

### Prérequis

Installez et démarrez :

- Docker Desktop
- Git
- uv, si vous souhaitez gérer l'environnement Python localement

### 1. Cloner le dépôt

```bash
git clone https://github.com/MDMAK04/airflow-tutorial.git
cd airflow-tutorial
```

### 2. Configurer les variables d'environnement

Si le dépôt contient un fichier `.env.example`, copiez-le :

```bash
cp .env.example .env
```

Sinon, créez votre propre fichier `.env` selon la configuration du projet.

Ne commitez jamais vos secrets ou variables sensibles dans Git.

### 3. Lancer Airflow avec Docker

```bash
docker compose up -d
```

Pour vérifier les conteneurs :

```bash
docker compose ps
```

Pour suivre les logs :

```bash
docker compose logs -f
```

### 4. Accéder à l'interface Airflow

Ouvrez :

http://localhost:8080

Les identifiants dépendent de la configuration du projet.

Dans une configuration Airflow classique, ils peuvent être :

```text
Username: airflow
Password: airflow
```

## 🧪 Utilisation des DAGs

Une fois l'interface Airflow ouverte :

1. Consultez la liste des DAGs.
2. Activez le DAG que vous souhaitez tester.
3. Déclenchez-le avec le bouton **Play**.
4. Ouvrez le DAG pour suivre l'exécution.
5. Sélectionnez une tâche pour consulter ses logs.
6. Utilisez la vue XCom pour observer les données échangées entre les tâches.

## 📚 Concepts étudiés

### DAG

Un DAG définit le workflow et les dépendances entre les tâches.

### Operators

Les Operators définissent le travail exécuté par une tâche.

Exemples :

```python
PythonOperator
BashOperator
```

### XCom

XCom permet à des tâches Airflow d'échanger de petites quantités de données.

Exemple :

```text
Task A → XCom → Task B
```

### Parallel Tasks

Plusieurs tâches indépendantes peuvent s'exécuter en parallèle.

```text
        ┌── Task A
Start ──┼── Task B
        └── Task C
```

### Branching

Le branching permet de choisir le chemin d'exécution selon une condition.

```text
             ┌── Task A
Condition ───┤
             └── Task B
```

### Scheduling

Airflow permet de planifier les DAGs avec différentes expressions et méthodes.

Exemples :

- Presets
- Cron
- Timedelta

## 🔐 Sécurité

Le fichier `.env` peut contenir des informations sensibles.

Assurez-vous qu'il est présent dans `.gitignore`.

Les logs locaux ne doivent pas être versionnés dans Git.

Avant chaque push :

```bash
git status
```

Vérifiez qu'aucun secret ou fichier sensible n'est inclus.

## 🔧 Commandes utiles

Démarrer les services :

```bash
docker compose up -d
```

Arrêter les services :

```bash
docker compose down
```

Voir les conteneurs :

```bash
docker compose ps
```

Voir les logs :

```bash
docker compose logs -f
```

Redémarrer les services :

```bash
docker compose restart
```

## 🎓 Objectif du projet

Ce projet a été créé pour construire une compréhension pratique d'Apache Airflow et de l'orchestration de workflows.

L'objectif est de passer progressivement de DAGs simples à des workflows utilisant :

- Operators
- XComs
- Parallelism
- Branching
- Scheduling
- Docker
- PostgreSQL
- Redis

## 🤝 Contribution

Ce projet est principalement destiné à l'apprentissage.

Vous pouvez :

- Forker le dépôt
- Ajouter de nouveaux DAGs
- Modifier les exemples
- Tester d'autres Operators
- Ajouter de nouveaux cas d'utilisation

## 📜 Licence

Ce projet est distribué sous licence MIT si le fichier `LICENSE` du dépôt l'indique.

---

Créé dans le cadre d'un apprentissage pratique d'Apache Airflow.

Repository:

https://github.com/MDMAK04/airflow-tutorial
