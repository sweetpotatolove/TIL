from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator

def print_hello():
    return "Hello, Airflow!"

with DAG(
    dag_id="dags_python_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2025, 11, 22, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
) as dag:
    python_task = PythonOperator(
        task_id='print_hello_task',
        python_callable=print_hello
    )
