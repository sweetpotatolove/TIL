from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings

import os
import time
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Flink 작업 시작...")
    
    # 스트림 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()
    # Table API는 Batch와 Streaming 모드를 명확히 구분
    # DataStream API는 기본이 스트리밍 → 별도 설정 필요 없음
    # Table API에서 Kafka 사용 시	in_streaming_mode() + StreamTableEnvironment 필수
    env_settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
    table_env = StreamTableEnvironment.create(env, environment_settings=env_settings)
    
    # 로깅 레벨 설정
    table_env.get_config().get_configuration().set_string("pipeline.global-job-parameters.logger.level", "INFO")
    
    # JAR 파일 추가 (전체 경로로 수정하세요)
    kafka_jar = os.path.join(os.path.abspath('.'), 'flink-sql-connector-kafka-3.3.0-1.19.jar')
    logger.info(f"사용하는 JAR 파일 경로: {kafka_jar}")
    if not os.path.exists(kafka_jar):
        logger.error(f"JAR 파일이 존재하지 않습니다: {kafka_jar}")
        return
    
    table_env.get_config().get_configuration().set_string("pipeline.jars", f"file://{kafka_jar}")
    
    # 소스 테이블 정의
    try:
        logger.info("Kafka 소스 테이블 생성 시도...")
        table_env.execute_sql("""
        CREATE TABLE kafka_source (
            user_id STRING,
            item_id STRING,
            category STRING,
            behavior STRING,
            ts TIMESTAMP(3),
            proctime AS PROCTIME()
        ) WITH (
            'connector' = 'kafka',
            'topic' = 'user_behaviors',
            'properties.bootstrap.servers' = 'localhost:9092',
            'properties.group.id' = 'flink-consumer-group',
            'scan.startup.mode' = 'earliest-offset',
            'format' = 'json',
            'json.fail-on-missing-field' = 'false',
            'json.ignore-parse-errors' = 'true'
        )
        """)
        logger.info("Kafka 소스 테이블 생성 성공")
    except Exception as e:
        logger.error(f"소스 테이블 생성 중 오류 발생: {e}")
        return
    
    # 싱크 테이블 정의
    try:
        logger.info("Kafka 싱크 테이블 생성 시도...")
        table_env.execute_sql("""
        CREATE TABLE kafka_sink (
            category STRING,
            behavior STRING,
            behavior_count BIGINT,
            update_time TIMESTAMP(3),
            PRIMARY KEY (category, behavior) NOT ENFORCED
        ) WITH (
            'connector' = 'upsert-kafka',
            'topic' = 'behavior_stats',
            'properties.bootstrap.servers' = 'localhost:9092',
            'key.format' = 'json',
            'value.format' = 'json',
            'properties.group.id' = 'flink-sink-group'
        )
        """)
        logger.info("Kafka 싱크 테이블 생성 성공")
    except Exception as e:
        logger.error(f"싱크 테이블 생성 중 오류 발생: {e}")
        return
    
    # 작업 제출
    try:
        logger.info("SQL 쿼리 실행 시도...")
        stmt_set = table_env.create_statement_set()
        stmt_set.add_insert_sql("""
        INSERT INTO kafka_sink
        SELECT 
            category,
            behavior,
            COUNT(*) AS behavior_count,
            CURRENT_TIMESTAMP as update_time
        FROM kafka_source
        GROUP BY category, behavior
        """)
        
        # 작업 실행 및 JobClient 가져오기
        job_client = stmt_set.execute().get_job_client()
        
        if job_client:
            job_id = job_client.get_job_id()
            logger.info(f"작업이 성공적으로 제출되었습니다. 작업 ID: {job_id}")
            
            # 작업 상태 확인
            monitor_job(job_client)
        else:
            logger.error("작업 클라이언트를 가져올 수 없습니다.")
    except Exception as e:
        logger.error(f"작업 실행 중 오류 발생: {e}")

def monitor_job(job_client):
    """작업 상태에 대한 로그를 출력합니다."""
    try:
        # 작업 상태 확인
        # Flink Job 상태 값
        # RUNNING    : Flink 작업이 현재 실행 중
        # FINISHED   : 작업이 성공적으로 완료됨
        # FAILED     : 작업 실패
        # CANCELED   : 작업이 중단됨
        # RESTARTING : 작업이 재시작 중
        
        job_status = job_client.get_job_status().result()

        logger.info(f"현재 작업 상태: {job_status}")
        
        # 샘플 데이터가 있는지 확인
        logger.info("Kafka 토픽에 샘플 데이터가 있는지 확인해주세요.")
        logger.info("샘플 데이터가 없다면 kafka_producer.py를 실행하여 테스트 데이터를 생성하세요.")
        
        # 작업 실행 중 상태 확인
        print("\n작업 확인 시작 (10초마다 상태 확인, Ctrl+C로 종료)")
        for i in range(6):  # 60초 동안 확인
            time.sleep(10)
            try:
                current_status = job_client.get_job_status().result()
                print(f"[{i+1}/6] 현재 작업 상태: {current_status}")
                
                # 선택적: 작업 메트릭스 확인 (PyFlink API가 지원하는 경우)
                # 이 부분은 PyFlink 버전에 따라 다를 수 있습니다
                if hasattr(job_client, 'get_job_metrics'):
                    metrics = job_client.get_job_metrics()
                    print(f"작업 메트릭스: {metrics}")
            except Exception as e:
                print(f"상태 확인 중 오류 발생: {e}")
        
        print("\n확인 완료. 작업은 계속 실행 중입니다.")
        print("결과를 확인하려면 다음 명령어를 실행하세요:")
        print("$KAFKA_HOME/bin/kafka-console-consumer.sh --topic behavior_stats --bootstrap-server localhost:9092 --from-beginning")
        
    except Exception as e:
        logger.error(f"작업 확인 중 오류 발생: {e}")

if __name__ == '__main__':
    main()
    