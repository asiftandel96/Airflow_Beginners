# Airflow Beginners

A hands-on Apache Airflow learning project covering DAGs, operators, XComs, and parallel task execution. It runs locally with Docker Compose.

## Topics

- Basic DAGs and task dependencies
- DAG versioning and operators
- Automatic and manual XCom usage
- Parallel task execution

## Prerequisites

- Docker Desktop or Docker Engine with the Compose plugin
- At least 4 GB of memory available to Docker
- Git, if cloning the repository

## Quick Start

```bash
git clone https://github.com/asiftandel96/Airflow_Beginners.git
cd Airflow_Beginners
docker compose up -d
```

Open [http://localhost:8080](http://localhost:8080).

Default credentials:

```text
Username: airflow
Password: airflow
```

New DAGs are paused by default. Unpause one in the UI or run:

```bash
docker compose exec airflow-scheduler airflow dags unpause parallel_tasks_dag
```

## Example DAGs

The examples are in `AIRFLOW_TUTORIAL/dags/` and are mounted into containers as `/opt/airflow/dags`.

| File | DAG | Topic |
| --- | --- | --- |
| `1_dag.py` | `my_first_dag` | Basic DAG and dependencies |
| `2_dag_versioning.py` | `versioned_dag` | DAG versioning |
| `3_operators.py` | `operator_dag` | Airflow operators |
| `4_XCOMS_Auto.py` | `xcoms_dag_auto` | Automatic XComs |
| `5_XCOM_Manual.py` | `xcoms_dag_kwargs` | Manual XComs |
| `6_parallel_tasks.py` | `parallel_tasks_dag` | Parallel transforms and loading |

## Useful Commands

```bash
# Check services
docker compose ps

# Follow scheduler or parser logs
docker compose logs -f airflow-scheduler
docker compose logs -f airflow-dag-processor

# List discovered DAGs
docker compose exec airflow-scheduler airflow dags list

# Trigger the parallel example
docker compose exec airflow-scheduler airflow dags trigger parallel_tasks_dag

# Stop services
docker compose down
```

To remove the local PostgreSQL metadata volume and start fresh:

```bash
docker compose down -v
```

## Project Layout

```text
AIRFLOW_TUTORIAL/dags/  Example DAG definitions
config/                  Local Airflow configuration output
logs/                    Local task and parser logs
docker-compose.yaml      Airflow services and volume configuration
.env                     Local environment variables
```

Runtime output in `logs/`, `config/`, and Python cache directories is ignored by Git. Never commit passwords, tokens, or private Fernet keys.

## Development Checks

```bash
python -m compileall -q AIRFLOW_TUTORIAL/dags
docker compose config --quiet
```

## License

This project uses Apache Airflow, licensed under the Apache License 2.0.