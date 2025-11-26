from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
import pendulum

# DAG 정의
with DAG(
    dag_id="basic_dag_example",
    start_date=pendulum.datetime(2025, 11, 22, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    # 시작 Task (EmptyOperator)
    start = EmptyOperator(
        task_id="start"
    )

    # BashOperator 실행 Task 1
    task_1 = BashOperator(
        task_id="task_1",
        bash_command="echo 'Task 1 실행'"
    )

    # BashOperator 실행 Task 2
    task_2 = BashOperator(
        task_id="task_2",
        bash_command="echo 'Task 2 실행'"
    )

    # 종료 Task (EmptyOperator)
    end = EmptyOperator(
        task_id="end"
    )

    # DAG 연결 설정
    start >> task_1 >> task_2 >> end