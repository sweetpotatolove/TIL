from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

with DAG(
    dag_id='spark_submit_example',
    start_date=datetime(2025, 11, 24),
    schedule_interval=None,
    catchup=False,
    tags=['spark'],
) as dag:

    submit_job = SparkSubmitOperator(
        task_id='spark_submit_task',
        application='/opt/airflow/dags/scripts/spark_wordcount.py',
        conn_id='spark_default',
        conf={
            "spark.master": "spark://spark-master:7077"
        },
        verbose=True,
    )
