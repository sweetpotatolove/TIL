from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd

# CSV 파일 경로
# dag와 동일한 경로
CSV_FILE_PATH = "./data/input_data.csv"
OUTPUT_FILE_PATH = "./data/output_data.csv"

# 데이터 변환 함수
def transform_csv():
    # CSV 파일 읽기
    df = pd.read_csv(CSV_FILE_PATH)
    
    # 데이터 변환 (예: 컬럼명 변경 및 새로운 컬럼 추가)
    df.rename(columns={"old_column": "new_column"}, inplace=True)
    df["processed_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 변환된 데이터 저장
    df.to_csv(OUTPUT_FILE_PATH, index=False)
    print("Data transformation complete. Saved to", OUTPUT_FILE_PATH)

# DAG 설정
default_args = {
    "start_date": datetime(2025, 11, 24),
}

dag = DAG(
    "csv_transform_dag",
    default_args=default_args,
    description="DAG to read and transform CSV file",
)

# PythonOperator Task
transform_task = PythonOperator(
    task_id="transform_csv_task",
    python_callable=transform_csv,
    dag=dag,
)

# DAG 실행 순서
transform_task



