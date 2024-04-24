from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python_operator import PythonOperator

default_args={
    'owner':'airflow',
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
    'start_date': datetime(2024, 4, 24),
}

dag=DAG(
    dag_id="my_first_task_with_apache_airflow",
    description="this is the project to orchestrat the workflows (python as code)",
    default_args=default_args,
    # schedule_interval=timedelta(days=1),                                          # (either) frequency-based schedule interval
    schedule_interval="@daily",                                                     # (or) Defining a daily schedule interval
    # start_date=datetime(year=2024, month=4, day=26)                                # (optional)                             
    # end_date=datetime(year=2019, month=1, day=5)                                  # (optional) 
)

def printHello():
    print("Hello World from apache paresh makwnaa")

hello_task = PythonOperator(
    task_id='hello_world_from_paresh',
    # description="this script resembles a hello from python operator from airflow ",
    python_callable=printHello,
    dag=dag,
)

hello_task
