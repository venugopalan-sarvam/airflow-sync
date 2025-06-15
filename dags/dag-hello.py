from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from hellocall.hello import hello

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

with DAG(
    'dags-greeting',
    default_args=default_args,
    description='A simple greeting DAG',
    schedule_interval=None,
    catchup=False
) as dag:

    hello_task = BashOperator(
        task_id='hello_world_task',
        bash_command=f'echo {hello("Venu")}'
    )

    hello_task
