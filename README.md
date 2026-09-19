# 🚀 Apache Airflow Tutorial

A practical project for learning Apache Airflow, from basic concepts to advanced scheduling with Cron, Delta, Branching, and XComs.

This project uses Docker for the runtime environment and `uv` for Python dependency management.

## 📌 Project Description

This repository is a hands-on learning laboratory containing a collection of DAGs (Directed Acyclic Graphs) that demonstrate key Apache Airflow features.

It is designed as a practical reference for understanding workflow orchestration with Airflow.

### 🎯 What You Will Learn

- The structure of a DAG
- DAG versioning
- Using Operators such as `PythonOperator` and `BashOperator`
- Communication between tasks using XComs
- Passing values and `kwargs`
- Running tasks in parallel
- Conditional branching
- Different scheduling methods
- Schedule presets
- Cron expressions
- Timedelta scheduling

## 🛠️ Tech Stack

- **Apache Airflow** — Workflow orchestration
- **Docker & Docker Compose** — Containerized environment
- **PostgreSQL** — Airflow database
- **Redis** — Message broker for distributed task execution
- **Python 3.x** — Programming language
- **uv** — Python package and environment manager
- **VS Code** — Recommended development environment

## 📂 Project Structure

```text
AIRFLOW TUTORIAL/
├── config/                  # Airflow configuration files
├── dags/                    # Example DAGs
│   ├── 1_first_dag.py       # Basic DAG
│   ├── 2_dag_versioning.py  # DAG versioning
│   ├── 3_Operators.py       # Different Operators
│   ├── 4_XCORS_auto.py      # Automatic XComs
│   ├── 5_XCORS_kwargs.py    # XComs with kwargs
│   ├── 6_parellel_tasks.py  # Parallel tasks
│   ├── 7_branches.py        # Conditional branching
│   ├── 8_schedule_preset.py # Schedule presets
│   ├── 9_schedule_cron.py   # Cron scheduling
│   └── 10_schedule_delta.py # Delta scheduling
├── logs/                    # Execution logs
├── plugins/                 # Custom plugins
├── src/                     # Python source code
├── .env                     # Environment variables
├── .gitignore               # Git ignore rules
├── docker-compose.yaml      # Docker Compose configuration
├── pyproject.toml           # Python dependencies
├── uv.lock                  # Locked uv dependencies
└── README.md                # Project documentation
```

## 🚀 Installation and Setup

### Prerequisites

Install and start:

- Docker Desktop
- Git
- uv, if you want to manage the Python environment locally

### 1. Clone the repository

```bash
git clone https://github.com/MDMAK04/airflow-tutorial.git
cd airflow-tutorial
```

### 2. Configure environment variables

If the repository contains a `.env.example` file, copy it:

```bash
cp .env.example .env
```

Otherwise, create a `.env` file according to the project configuration.

Never commit secrets or sensitive environment variables to Git.

### 3. Start Airflow with Docker

```bash
docker compose up -d
```

Check the running containers:

```bash
docker compose ps
```

Follow the logs:

```bash
docker compose logs -f
```

### 4. Access the Airflow UI

Open:

http://localhost:8080

The credentials depend on the project configuration.

For a standard Airflow configuration, they may be:

```text
Username: airflow
Password: airflow
```

## 🧪 Working with the DAGs

Once the Airflow UI is open:

1. View the list of DAGs.
2. Enable the DAG you want to test.
3. Trigger it using the **Play** button.
4. Open the DAG to monitor its execution.
5. Select a task to inspect its logs.
6. Use the XCom view to inspect data exchanged between tasks.

## 📚 Concepts Covered

### DAG

A DAG defines a workflow and the dependencies between its tasks.

### Operators

Operators define the work executed by a task.

Examples:

```python
PythonOperator
BashOperator
```

### XCom

XCom allows Airflow tasks to exchange small amounts of data.

Example:

```text
Task A → XCom → Task B
```

### Parallel Tasks

Independent tasks can run in parallel.

```text
        ┌── Task A
Start ──┼── Task B
        └── Task C
```

### Branching

Branching allows a workflow to choose an execution path based on a condition.

```text
             ┌── Task A
Condition ───┤
             └── Task B
```

### Scheduling

Airflow provides different ways to schedule DAGs.

This project covers:

- Presets
- Cron
- Timedelta

## 🔐 Security

The `.env` file may contain sensitive information.

Make sure it is included in `.gitignore`.

Local logs should not be committed to Git.

Before pushing changes:

```bash
git status
```

Check that no secrets or sensitive files are included.

## 🔧 Useful Commands

Start the services:

```bash
docker compose up -d
```

Stop the services:

```bash
docker compose down
```

Check running containers:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f
```

Restart the services:

```bash
docker compose restart
```

## 🎓 Project Goal

This project was created to build a practical understanding of Apache Airflow and workflow orchestration.

The goal is to progress from simple DAGs to workflows using:

- Operators
- XComs
- Parallelism
- Branching
- Scheduling
- Docker
- PostgreSQL
- Redis

## 🤝 Contribution

This project is mainly intended for learning.

You can:

- Fork the repository
- Add new DAGs
- Modify the examples
- Experiment with other Operators
- Add new workflow use cases

## 📜 License

This project is distributed under the MIT License if the repository contains a `LICENSE` file.

---

Created as part of a practical Apache Airflow learning project.

Repository:

https://github.com/MDMAK04/airflow-tutorial
