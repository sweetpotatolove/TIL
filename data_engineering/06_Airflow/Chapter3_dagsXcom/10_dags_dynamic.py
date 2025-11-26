from airflow import DAG
from airflow.operators.empty import EmptyOperator
import pendulum

# Task 목록
task_list = ['task_1', 'task_2', 'task_3']

# DAG 정의
dag = DAG(
    dag_id='dynamic_dag_example',
    start_date=pendulum.datetime(2025, 11, 21, tz="Asia/Seoul"),
)

# 반복문을 활용한 동적 Task 생성
for task_name in task_list:
    task = EmptyOperator(
        task_id=task_name,
        dag=dag
    )