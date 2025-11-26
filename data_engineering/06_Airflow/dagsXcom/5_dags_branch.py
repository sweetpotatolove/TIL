from airflow import DAG
from airflow.operators.python import BranchPythonOperator
from airflow.operators.bash import BashOperator
import pendulum

# 분기 조건 함수
def choose_branch(**kwargs):
    value = "A"  # 실행 조건 변경 가능
    return "task_A" if value == "A" else "task_B"

# DAG 정의
with DAG(
    dag_id="simple_branch_operator_example",
    start_date=pendulum.datetime(2025, 11, 21, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    # 조건 기반 분기 Task
    branch_task = BranchPythonOperator(
        task_id="branching",
        python_callable=choose_branch
    )

    # 선택될 Task A
    task_A = BashOperator(
        task_id="task_A",
        bash_command="echo 'Task A 실행'"
    )

    # 선택될 Task B
    task_B = BashOperator(
        task_id="task_B",
        bash_command="echo 'Task B 실행'"
    )

    # 공통 종료 Task (Trigger Rule 적용)
    end_task = BashOperator(
        task_id="end_task",
        bash_command="echo '모든 분기 완료'",
        trigger_rule="none_failed_or_skipped"
    )

    # DAG 실행 흐름
    branch_task >> [task_A, task_B]  # 하나만 실행됨
    [task_A, task_B] >> end_task  # 종료 Task는 항상 실행됨