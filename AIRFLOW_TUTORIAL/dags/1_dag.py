from airflow.sdk import dag,task

@dag(dag_id="my_first_dag")

def first_dag():

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
first_dag()