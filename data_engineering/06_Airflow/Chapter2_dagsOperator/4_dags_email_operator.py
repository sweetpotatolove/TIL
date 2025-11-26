from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2025, 11, 22, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
) as dag:
    send_email_task = EmailOperator(
        task_id='send_email_task',
        to='timeors0330@gmail.com', # {본인 이메일}
        subject='Airflow 성공메일',
        html_content='Airflow 작업이 완료되었습니다.'
    )