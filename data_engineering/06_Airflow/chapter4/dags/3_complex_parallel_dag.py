from airflow import DAG
from airflow.operators.empty import EmptyOperator
import pendulum

with DAG(
    dag_id="complex_parallel_example_dag",
    start_date=pendulum.datetime(2025, 11, 24, tz="Asia/Seoul"),
    catchup=False,
    schedule_interval=None,  # 원하는 스케줄 지정 가능
) as dag:

    # ---------------------
    # 1) 시작 작업
    # ---------------------
    start = EmptyOperator(task_id="start")

    # ---------------------
    # 2) 첫 번째 병렬 체인 (A 흐름)
    # ---------------------
    # A1 -> A2 순차적으로 실행
    task_A1 = EmptyOperator(task_id="task_A1")
    task_A2 = EmptyOperator(task_id="task_A2")

    # ---------------------
    # 3) 두 번째 병렬 체인 (B 흐름)
    # ---------------------
    # B1 실행 후 -> B2, B3 동시에 실행
    task_B1 = EmptyOperator(task_id="task_B1")
    task_B2 = EmptyOperator(task_id="task_B2")
    task_B3 = EmptyOperator(task_id="task_B3")

    # ---------------------
    # 4) 세 번째 병렬 체인 (C 흐름)
    # ---------------------
    # C1 -> C2 순차적으로 실행
    task_C1 = EmptyOperator(task_id="task_C1")
    task_C2 = EmptyOperator(task_id="task_C2")

    # ---------------------
    # 5) 모든 병렬 흐름 끝나고 마지막 작업
    # ---------------------
    end = EmptyOperator(task_id="end")

    # ---------------------
    # 실행 순서 정의
    # ---------------------
    # (1) 시작 -> 세 개의 병렬 흐름 동시에 시작
    start >> [task_A1, task_B1, task_C1]

    # (2) A 흐름: A1 -> A2
    task_A1 >> task_A2

    # (3) B 흐름: B1 -> (B2, B3 동시에)
    task_B1 >> [task_B2, task_B3]

    # (4) C 흐름: C1 -> C2
    task_C1 >> task_C2

    # (5) 모든 흐름(A2, B2, B3, C2)이 끝나면 end로 합류
    [task_A2, task_B2, task_B3, task_C2] >> end
