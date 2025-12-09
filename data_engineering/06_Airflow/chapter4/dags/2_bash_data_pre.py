from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# 기본 DAG 설정
default_args = {
    "start_date": datetime(2025, 11, 24),
}
dag = DAG(
    "bash_processing_dag",
    default_args=default_args,
    description="DAG to process using Bash script",
)

# BashOperator Task
process_csv_task = BashOperator(
    task_id="process_csv",
    bash_command="/opt/airflow/plugins/shell/process_csv.sh ",  # 스크립트 실행
    dag=dag,
)

# DAG 실행 순서 정의
process_csv_task



