import sys
import argparse
import os
import shutil
from datetime import datetime, timedelta

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, count, from_json, to_timestamp
from pyspark.sql.types import ArrayType, StringType
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def main(report_date_str):
    print(f"시작 날짜: {report_date_str}")
    
    INPUT_PATH = "/opt/airflow/data/realtime/*.json"
    REALTIME_DIR = "/opt/airflow/data/realtime"
    ARCHIVE_DIR = "/opt/airflow/data/news_archive"
    REPORT_DIR = "/opt/airflow/data"

    spark = SparkSession.builder \
            .appName("DailyNewsReport") \
            .getOrCreate()

    report_date = datetime.strptime(report_date_str, "%Y-%m-%d")
    start_date = report_date - timedelta(days=1)
    end_date = report_date

    # 데이터 읽기
    df = spark.read.option("multiLine", True).json(INPUT_PATH)

    # write_date를 timestamp로 변환 후 필터링
    df = df.withColumn("write_date_ts", to_timestamp(col("write_date")))
    df = df.filter((col("write_date_ts") >= start_date) & (col("write_date_ts") < end_date))

    if df.rdd.isEmpty():
        print("지정된 날짜 범위에 해당하는 데이터가 없습니다.")
        spark.stop()
        sys.exit(0)

    # keywords 파싱 및 explode
    df = df.withColumn("keywords_array", from_json(col("keywords").cast("string"), ArrayType(StringType())))
    exploded_df = df.withColumn("keyword", explode(col("keywords_array")))

    # 키워드별 count
    keyword_counts = exploded_df.groupBy("keyword").agg(count("keyword").alias("count")).orderBy(col("count").desc())

    # 상위 10개 키워드
    keyword_pd = keyword_counts.limit(10).toPandas()

    # 폰트 설정 (기본 폰트)
    font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
    font_prop = fm.FontProperties(fname=font_path, size=12)

    # 그래프 그리기
    plt.figure(figsize=(10, 6))
    plt.bar(keyword_pd['keyword'], keyword_pd['count'], color='skyblue')
    plt.xlabel("키워드", fontproperties=font_prop)
    plt.ylabel("빈도수", fontproperties=font_prop)
    plt.title(f"{start_date.strftime('%Y-%m-%d')} 뉴스 리포트 - Top 10 Keywords", fontproperties=font_prop)
    plt.xticks(rotation=45, fontproperties=font_prop)
    plt.tight_layout()
    
    # 리포트 저장
    os.makedirs(REPORT_DIR, exist_ok=True)
    report_file = os.path.join(REPORT_DIR, f"daily_report_{report_date.strftime('%Y%m%d')}.pdf")
    plt.savefig(report_file)
    plt.close()

    print(f"리포트가 {report_file} 에 저장되었습니다.")

    spark.stop()

    # JSON 파일 archive 이동
    try:
        os.makedirs(ARCHIVE_DIR, exist_ok=True)

        files = os.listdir(REALTIME_DIR)
        if not files:
            print(f"{REALTIME_DIR} 디렉터리에 이동할 파일이 없습니다.")
        else:
            for file in files:
                source_path = os.path.join(REALTIME_DIR, file)
                target_path = os.path.join(ARCHIVE_DIR, file)
                shutil.move(source_path, target_path)
                print(f"파일 {source_path} -> {target_path} 로 이동")
            print(f"모든 파일이 {ARCHIVE_DIR}로 이동되었습니다.")
    except Exception as e:
        print("파일 이동 중 오류 발생:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spark를 이용한 일일 뉴스 리포트 생성")
    parser.add_argument("--date", required=True, help="보고서 기준 날짜 (YYYY-MM-DD)")
    args = parser.parse_args()

    main(args.date)


'''
batch/
├── dags/
│   └── scripts/
│       └── spark_daily_report.py     ← 이 파일 위치
├── data/
│   ├── realtime/                     ← JSON 원본 데이터
│   └── news_archive/                ← 처리 완료된 파일 이동
├── daily_report_20251204.pdf        ← PDF 리포트 저장

mkdir -p dags/scripts         # Spark 스크립트
mkdir -p data/realtime        # JSON 수신
mkdir -p data/news_archive    # 이동 대상
'''