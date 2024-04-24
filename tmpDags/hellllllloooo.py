from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 23),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the function that will be executed as the task
def print_hello():
    print("Hello, World!")

# Define the DAG
dag = DAG(
    'hello_worldclassswjrdjefbnfbbef',
    default_args=default_args,
    description='A simple DAG that prints Hello, World!',
    schedule_interval=timedelta(days=1),  # Runs once a day
)

# Define the task
hello_task = PythonOperator(
    task_id='print_helloworlldldslls',
    python_callable=print_hello,
    dag=dag,
)

# Define the task dependencies
hello_task
