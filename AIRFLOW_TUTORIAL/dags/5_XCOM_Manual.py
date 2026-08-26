from airflow.sdk import dag,task

@dag(dag_id="xcoms_dag_kwargs")

def xcom_dag_kwargs():

    @task.python
    def first_task(**kwargs):

        # Extract ti from kwargs to push XComs manually
        ti = kwargs['ti']

        print("Extracting the data.This is the first task")
        fetched_data = {"data":[1,2,3,4,5]}
        ti.xcom_push(key='return_result',value=fetched_data)
    
    @task.python
    def second_task(**kwargs):

        ti=kwargs['ti']

        ## Pulling XComs pushed by the first break
        fetched_data = ti.xcom_pull(task_ids='first_task',key='return_result')['data']
        print("Transformation Data.This is the second task")
        transformed_data=fetched_data * 2
        transformed_data_dict={'transf_data':transformed_data}
        ti.xcom_push(key='return_result',value=transformed_data_dict)

    @task.python
    def third_task(**kwargs):
        ti=kwargs['ti']

        ## Pulling XComs pushed by the second break
        load_data= ti.xcom_pull(task_ids='second_task',key='return_result')
        print("Loading Data.This is the third task")
        return load_data

    first=first_task()
    second = second_task()
    third = third_task()

    first >> second >> third

xcom_dag_kwargs()
