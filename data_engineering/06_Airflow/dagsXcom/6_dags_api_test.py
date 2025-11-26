import requests
from airflow import DAG
from airflow.operators.python import BranchPythonOperator, PythonOperator
from airflow.operators.bash import BashOperator
import pendulum

# API 응답값을 확인하여 실행할 Task 결정하는 함수
def check_weather():
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=37.5665&longitude=126.9780&current_weather=true"
    )
    data = response.json()
    
    # JSON 응답 전체 출력
    print("API 응답 전체 데이터:", data)

    # 현재 기온 가져오기
    temperature = data["current_weather"]["temperature"]
    print("현재 기온:", temperature, "도")

    if temperature >= 15:
        return "task_hot"
    else:
        return "task_cold"

# API 응답값을 출력하는 함수
def print_weather():
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=37.5665&longitude=126.9780&current_weather=true"
    )
    data = response.json()

    temperature = data["current_weather"]["temperature"]
    print("현재 날씨 데이터:", data)
    print("현재 기온:", temperature, "도")

# DAG 정의
with DAG(
    dag_id="branch_operator_weather_api_logging_example",
    start_date=pendulum.datetime(2025, 11, 21, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    # API 상태 확인 후 실행할 Task 선택
    branch_task = BranchPythonOperator(
        task_id="branching_weather_api",
        python_callable=check_weather
    )

    # 15도 이상이면 실행될 Task
    task_hot = BashOperator(
        task_id="task_hot",
        bash_command="echo '오늘 날씨: 덥습니다'"
    )

    # 15도 미만이면 실행될 Task
    task_cold = BashOperator(
        task_id="task_cold",
        bash_command="echo '오늘 날씨: 춥습니다'"
    )

    # API 결과값을 출력하는 Task
    log_weather = PythonOperator(
        task_id="log_weather",
        python_callable=print_weather
    )

    # DAG 실행 흐름 설정
    log_weather >> branch_task >> [task_hot, task_cold]
