from airflow.sdk import dag,task
from pendulum import datetime

@dag(dag_id="schedule_preset_dag",start_date=datetime(year=2026,month=8,day=27,tz="UTC"),schedule="@daily",is_paused_upon_creation=False)


def schedule_preset_dag():

    @task.python
    def first_task():
        print("This is the first task")
    @task.python
    def second_task():
        print("This is the second task")

    @task.python
    def third_task():
        print("This is the third task")

    ## Definining the task dependencies

    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third

## Initialize the DAG
schedule_preset_dag()