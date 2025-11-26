from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
import pendulum

with DAG(
    dag_id="empty_operator_example",
    start_date=pendulum.datetime(2025, 11, 22, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    start = EmptyOperator(
        task_id="start"
    )
    task_1 = BashOperator(
        task_id="task_1",
        bash_command="echo 'Task 1 실행'"
    )
    task_2 = BashOperator(
        task_id="task_2",
        bash_command="echo 'Task 2 실행'"
    )
    end = EmptyOperator(
        task_id="end"
    )
    # DAG 흐름 설정
    start >> [task_1, task_2] >> end

    