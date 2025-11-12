FROM flink:1.19-scala_2.12-java17

# 2. Python & pip 설치 + PyFlink 설치
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install --no-cache-dir apache-flink==1.19.3 && \
    pip install pandas

# 3. 기본 Python3 링크 설정
RUN ln -s /usr/bin/python3 /usr/bin/python

# 4. 작업 디렉토리 설정
WORKDIR /opt/flink
