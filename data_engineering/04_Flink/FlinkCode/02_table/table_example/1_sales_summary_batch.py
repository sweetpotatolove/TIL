import pandas as pd
import os
from pyflink.table import EnvironmentSettings, TableEnvironment

# 1. 환경 설정
env_settings = EnvironmentSettings.in_batch_mode()
t_env = TableEnvironment.create(environment_settings=env_settings)

# 2. 경로 설정
input_path = "input/online_sales_clean_final.csv"
output_path = "output/sales_summary"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# 테이블 제거 (있을 경우)
t_env.execute_sql("DROP TABLE IF EXISTS sales")
t_env.execute_sql("DROP TABLE IF EXISTS sales_summary")

# 3. 소스 테이블 생성 (csv 파싱 오류 무시 옵션 추가)
t_env.execute_sql(f"""
    CREATE TABLE sales (
        InvoiceNo STRING,
        StockCode STRING,
        Description STRING,
        Quantity DOUBLE,
        InvoiceDate STRING,
        UnitPrice DOUBLE,
        CustomerID DOUBLE,
        Country STRING,
        Discount DOUBLE,
        PaymentMethod STRING,
        ShippingCost DOUBLE,
        Category STRING,
        SalesChannel STRING,
        ReturnStatus STRING,
        ShipmentProvider STRING,
        WarehouseLocation STRING,
        OrderPriority STRING
    ) WITH (
        'connector' = 'filesystem',
        'path' = '{input_path}',
        'format' = 'csv',
        'csv.ignore-parse-errors' = 'true'
    )
""")

# 4. 집계 쿼리 실행
result = t_env.sql_query("""
    SELECT
        Category,
        ROUND(COALESCE(SUM(Quantity * UnitPrice), 0.0), 2) AS TotalSales
    FROM sales
    GROUP BY Category
""")

# 5. 결과 테이블 생성
t_env.execute_sql(f"""
    CREATE TABLE sales_summary (
        Category STRING,
        TotalSales DOUBLE
    ) WITH (
        'connector' = 'filesystem',
        'path' = '{output_path}',
        'format' = 'csv',
        'sink.parallelism' = '1'
    )
""")

# 6. 결과 삽입
result.execute_insert("sales_summary").wait()
print("카테고리별 총 매출 집계 완료:", output_path)