import pendulum
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

local_tz = pendulum.timezone("Asia/Seoul")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='daily_report_dag',
    default_args=default_args,
    description='매일 새벽 1시에 Spark를 이용해 뉴스 리포트 생성',
    schedule_interval='0 1 * * *',
    start_date=datetime(2025, 5, 1, tzinfo=local_tz),
    catchup=False,
    tags=['daily', 'report', 'spark']
) as dag:
    
    # job 제출(Tark1)
    submit_spark_job = SparkSubmitOperator(
        task_id='spark_daily_report',
        application='/opt/airflow/dags/scripts/spark_daily_report.py',  # Spark에게 실행해달라고 job 제출
        conn_id='spark_default',
        conf={
            'spark.master': 'spark://spark-master:7077'
        },
        application_args=['--date', '{{ ds }}'],    # ds: 분석에 사용하려는 날짜
    )

    # 더미 데이터(Task2) 예시용
    notify_report_generated = BashOperator(
        task_id='notify_report_generated',
        bash_command=(
            'echo "리포트가 생성되었습니다: 이메일 보내기"'
        )
    )

    submit_spark_job >> notify_report_generated

if __name__ == "__main__":
    dag.test()
