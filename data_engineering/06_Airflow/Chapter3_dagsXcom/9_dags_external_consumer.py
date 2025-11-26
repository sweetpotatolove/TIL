from airflow import DAG
from airflow.sensors.external_task import ExternalTaskSensor
import pendulum

dag_b = DAG(
    dag_id="dag_b",
    start_date=pendulum.datetime(2025, 11, 21, tz="Asia/Seoul"),
)

wait_for_task_a = ExternalTaskSensor(
    task_id="wait_for_task_a",
    external_dag_id="dag_a",  # DAG A를 감지
    external_task_id="task_a",  # DAG A의 task_a 완료 여부 확인
    timeout=600,  # 600초(10분) 동안 기다림
    poke_interval=30,  # 30초마다 상태 확인
    mode="poke",  # 센서 실행 방식 (poke 또는 reschedule)
    dag=dag_b
)
