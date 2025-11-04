# Python 3.10 slim 버전 사용
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /workspace

# 라이브러리 설치
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Python 앱 복사 및 실행 설정
COPY app.py .
CMD ["python", "app.py"]
