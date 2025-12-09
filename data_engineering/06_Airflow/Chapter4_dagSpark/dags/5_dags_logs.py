from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
import random
import psycopg2  # 간단한 테스트용 DB
from datetime import datetime

# Task 1: CSV 데이터 읽기
def download_data():
    df = pd.read_csv("./data/input_data.csv")  # Airflow 환경에서 접근 가능하도록 절대 경로 사용
    print("데이터 로드 완료")
    return df.to_dict()  # XCom을 통해 데이터 전달

# Task 2: 데이터 처리 (old_column 삭제, age_group 추가)
def process_data(**kwargs):
    ti = kwargs['ti']
    data_dict = ti.xcom_pull(task_ids="download_data")  # XCom을 통해 데이터 가져오기
    df = pd.DataFrame(data_dict)  # Dictionary를 DataFrame으로 변환

    df = df.drop(columns=["old_column"])  # 필요 없는 컬럼 삭제
    df["age_group"] = df["age"].apply(lambda x: "Young" if x < 30 else "Adult")
    print("데이터 처리 완료")

    ti.xcom_push(key="processed_data", value=df.to_dict())  # XCom에 데이터 저장

# Task 3: 데이터 저장 
def store_data(**kwargs):
    ti = kwargs['ti']
    data_dict = ti.xcom_pull(task_ids="process_data", key="processed_data")  
    df = pd.DataFrame(data_dict)

    # 존재하지 않는 데이터베이스에 연결 시도
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="non_existent_db",
            user="airflow_user",
            password="wrong_password",
            port="5432"
        )
        cursor = conn.cursor()
        for _, row in df.iterrows():
            cursor.execute(
                "INSERT INTO users (id, name, age, age_group) VALUES (%s, %s, %s, %s)",
                (row["id"], row["name"], row["age"], row["age_group"])
            )
        conn.commit()
        cursor.close()
        conn.close()
        print("데이터 저장 완료")

    except Exception as e:
        raise ConnectionError(f"데이터베이스 연결 실패: {e}")

# DAG 정의
dag = DAG(
    "dag_logs_processing",
    schedule_interval="@daily",
    start_date=datetime(2025, 11, 24),
    catchup=False
)

# Task 정의
task_1 = PythonOperator(
    task_id="download_data",
    python_callable=download_data,
    dag=dag
)

task_2 = PythonOperator(
    task_id="process_data",
    python_callable=process_data,
    dag=dag
)

task_3 = PythonOperator(
    task_id="store_data",
    python_callable=store_data,
    dag=dag
)

# 실행 순서 정의
task_1 >> task_2 >> task_3
