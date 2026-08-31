from dag_orchestrator_1 import first_orchestrator_dag
from dag_orchestrator_2 import second_orchestrator_dag
from airflow.sdk import dag,task
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

@dag

def dag_orchestrator_parent():

    trigger_first_dag = TriggerDagRunOperator(
        task_id = 'trigger_first_orchestrator_dag',
        trigger_dag_id = 'first_orchestrator_dag',
        wait_for_completion = True # Optional (This is slow): Waits for the triggered DAG to complete
    )

    trigger_second_dag = TriggerDagRunOperator(
        task_id = 'trigger_second_orchestrator_dag',
        trigger_dag_id = 'second_orchestrator_dag',
        wait_for_completion = True # Optional (This is slow): Waits for the Triggered DAG to complete
    )

    trigger_first_dag >> trigger_second_dag

# Initialize the DAG
dag_orchestrator_parent()
