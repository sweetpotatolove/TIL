from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
import pendulum

# DAG 정의
with DAG(
    dag_id="multi_task_dependency_example",
    start_date=pendulum.datetime(2025, 11, 22, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    # 시작 Task
    start = EmptyOperator(task_id="start")

    # 병렬 실행 Task
    task_1 = BashOperator(
        task_id="task_1",
        bash_command="echo 'Task 1 실행'"
    )

    task_2 = BashOperator(
        task_id="task_2",
        bash_command="echo 'Task 2 실행'"
    )

    # 종속 Task (task_1, task_2가 완료되어야 실행됨)
    task_3 = BashOperator(
        task_id="task_3",
        bash_command="echo 'Task 3 실행 - Task 1, Task 2 완료 후 실행'"
    )

    # 종속 Task (task_3 완료 후 실행됨)
    task_4 = BashOperator(
        task_id="task_4",
        bash_command="echo 'Task 4 실행'"
    )

    task_5 = BashOperator(
        task_id="task_5",
        bash_command="echo 'Task 5 실행'"
    )

    # 종료 Task
    end = EmptyOperator(task_id="end")

    # DAG 실행 순서 (다중 종속 관계 설정)
    start >> [task_1, task_2]  # start 이후 task_1, task_2 병렬 실행
    [task_1, task_2] >> task_3  # task_1과 task_2가 완료되어야 task_3 실행
    task_3 >> [task_4, task_5]  # task_3이 완료된 후 task_4, task_5 병렬 실행
    [task_4, task_5] >> end  # task_4, task_5가 완료된 후 end Task 실행
