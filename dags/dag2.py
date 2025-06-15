from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

# Instantiate the DAG object
with DAG(
    'dags-hello-venu.py',
    default_args=default_args,
    description='A simple Hello World DAG',
    schedule_interval=None,
    catchup=False
) as dag:

    # Define the tasks
    hello_task = BashOperator(
        task_id='hello_world_task',
        bash_command='echo "Hello, Venugopalan!"'
    )

    # Set the task dependencies
    hello_task