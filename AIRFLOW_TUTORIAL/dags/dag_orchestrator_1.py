from airflow.sdk import dag,task
import os

@dag(dag_id = "first_orchestrator_dag")

def first_orchestrator_dag():

    @task.python
    def first_task():
        print("This is first task")

    @task.python
    def second_task():
        print("This is second task")

    @task.python
    def third_task():

        # Ensure the directory exists.
        os.makedirs(os.path.dirname("/opt/airflow/logs"),exist_ok=True)


        with open("/opt/airflow/logs/output_1.txt","w") as f:
            f.write(f"Data Processed Successfully")

    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third

# Initialize the DAG
first_orchestrator_dag()
