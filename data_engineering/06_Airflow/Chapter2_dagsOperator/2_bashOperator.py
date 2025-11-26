from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="bash_operator_example",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2025, 11, 22, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
) as dag:
    bash_t1 = BashOperator(
        task_id="bahs_t1",
        bash_command='echo "Hello, Airflow!"',
    )
    bash_t2 = BashOperator(
    task_id="bahs_t2",
    bash_command="ls -al",
)
    
    bash_t1 >> bash_t2


    