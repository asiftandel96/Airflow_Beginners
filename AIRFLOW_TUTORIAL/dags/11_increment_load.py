from airflow.sdk import dag,task
from pendulum import datetime
from airflow.timetables.interval import CronDataIntervalTimetable

@dag(
    schedule=CronDataIntervalTimetable("@daily",timezone="UTC"),
    start_date = datetime(year=2026,month=8,day=26,tz="UTC"),
    end_date=datetime(year=2026,month=8,day=31,tz="UTC"),
    catchup=True
)

def increment_load_dag():

    @task.python
    def incremental_data_fetch(**kwargs):

        data_interval_start = kwargs['data_interval_start']
        data_interval_end = kwargs['data_interval_end']

        print(f"Fetching data from {data_interval_start} to {data_interval_end}")

    @task.bash
    def incremental_data_process():

        return "echo 'Processing incremental data from {{data_interval_start}} to {{data_interval_end}}'"

    ## Defining the task dependencies
    fetch_task = incremental_data_fetch()
    process_task = incremental_data_process()

    fetch_task >> process_task

## Initilaize the DAG
increment_load_dag()
        