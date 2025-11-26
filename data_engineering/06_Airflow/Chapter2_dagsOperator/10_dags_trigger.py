from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
import pendulum

# DAG 정의
with DAG(
    dag_id="trigger_rule_example",
    start_date=pendulum.datetime(2025, 11, 22, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    # 시작 Task
    start = EmptyOperator(task_id="start")

    # 정상 실행되는 Task
    task_1 = BashOperator(
        task_id="task_1",
        bash_command="echo 'Task 1 실행'"
    )

    # 강제로 실패시키는 Task
    task_2 = BashOperator(
        task_id="task_2",
        bash_command="exit 1",  # 강제 실패
    )

    # Trigger Rule: 모든 Upstream Task가 성공해야 실행됨 (실패한 Task가 있으므로 실행되지 않음)
    task_3 = BashOperator(
        task_id="task_3",
        bash_command="echo 'Task 3 실행'",
        trigger_rule="all_success"
    )

    # Trigger Rule: 최소 1개 Task가 실패하면 실행됨 (task_2가 실패했으므로 실행됨)
    task_4 = BashOperator(
        task_id="task_4",
        bash_command="echo 'Task 4 실행 (one_failed)'",
        trigger_rule="one_failed"
    )

    # Trigger Rule: 모든 Upstream Task가 끝나면 실행됨 (성공, 실패 여부 관계없이 실행됨)
    task_5 = BashOperator(
        task_id="task_5",
        bash_command="echo 'Task 5 실행 (all_done)'",
        trigger_rule="all_done"
    )

    # 종료 Task
    end = EmptyOperator(task_id="end")

    # DAG 실행 흐름 설정
    start >> [task_1, task_2]  # task_1, task_2 병렬 실행
    [task_1, task_2] >> task_3  # 모든 Task 성공 시 실행 (실행되지 않음)
    [task_1, task_2] >> task_4  # 최소 1개 실패 시 실행 (실행됨)
    [task_1, task_2] >> task_5  # 모든 Task 완료 후 실행 (실행됨)
    [task_3, task_4, task_5] >> end  # 모든 Task 종료 후 end 실행
