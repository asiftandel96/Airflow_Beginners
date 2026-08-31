from asset_13 import fetch_data
from airflow.sdk import dag, task, asset
from pendulum import datetime
import os

@asset(
    schedule = fetch_data,
    uri="/opt/airflow/logs/process_data.txt",
    name = "process_data"
    )

def process_data(self):

    ## Ensure that the directory exists

    os.makedirs(os.path.dirname(self.uri), exist_ok=True)

    ## Simulate data fetching by writing to a file

    with open(self.uri, "w") as f:

        f.write(f"Data processed successfully")

    print(f"Data processed Successfully")