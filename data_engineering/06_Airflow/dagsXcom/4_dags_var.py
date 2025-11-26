from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable  # Airflow Variable 모듈 불러오기
import pendulum

# Variable에서 값을 가져오는 함수
def print_variable():
    my_var = Variable.get("my_variable", default_var="default")
    print("Airflow Variable 값:", my_var)

# DAG 정의
with DAG(
    dag_id="airflow_variable_example",
    start_date=pendulum.datetime(2025, 11, 21, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    # 전역 변수 출력 Task
    print_var_task = PythonOperator(
        task_id="print_variable_task",
        python_callable=print_variable
    )