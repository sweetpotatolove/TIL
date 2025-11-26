from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# PythonOperator에서 자동으로 XCom에 저장되는 return 값
def push():
    return "hello"  # 자동으로 XCom에 저장됨

def pull(ti):
    result = ti.xcom_pull(task_ids='push_task')  # XCom에서 pull
    print(f"Received message: {result}")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 11, 21),
}

with DAG('xcom_return_example', default_args=default_args, schedule_interval=None) as dag:
    # XCom에 값을 자동으로 푸시하는 태스크
    push_task = PythonOperator(
        task_id='push_task',
        python_callable=push,
    )

    # XCom에서 값을 가져오는 태스크
    pull_task = PythonOperator(
        task_id='pull_task',
        python_callable=pull,
        provide_context=True  # context를 제공하여 ti에 접근할 수 있도록
    )

    # 순서대로 실행
    push_task >> pull_task
