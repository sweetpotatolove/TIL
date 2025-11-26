from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum

# XCom에 데이터 저장 (Push)
def push_xcom_value(**kwargs):
    kwargs['ti'].xcom_push(key='message', value='Hello from push_task')

# XCom에서 데이터 가져오기 (Pull)
def pull_xcom_value(**kwargs):
    message = kwargs['ti'].xcom_pull(task_ids='push_task', key='message')
    print("XCom에서 받은 값:", message)

# DAG 정의
with DAG(
    dag_id="xcom_example",
    start_date=pendulum.datetime(2025, 11, 21, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    # XCom에 값 저장
    push_task = PythonOperator(
        task_id="push_task",
        python_callable=push_xcom_value
    )

    # XCom에서 값 가져오기
    pull_task = PythonOperator(
        task_id="pull_task",
        python_callable=pull_xcom_value
    )

    # DAG 실행 흐름
    push_task >> pull_task
