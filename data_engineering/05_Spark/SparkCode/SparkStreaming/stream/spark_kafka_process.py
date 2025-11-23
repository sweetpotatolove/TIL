from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, window
from pyspark.sql.types import StructType, StructField, TimestampType, StringType
import findspark

findspark.init()

# SparkSession 생성
def create_spark_session():
    return (SparkSession.builder
        .appName("KafkaSparkStreaming")
        .config("spark.jars.packages",
                "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0")
        .getOrCreate())

def process_kafka_stream():

    spark = create_spark_session()

    # Kafka 스트림 읽기
    df = (spark
        .readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", "localhost:9092")
        .option("subscribe", "test-topic")
        .option("startingOffsets", "latest")
        .load()
    )

    # Kafka value → 문자열
    value_df = df.selectExpr("CAST(value AS STRING)")

    # JSON 스키마
    schema = StructType([
        StructField("timestamp", TimestampType(), True),
        StructField("message", StringType(), True)
    ])

    # JSON 파싱
    parsed_df = (value_df
        .select(from_json(col("value"), schema).alias("data"))
        .select("data.*")
    )

    # 1분 윈도우 + watermark + count
    result_df = (parsed_df
        .withWatermark("timestamp", "1 minute")
        .groupBy(window("timestamp", "1 minute"))
        .count()
    )

    # 콘솔 출력
    query = (result_df
        .writeStream
        .outputMode("complete")
        .format("console")
        .start()
    )

    query.awaitTermination()

if __name__ == "__main__":
    process_kafka_stream()
