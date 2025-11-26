from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# 데이터를 XCom에 푸시하는 함수
def push(ti):
    value = "This is a pushed value."
    ti.xcom_push(key='message', value=value)  # key와 value를 명시적으로 설정하여 XCom에 푸시

# XCom에서 데이터를 받는 함수
def pull(ti):
    message = ti.xcom_pull(task_ids='push_task', key='message')  # XCom에서 'message' 값을 pull
    print(f"Received message: {message}")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 11, 21),
}

with DAG('xcom_push_pull_example', default_args=default_args, schedule_interval=None) as dag:
    # XCom에 데이터를 푸시하는 태스크
    push_task = PythonOperator(
        task_id='push_task',
        python_callable=push,
        provide_context=True  # context를 제공하여 ti에 접근
    )

    # XCom에서 데이터를 받는 태스크
    pull_task = PythonOperator(
        task_id='pull_task',
        python_callable=pull,
        provide_context=True  # context를 제공하여 ti에 접근
    )

    # push_task가 먼저 실행된 후 pull_task가 실행됩니다.
    push_task >> pull_task
