## HDFS 파일 시스템 테스트

```bash
# 로컬 작업 디렉토리 생성 (Hadoop 관련 실습 파일을 저장할 공간) 만들었다면 제외
mkdir -p /home/ssafy/ssafy_hadoop

# 해당 디렉토리로 이동
cd /home/ssafy/ssafy_hadoop

# HDFS의 DataNode들이 데이터를 저장할 로컬 경로 생성 (Hadoop 설정 시 사용됨)
mkdir -p /home/ssafy/hadoop_data

# 하둡 프로세스가 해당 디렉토리에 자유롭게 접근할 수 있도록 전체 권한 부여
sudo chmod -R 777 /home/ssafy/hadoop_data

# 예제에 사용할 간단한 텍스트 파일 생성
echo "Hello Hadoop" > test.txt

# ================== HDFS 관련 작업 시작 ==================

# HDFS 상에 디렉토리 생성
# - Hadoop 클러스터 내 분산 파일 시스템(HDFS)에 /user/local/hadoop_data 경로 생성
# - 로컬 디렉토리와는 무관한 HDFS 내부 디렉토리임
# hadoop fs : 하둡을 통해 여러 종류의 파일시스템(HDFS, 로컬, S3 등)을 공통 인터페이스로 다루는 명령어
# hdfs dfs : HDFS 전용 명령어로, NameNode에 직접 접근하는 HDFS 관리용 CLI

hadoop fs -mkdir -p /user/local/hadoop_data

# 로컬 파일(test.txt)을 HDFS의 지정된 경로에 업로드
# - 로컬 → HDFS 방향의 파일 이동
hadoop fs -put test.txt /user/local/hadoop_data

# 업로드가 제대로 되었는지 HDFS 상의 디렉토리 내용을 확인
# - HDFS 상의 경로 및 파일 목록 출력
hadoop fs -ls /user/local/hadoop_data

# 업로드된 파일의 내용을 HDFS에서 직접 출력해 확인
# - hadoop fs -cat 명령은 HDFS 상의 파일 내용을 출력
hadoop fs -cat /user/local/hadoop_data/test.txt

# HDFS 상의 파일을 로컬 경로로 다운로드
# - HDFS → 로컬 방향의 파일 복사
hadoop fs -get /user/local/hadoop_data/test.txt /home/ssafy/ssafy_hadoop/hadoop_test.txt

# HDFS 상의 파일 삭제
# - 업로드한 파일을 HDFS에서 제거
hadoop fs -rm /user/local/hadoop_data/test.txt

```

---
