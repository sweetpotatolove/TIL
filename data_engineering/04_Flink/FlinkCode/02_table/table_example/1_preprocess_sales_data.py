import pandas as pd
import os

# 1. CSV 읽기
df = pd.read_csv("input/online_sales_dataset.csv")

# 2. 숫자형 컬럼 강제 변환 및 결측값 채우기
numeric_cols = ["Quantity", "UnitPrice", "ShippingCost", "CustomerID", "Discount"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0.0)

# 3. 필터링 (양수 & 카테고리 존재)
df = df[
    (df["Quantity"] > 0) &
    (df["UnitPrice"] > 0) &
    df["ShippingCost"].notna() &
    df["CustomerID"].notna() &
    df["Discount"].notna() &
    df["Category"].notna()
]

# 4. 문자열 정리
df["Category"] = df["Category"].astype(str).str.strip()
df[numeric_cols] = df[numeric_cols].astype(float)

# 5. 순서 고정 (Flink 스키마와 일치)
final_cols = [
    "InvoiceNo", "StockCode", "Description", "Quantity", "InvoiceDate",
    "UnitPrice", "CustomerID", "Country", "Discount", "PaymentMethod",
    "ShippingCost", "Category", "SalesChannel", "ReturnStatus",
    "ShipmentProvider", "WarehouseLocation", "OrderPriority"
]
df = df[final_cols]

# 6. 저장
os.makedirs("input", exist_ok=True)
df.to_csv("input/online_sales_clean_final.csv", index=False, encoding="utf-8", float_format="%.2f")
print("정제된 CSV 저장 완료")
