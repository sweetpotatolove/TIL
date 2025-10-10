import requests
import pandas as pd

data = pd.DataFrame([
    [7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]
], columns=[
    "fixed acidity", "volatile acidity", "citric acid", "residual sugar",
    "chlorides", "free sulfur dioxide", "total sulfur dioxide",
    "density", "pH", "sulphates", "alcohol"
])

response = requests.post(
    "http://localhost:5001/invocations",
    headers={"Content-Type": "application/json"},
    json={"dataframe_records": data.to_dict(orient="records")}
)

print(response.json())


'''
품질 점수 (quality)	의미	비고
3 ~ 4	낮은 품질	드묾
5 ~ 6	보통 품질	가장 많음
7 ~ 8	우수 품질	일부 있음
9	매우 우수	극히 드물게 있음
'''