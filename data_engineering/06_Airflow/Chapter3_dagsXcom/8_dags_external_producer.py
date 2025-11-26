from airflow import DAG
from airflow.operators.empty import EmptyOperator
import pendulum

dag_a = DAG(
    dag_id="dag_a",
    start_date=pendulum.datetime(2025, 11, 21, tz="Asia/Seoul"),
)

task_a = EmptyOperator(
    task_id="task_a",
    dag=dag_a
)

