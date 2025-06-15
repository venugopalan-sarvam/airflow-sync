
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import sys
import os

with DAG(
    # Ensure this DAG ID is unique within your Airflow environment
    dag_id='testimportpandas_just_import_pandas',
    start_date=datetime(2023, 1, 1), # Consider setting this to a date in the past
    schedule_interval='0 * * * *',
    catchup=False,
    tags=['user_upload', 'dynamic'],
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    }
) as dag:
    hello_task = BashOperator(
        task_id='run_uploaded_script_just_import_pandas',
        bash_command='python /opt/airflow/git/airflow-sync.git/dags/hellocall/just_import_pandas.py'
    )

    hello_task
