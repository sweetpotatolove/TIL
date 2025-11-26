from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
import pendulum


'''
Connection 등록 (필수)
PostgresHook(postgres_conn_id="my_postgres_conn") 이 코드가 작동하려면
해당 Connection ID(my_postgres_conn)가 Airflow Web UI > Admin > Connections에 사전에 등록되어 있어야 합니다.
'''

# Postgres 연결 체크 함수
def fetch_postgres_data():
    hook = PostgresHook(postgres_conn_id="my_postgres_conn")
    conn = hook.get_connection("my_postgres_conn")
    print(f"Connecting to host={conn.host}, port={conn.port}, db={conn.schema}, user={conn.login}")

    with hook.get_conn() as raw_conn:
        with raw_conn.cursor() as cur:
            cur.execute("SELECT 1;")
            one = cur.fetchone()[0]
            cur.execute("SELECT version();")
            version = cur.fetchone()[0]

    if one == 1:
        print("Postgres 연결 OK")
        print(f"Postgres version: {version}")
    else:
        raise Exception("Postgres 연결 실패")

# DAG 정의
with DAG(
    dag_id="postgres_hook_python_operator",
    start_date=pendulum.datetime(2025, 8, 18, tz="Asia/Seoul"),
    schedule_interval="@daily",
    catchup=False,
    tags=["postgres", "hook"]
) as dag:

    fetch_data_task = PythonOperator(
        task_id="fetch_postgres_data",
        python_callable=fetch_postgres_data
    )

    fetch_data_task
