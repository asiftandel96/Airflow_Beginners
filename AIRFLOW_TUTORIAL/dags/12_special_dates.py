from airflow.sdk import dag,task
from pendulum import datetime
from airflow.timetables.events import EventsTimetable

special_dates = EventsTimetable(
    event_dates = [
        datetime(2026,8,1),
        datetime(2026,8,15),
        datetime(2026,8,30)
    ]
)

@dag(
schedule = special_dates,
start_date = datetime(year=2026,month=8,day=1,tz="UTC"),
end_date=datetime(year=2026,month=8,day=31,tz="UTC"),
    catchup=True
)

def special_dates_dag():

    @task.python

    def special_event_task(**kwargs):

        execution_date = kwargs['logical_date']

        print(f"Running Tasks for special events on {execution_date}")


        special_task = special_event_task()

special_dates_dag()