from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

def print_sys_path():
    print("PYTHONPATH:", sys.path)

with DAG(
    'print_python_path',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False
) as dag:
    t1 = PythonOperator(
        task_id='print_path',
        python_callable=print_sys_path
    )