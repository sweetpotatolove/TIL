# Hadoop Cluster (Docker 기반) 설치 및 실행   
### 1 NameNode + 2 DataNode 실행 스크립트  

Docker 기반으로 Hadoop 멀티 노드 클러스터를 구성하는 환경
HDFS 복제본 2, YARN 기반 MapReduce, SSH 자동 실행, 컨테이너 시작 시 Hadoop 자동 실행

---

# 1. Docker Compose 구성  
Hadoop 클러스터의 각 노드를 Docker 컨테이너로 구성합니다.

```yaml
services:
  namenode:
    build: .
    container_name: namenode
    hostname: namenode
    ports:
      - "9870:9870"   # NameNode UI (HDFS 상태)
      - "9000:9000"   # fs.defaultFS (HDFS 접근 포트)
      - "8088:8088"   # YARN ResourceManager UI
    networks:
      - hadoop-net

  datanode1:
    build: .
    container_name: datanode1
    hostname: datanode1
    ports:
      - "9864:9864"   # DataNode UI
    networks:
      - hadoop-net

  datanode2:
    build: .
    container_name: datanode2
    hostname: datanode2
    ports:
      - "9865:9864"   # DataNode UI
    networks:
      - hadoop-net

networks:
  hadoop-net:
    external: true
```

## 설명
- 각 서비스는 Hadoop 클러스터의 **실제 노드** 역할을 수행합니다.
- `hostname`은 Hadoop 내부에서 **노드 식별자**로 사용되므로 매우 중요합니다.
- 원하는 포트만 호스트에 노출하여 UI 접근 가능:
  - 9870 → NameNode UI  
  - 8088 → ResourceManager UI  
  - 9864/9865 → DataNode UI  
- 모든 노드는 `hadoop-net` 네트워크를 공유하며 내부적으로 서로 통신합니다.

---

# 2. Dockerfile  
Hadoop, Java 11, SSH, Python 환경까지 포함한 이미지 생성.

```dockerfile
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Hadoop + Java 버전
ENV HADOOP_VERSION=3.3.5
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV HADOOP_HOME=/usr/local/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

# 기본 패키지 + Python3 포함
RUN apt-get update && \
    apt-get install -y \
        openjdk-11-jdk \
        ssh \
        curl \
        rsync \
        nano \
        python3 \
        python3-pip \
        python3-distutils \
        python3-venv \
    && apt-get clean

# python3 → python 심볼릭 링크 (Hadoop Streaming 호환용)
RUN ln -s /usr/bin/python3 /usr/bin/python || true

# Hadoop 다운로드 및 설치
RUN curl -O https://downloads.apache.org/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz && \
    tar -xzvf hadoop-$HADOOP_VERSION.tar.gz -C /usr/local && \
    mv /usr/local/hadoop-$HADOOP_VERSION $HADOOP_HOME && \
    rm hadoop-$HADOOP_VERSION.tar.gz

# Hadoop 설정 파일 복사
COPY core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml
COPY hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml
COPY yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml
COPY mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml
COPY capacity-scheduler.xml $HADOOP_HOME/etc/hadoop/capacity-scheduler.xml

# Entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# 필요한 포트 공개
EXPOSE 9870 9864 9866 8088 8042 9000

CMD ["/entrypoint.sh"]
```

## 설명
- Hadoop은 **Java 11**을 요구 → JAVA_HOME 설정 필수.
- SSH는 Hadoop 내부에서 Localhost도 SSH 접속을 하기 때문에 필수.
- Python은 Hadoop Streaming 과제나 ETL 처리 등 확장성을 위해 포함.
- 설정 파일을 Dockerfile 단계에서 복사하여 **이미지 빌드 시 구성 고정**.
- entrypoint.sh가 컨테이너 시작 시 Hadoop 자동 실행.

---

# 3. Hadoop 설정 파일  
설정 파일은 `/usr/local/hadoop/etc/hadoop/`에 위치합니다.

---

## 3.1 core-site.xml  
HDFS 기본 주소 설정.

```xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://namenode:9000</value>
    </property>
</configuration>
```

### 설명
- HDFS 접근 기본 URL을 설정.
- Docker에서는 hostname 기반 DNS가 제공되므로 반드시 **namenode** 사용.

---

## 3.2 hdfs-site.xml  
HDFS 저장 구조 + 복제본 설정.

```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>2</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:///usr/local/hadoop/hdfs/namenode</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:///usr/local/hadoop/hdfs/datanode</value>
    </property>
</configuration>
```

### 설명
- replication=2 → DataNode가 2개이므로 완전한 복제본 구성 가능.
- namenode.name.dir → 메타데이터 저장 위치.
- datanode.data.dir → 실제 HDFS 블록 저장 디렉토리.

---

## 3.3 mapred-site.xml  
MapReduce → YARN 위에서 실행하도록 지정.

```xml
<configuration>

  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>

  <property>
    <name>yarn.app.mapreduce.am.env</name>
    <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
  </property>

  <property>
    <name>mapreduce.map.env</name>
    <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
  </property>

  <property>
    <name>mapreduce.reduce.env</name>
    <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
  </property>

</configuration>
```

### 설명
- MRV2(MapReduce v2)는 **YARN 기반**으로 실행되기 때문에 필수 설정.
- Docker에서는 각 컨테이너 환경이 분리되므로 환경 변수 전달을 명시해야 함.

---

## 3.4 yarn-site.xml  
ResourceManager, NodeManager 설정 + 스케줄러 지정.

```xml
<configuration>
  <property>
    <name>yarn.resourcemanager.hostname</name>
    <value>namenode</value>
  </property>

  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>

  <property>
    <name>yarn.resourcemanager.scheduler.class</name>
    <value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler</value>
  </property>

</configuration>
```

### 설명
- ResourceManager는 NameNode 컨테이너에서 동작하도록 설정.
- NodeManager는 MR 작업 중 shuffle 처리를 위해 반드시 mapreduce_shuffle 필요.
- FairScheduler는 여러 작업에 공정하게 리소스를 배분.

---

# 4. entrypoint.sh  
컨테이너 시작 시 Hadoop 자동 실행.

```bash
#!/bin/bash

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

service ssh start

echo "[$HOSTNAME] Starting Hadoop Services..."

if [[ "$HOSTNAME" == "namenode" ]]; then
    echo "[Namenode] Formatting HDFS..."
    hdfs namenode -format -force

    echo "[Namenode] Starting NameNode..."
    hdfs namenode &

    echo "[Namenode] Starting ResourceManager..."
    yarn resourcemanager &

    tail -f /dev/null

else
    echo "[$HOSTNAME] Starting DataNode..."
    hdfs datanode &

    echo "[$HOSTNAME] Starting NodeManager..."
    yarn nodemanager &

    tail -f /dev/null
fi
```

## 설명
- 모든 컨테이너에서 SSH 서비스 자동 시작.
- NameNode에서는 **HDFS 초기 포맷 + NameNode + ResourceManager** 실행.
- DataNode에서는 **DataNode + NodeManager** 실행.
- tail -f /dev/null → 프로세스를 유지하여 컨테이너가 종료되지 않도록 함.

---

# 5. 실행 방법

```bash
docker compose up -d
```

모든 노드가 자동으로 Hadoop 서비스를 실행함.

---

# 6. UI 접속 URL

| 구성 요소 | 주소 |
|-----------|------|
| NameNode UI | http://localhost:9870 |
| ResourceManager UI | http://localhost:8088 |
| DataNode1 | http://localhost:9864 |
| DataNode2 | http://localhost:9865 |

---

# 7. 요약

- Docker 기반 Hadoop 완전 자동화 클러스터  
- NameNode 1개 + DataNode 2개  
- replication=2  
- YARN + MapReduce 완전 구성  
- entrypoint.sh 통한 자동 부팅  
- 교육/실습/개발 환경에 최적화  

