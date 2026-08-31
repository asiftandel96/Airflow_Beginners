from airflow.sdk import dag,task,asset
from pendulum import datetime
import os

@asset(
    schedule="@daily",

    uri = "/opt/airflow/logs/fetch_data.txt",
    name = "fetch_data"
)
def fetch_data(self):

    ## Ensure that the directory exists

    os.makedirs(os.path.dirname(self.uri), exist_ok=True)

    ## Simulate data fetching by writing to a file

    with open(self.uri, "w") as f:

        f.write(f"Data fetched successfully")

    print(f"Data written Successfully")
