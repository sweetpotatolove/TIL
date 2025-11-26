from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
import pendulum

# DAG 정의
with DAG(
    dag_id="nested_taskgroup_example",
    start_date=pendulum.datetime(2025, 11, 21, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    # 시작 Task
    start = EmptyOperator(task_id="start")

    # TaskGroup 정의 (group_1)
    with TaskGroup("group_1") as group_1:
        
        # 첫 번째 Task
        task_1 = BashOperator(
            task_id="task_1",
            bash_command="echo 'Task 1 실행'"
        )

        # 내부 TaskGroup 정의 (inner_group_1)
        with TaskGroup("inner_group_1") as inner_group_1:
            inner_task = BashOperator(
                task_id="inner_task",
                bash_command="echo 'Inner Group 실행'"
            )

        # 병렬 실행될 Task
        task_2 = BashOperator(
            task_id="task_2",
            bash_command="echo 'Task 2 실행'"
        )

        task_3 = BashOperator(
            task_id="task_3",
            bash_command="echo 'Task 3 실행'"
        )

        # 마지막 Task (task_2, task_3 완료 후 실행)
        task_4 = BashOperator(
            task_id="task_4",
            bash_command="echo 'Task 4 실행'"
        )

        # DAG 내 실행 순서 설정
        task_1 >> inner_group_1 >> [task_2, task_3] >> task_4

    # 종료 Task
    end = EmptyOperator(task_id="end")

    # DAG 실행 흐름 설정
    start >> group_1 >> end
