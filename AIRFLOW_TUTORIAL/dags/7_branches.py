from airflow.sdk import dag,task

@dag(dag_id="branches_dag")


def branches_dag():

    @task.python
    def extract_task(**kwargs):

        print("Extracting the data")

        ti = kwargs['ti']
        extracted_data_dict= {"api_extracted_data":[1,2,3],
                             "db_extracted_data":[4,5,6],
                             "s3_extracted_data":[7,8,9],
                             "weekend_flag":"False"}
    
        ti.xcom_push(key='return_result',value=extracted_data_dict)

    @task.python
    def transform_task_api(**kwargs):

        ti = kwargs['ti']

        api_extracted_data = ti.xcom_pull(task_ids='extract_task',key='return_result')['api_extracted_data']
        print(f"Transforming the data:{api_extracted_data}")

        transformed_api_data = [i*100 for i in api_extracted_data]
        ti.xcom_push(key='return_result',value=transformed_api_data)

    @task.python
    def transform_task_db(**kwargs):
        
        ti = kwargs['ti']

        db_extracted_data = ti.xcom_pull(task_ids='extract_task',key='return_result')['db_extracted_data']
        print(f"Transforming the data:{db_extracted_data}")

        transformed_db_data = [i*100 for i in db_extracted_data]
        ti.xcom_push(key='return_result',value=transformed_db_data)

    @task.python
    def transform_task_s3(**kwargs):
        
        ti = kwargs['ti']

        s3_extracted_data = ti.xcom_pull(task_ids='extract_task',key='return_result')['s3_extracted_data']
        print(f"Transforming the data:{s3_extracted_data}")

        transformed_s3_data = [i*100 for i in s3_extracted_data]
        ti.xcom_push(key='return_result',value=transformed_s3_data)

    @task.branch
    def decider_task(**kwargs):
        
        ti = kwargs['ti']
        weekend_flag = ti.xcom_pull(task_ids='extract_task',key='return_result')['weekend_flag']

        if weekend_flag == "True":
            return "no_load_task"
        else:
            return "load_task"
    
    @task.bash
    def load_task(**kwargs):

        print("Loading data to destination")
        api_data = kwargs['ti'].xcom_pull(task_ids='extract_task',key='return_result')['api_extracted_data']
        db_data = kwargs['ti'].xcom_pull(task_ids='transform_task_db',key='return_result')
        s3_data = kwargs['ti'].xcom_pull(task_ids='transform_task_s3',key='return_result')

        return f"echo Loaded Data: {api_data} {db_data} {s3_data}"

    @task.bash
    def no_load_task():
        print("No data to load as it is weekend")
        return "echo No data to load as it is weekend"

    first = extract_task()
    second_api = transform_task_api()
    second_db = transform_task_db()
    third_db = transform_task_s3()
    decider = decider_task()
    load = load_task()
    no_load = no_load_task()

    first >> (second_api, second_db, third_db) >> decider >> [load, no_load]

branches_dag()