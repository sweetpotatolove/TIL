from airflow import DAG
from airflow.operators.empty import EmptyOperator  # Airflow 2.x 기준
from airflow.operators.bash import BashOperator
import pendulum

# DAG 정의
with DAG(
    dag_id="parallel_task_example",
    start_date=pendulum.datetime(2025, 11, 22, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    # 시작 Task
    start = EmptyOperator(
        task_id="start"
    )

    # 병렬로 실행될 Task들
    task_1 = BashOperator(
        task_id="task_1",
        bash_command="echo 'Task 1 실행'"
    )

    task_2 = BashOperator(
        task_id="task_2",
        bash_command="echo 'Task 2 실행'"
    )

    task_3 = BashOperator(
        task_id="task_3",
        bash_command="echo 'Task 3 실행'"
    )

    # 종료 Task
    end = EmptyOperator(
        task_id="end"
    )

    # DAG 연결 설정 (start → 병렬 실행 → end)
    start >> [task_1, task_2, task_3] >> end
