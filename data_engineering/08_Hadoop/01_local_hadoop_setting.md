# Hadoop 설치 및 실행 환경 설정 (WSL 기반)

WSL 환경에서 Hadoop을 설치하고 실행하기 위한 기본 설정 방법을 정리
SSH 설정 → Hadoop 다운로드 및 설치 → 환경설정 → 실행까지 진행

---

## 1. SSH 설치

Hadoop은 클러스터 환경(멀티 노드)에서 동작하도록 설계되어 있어, **노드 간 통신**에 SSH를 사용합니다.  
단일 PC(WLS)에서도 마찬가지로 SSH 환경이 필요합니다.

```bash
sudo apt install -y openssh-server
```

- `openssh-server`: SSH 프로토콜을 이용한 원격 접속을 제공하는 데몬.  
- Hadoop 실행 시 내부적으로 **자기 자신(localhost)** 에도 SSH 접속을 하기 때문에 세팅이 필요합니다.

---

## 2. SSH 키 생성 및 설정

비밀번호 입력 없이 SSH 접속이 가능하도록 키 기반 인증을 설정합니다.

```bash
ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

- `ssh-keygen`: RSA 키쌍(private/public)을 생성.  
- `-P ""`: 패스프레이즈 없이 키 생성.  
- `authorized_keys`: 허용된 공개키 목록. 본인 키를 등록하면 자기 자신에게 무비밀번호 접속 가능.  
- `chmod 600`: 보안상 권한 설정(읽기/쓰기 본인만).

> 이 설정이 없으면 Hadoop 실행 시마다 SSH 비밀번호 입력을 요구하여 자동화 실행이 불가능합니다.

---

## 3. Hadoop 설치

1. 홈 디렉토리 이동  
   ```bash
   cd /home/ssafy
   ```

2. Hadoop 다운로드  
   ```bash
   wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.5/hadoop-3.3.5.tar.gz
   ```

3. 압축 해제  
   ```bash
   tar -xvzf hadoop-3.3.5.tar.gz
   ```

4. 디렉토리명 변경  
   ```bash
   mv hadoop-3.3.5 hadoop
   ```

- `wget`: 공식 아파치 미러에서 Hadoop 소스 다운로드.  
- `tar`: 압축 해제.  
- 디렉토리명을 `hadoop`으로 변경하면 버전 업그레이드 시 관리가 용이합니다.

---

## 4. Hadoop 환경 변수 설정

Hadoop 실행에 필요한 **JAVA_HOME**을 지정해야 합니다.  
(Hadoop은 자바 기반 프로그램)

```bash
sudo apt update
sudo apt install -y openjdk-11-jdk
```

```bash
vi /home/ssafy/hadoop/etc/hadoop/hadoop-env.sh
```

```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

- Hadoop은 Java 11을 권장합니다.  
- `hadoop-env.sh`는 Hadoop 실행 시 로딩되는 환경 변수 파일입니다.

---

## 5. Hadoop 설정 파일 수정

```bash
vi ~/.bashrc
```

```bash
export HADOOP_HOME=/home/ssafy/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```

Hadoop 실행을 위해 총 **4개 설정 파일**을 수정합니다.

---

### 5.1 core-site.xml

```xml
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
  </property>
</configuration>
```

- `fs.defaultFS`: HDFS 기본 파일시스템 주소.  
- `localhost:9000`: NameNode가 서비스하는 주소와 포트.

---

### 5.2 yarn-site.xml

```xml
<configuration>
  <property>
    <name>yarn.resourcemanager.hostname</name>
    <value>localhost</value>
  </property>
  
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>

  <!-- 추가 -->
  <property>
    <name>yarn.log-aggregation-enable</name>
    <value>true</value>
  </property>
</configuration>
```

- YARN은 Hadoop의 리소스 관리 프레임워크.  
- `resourcemanager.hostname`: 클러스터 중앙 관리자인 ResourceManager 위치.  
- `mapreduce_shuffle`: 맵리듀스 실행 시 필요한 데이터 셔플링 지원 서비스.

---

### 5.3 mapred-site.xml

```xml
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>

  <property>
    <name>yarn.app.mapreduce.am.env</name>
    <value>HADOOP_MAPRED_HOME=/home/ssafy/hadoop</value>
  </property>

  <property>
    <name>mapreduce.map.env</name>
    <value>HADOOP_MAPRED_HOME=/home/ssafy/hadoop</value>
  </property>

  <property>
    <name>mapreduce.reduce.env</name>
    <value>HADOOP_MAPRED_HOME=/home/ssafy/hadoop</value>
  </property>
</configuration>
```

- MapReduce 작업을 실행할 프레임워크 지정.  
- `yarn`: YARN 위에서 맵리듀스 실행. (기본 `local` 대신)

---

### 5.4 hdfs-site.xml

```xml
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>

  <property>
    <name>dfs.namenode.name.dir</name>
    <value>file:///home/ssafy/hadoop/data/namenode</value>
  </property>

  <property>
    <name>dfs.datanode.data.dir</name>
    <value>file:///home/ssafy/hadoop/data/datanode</value>
  </property>
</configuration>
```

- `dfs.replication`: 복제본 개수(WSL 단일 노드이므로 `1`).  
- `dfs.namenode.name.dir`: NameNode 메타데이터 저장 경로.  
- `dfs.datanode.data.dir`: DataNode 실제 블록 저장 경로.

---

## 6. HDFS 데이터 디렉토리 생성

```bash
mkdir -p ~/hadoop/data/namenode
mkdir -p ~/hadoop/data/datanode
```

> 위에서 지정한 `hdfs-site.xml` 경로와 반드시 일치해야 합니다.

---

## 7. Hadoop 실행

0. 설정 적용
   ```bash
  source ~/.bashrc
   ```
1. **HDFS 포맷** (최초 1회)  
   ```bash
   hdfs namenode -format
   ```

   - NameNode 메타데이터 초기화.  
   - `VERSION` 파일과 메타데이터 구조 생성.

2. **HDFS 실행**  
   ```bash
   start-dfs.sh
   ```

   - NameNode, DataNode, SecondaryNameNode 시작.

3. **YARN 실행**  
   ```bash
   start-yarn.sh
   ```

   - ResourceManager, NodeManager 시작.

---

## 8. 설치 완료 확인

- `jps` 명령어로 실행 중인 JVM 프로세스 확인:

```bash
jps
```

예상 출력:
- `jps` 명령어 실행 시 아래와 같은 프로세스가 떠야 정상 동작합니다.  

- **NameNode** – HDFS 메타데이터 관리  
- **DataNode** – HDFS 블록 저장  
- **SecondaryNameNode** – 메타데이터 체크포인트 보조  
- **ResourceManager** – 클러스터 자원 관리  
- **NodeManager** – 개별 노드 자원 및 작업 실행 담당  

---

## 정리

- **SSH**: 클러스터 통신 기반  
- **환경변수**: Hadoop 실행 필수 (JAVA_HOME)  
- **설정 파일 4개**: core, yarn, mapred, hdfs  
- **디렉토리**: HDFS 데이터 저장소 준비  
- **실행**: `hdfs namenode -format → start-dfs.sh → start-yarn.sh`  
- **검증**: `jps` 프로세스로 정상 동작 확인  

---