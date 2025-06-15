from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def list_files_and_folders():
    root_dir = '/opt/airflow/git/airflow-sync.git/dags'
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(f"Directory: {dirpath}")
        if dirnames:
            print(f"  Subdirectories: {dirnames}")
        if filenames:
            print(f"  Files: {filenames}")
        print("----")

with DAG(
    'list_airflow_dags_folder',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['debug']
) as dag:
    list_files_task = PythonOperator(
        task_id='list_files_and_folders_task',
        python_callable=list_files_and_folders
    )
