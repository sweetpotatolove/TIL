from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import pendulum

# XCom에 데이터 저장 (PythonOperator)
def push_xcom_value(**kwargs):
    kwargs['ti'].xcom_push(key='message', value='Hello from PythonOperator!')

# DAG 정의
with DAG(
    dag_id="python_bash_xcom_example",
    start_date=pendulum.datetime(2025, 11, 21, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    # PythonOperator를 사용하여 XCom에 값 저장
    push_task = PythonOperator(
        task_id="push_task",
        python_callable=push_xcom_value
    )

    # BashOperator에서 XCom 값을 가져와 출력
    pull_task = BashOperator(
        task_id="pull_task",
        bash_command="echo '{{ ti.xcom_pull(task_ids=\"push_task\", key=\"message\") }}'",
    )

    # DAG 실행 흐름
    push_task >> pull_task