from airflow.sdk import dag,task
from airflow.operators.bash import BashOperator
@dag(dag_id="operator_dag")

def operator_dag():

    @task.python
    def first_task():
        print("This is the first task")
    @task.python
    def second_task():
        print("This is the second task")

    @task.bash
    def run_after_loop() -> str:
        return "echo https://airflow.apache.org/"

    @task.python
    def third_task():
        print("This is the third task")
    ## Definining the task dependencies

    first = first_task()
    second = second_task()
    run_after_loop = run_after_loop()
    third = third_task()

    first >> second >> run_after_loop >> third

## Initialize the DAG
operator_dag()