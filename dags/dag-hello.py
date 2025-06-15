from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

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
        bash_command='python /opt/airflow/git/airflow-sync.git/dags/hellocall/hello.py'
    )

    hello_task
