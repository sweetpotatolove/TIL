from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

# 데이터를 XCom에 푸시하는 PythonOperator
def push(ti):
    value = "This is a pushed value."
    ti.xcom_push(key='message', value=value)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 11, 21),
}

with DAG('xcom_jinja_example', default_args=default_args, schedule_interval=None) as dag:
    # XCom에 데이터를 푸시하는 PythonOperator
    push_task = PythonOperator(
        task_id='push_task',
        python_callable=push,
        provide_context=True
    )

    # BashOperator에서 Jinja 템플릿을 사용해 XCom 값 참조
    bash_task = BashOperator(
        task_id='bash_task',
        bash_command="echo '{{ ti.xcom_pull(task_ids=\"push_task\", key=\"message\") }}'",
    )

    # push_task가 먼저 실행된 후 bash_task가 실행됩니다.
    push_task >> bash_task
