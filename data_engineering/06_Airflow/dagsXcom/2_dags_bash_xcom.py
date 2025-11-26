from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum

# DAG 정의
with DAG(
    dag_id="bash_xcom_example",
    start_date=pendulum.datetime(2025, 11, 21, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    # XCom에 값 저장 (Push)
    push_task = BashOperator(
        task_id="push_task",
        bash_command="echo 'Hello from BashOperator!'",
        do_xcom_push=True  # XCom에 출력값 저장
    )

    # XCom에서 값 가져오기 (Pull)
    pull_task = BashOperator(
        task_id="pull_task",
        bash_command="echo '{{ ti.xcom_pull(task_ids=\"push_task\") }}'",
    )

    # DAG 실행 흐름
    push_task >> pull_task