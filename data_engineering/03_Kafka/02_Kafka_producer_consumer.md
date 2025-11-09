# Kafka 프로듀서와 컨슈머  
## Kafka Producer 
### Kafka 구조 복습  
- 생산자(Producer)
  - 메시지를 생산하여 브로커에 전송
- 소비자(Consumer)
  - 브로커에서 메시지를 소비

    ![alt text](image-42.png)
    - 컨슈머가 메시지를 '가져가는' 형태이므로 **비동기** 형태로 전달됨
    - -> 안정성, 확장성에 유리

- 토픽(Topic)
  - 메시지를 저장하는 **논리적** 단위, 택배를 찾을 때 주소 같은 느낌
- 파티션(Partition)
  - 메시지를 병렬로 처리하기 위한 **물리적** 단위, 큐와 유사함, 택배 창고 같은 느낌
  - 파티션이 토픽에 포함된 개념은 아님
  - 토픽과 파티션은 1:N 관계이지, 파티션이 토픽에 물리적으로 소속된 형태는 아님!!
- 브로커(Broker)
  - 메시지를 관리하는 Kafka의 서버  
- 클러스터(Cluster)
  - 함께 동작하는 Kafka 서버 집단
- 오프셋(Offset)
  - 파티션 내에서 메시지의 위치를 나타내는 고유 번호
  - 즉, 파티션 내의 메시지 순서
- 세그먼트(Segment)
  - 파티션 내에서 메시지를 저장하는 물리적 파일 단위
  - 즉, 파티션이 실제로 저장되는 물리적 단위 -> 파일 형태

### Kafka 클러스터 및 데이터 분산 복습  
- Kafka의 클러스터  
  - 컨트롤러(Controller)
    - 클러스터 관리 및 장애 처리 역할 수행  
  - 주키퍼(Zookeeper)
    - 클러스터 관리에 필요한 데이터 관리 및 헬스체크, 컨트롤러 선정 수행  
  - 레플리카(Replica)
    - 파티션의 복제본을 여러 브로커에 저장하는 방식, 리더와 팔로워로 나뉨

### Kafka Producer
- 프로듀서(Producer)
  - Kafka 토픽에 메시지를 전송하는 클라이언트
  - 다양한 데이터 소스(로그, 사용자 이벤트, 센서 데이터)에서 메시지 생성함

- Kafka Producer의 메시지 전송 과정  
  - 메시지는 **직렬화 → 파티션 결정 → 압축**의 과정을 거쳐 완성됨  
  - 그 후 **파티션별 버퍼**에 저장되어 있다가 일정 조건(시간, 용량)을 만족하면 **전송 스레드에 의해 브로커로 전송**

    ![alt text](image-43.png)
    - 직렬화(Serialization): 데이터를 바이트(Binary) 형태로 변환하는 과정(변환 전에는 데이터가 문자열, JSON 등의 형태)
    - 파티션 결정(Partitioning): 메시지를 저장할 파티션을 결정하는 과정
      - key 값에 따라 hash 함수를 적용해 파티션 결정 -> 같은 key 값은 같은 파티션에 저장하여 순서 보장 (key 파티셔닝)
    - 압축(Compression): 메시지의 크기를 줄여 전송 효율(네트워크 전송 속도 up, 저장 공간 절약)을 높이는 과정
    - 버퍼(Buffering): 전송 효율을 높이기 위해 메시지를 '일시적으로 저장'하는 메모리 공간
    - 전송 스레드(Sender Thread): 버퍼에 저장된 메시지를 브로커로 전송하는 별도의 스레드
  - 이 과정을 거치면 클러스터에서 어떤 브로커의 어떤 토픽의 리더 파티션에 메시지를 보낼지 결정되고, 팔로워는 리더로부터 복제됨

### Kafka Producer의 메시지 구조
- Kafka Producer Record
  - 레코드(Record)
    - 프로듀서가 **데이터를 전송하는 기본 단위**
  - **Topic**, **Value** 필수. 나머지는 선택사항
    | 항목 | 설명 | 예시 값 |
    |------|------|--------|
    | **Topic** | 전송될 Kafka 토픽 | `UserAction` |
    | **Value** | 전송할 값 | `"로그인 시도"` |
    | **Key** | 파티션을 지정할 키 값 | `"User 003"` |
    | **Partition** | 전송될 파티션 번호 | `3` |
    | **Headers** | 기타 포함할 정보 |  (데이터 소스 : 게임 페이지) |
    | **Timestamp** | 생성 시간 | `1728393847` |
 
### Kafka Producer의 직렬화  
- Kafka 직렬화 과정  
  - 직렬화(Serialized)
    - 문자열 같은 데이터(문자열, JSON, 객체 등)를 단순한 Byte 형태로 바꾸는 작업  
  - 역직렬화(Deserialized)
    - Byte 형태의 데이터를 다시 고수준의 원본 형태로 바꾸는 작업

    ![alt text](image-44.png)
  
  - 직렬화 장점
    - 네트워크 전송 효율 향상 -> 데이터 크기가 작고, 구조 단순하기 때문에 전송 속도 빠름
    - 스토리지 저장이 빠름 -> 스토리지 저장에 최적화된 형태가 '바이트 배열'이기 때문
    - 압축이 편리 -> 바이트 배열은 압축 알고리즘이 최적화되어 있어 압축률이 높음
    - 무결성 및 복구 용이 -> 직렬화된 데이터는 오류 검출 및 복구 메커니즘이 포함될 수 있음

### Kafka Producer의 파티션 선택  
- Kafka 파티션 선정 알고리즘  
  - RR(Round Robin)
    - 기본 파티셔너'였'음
    - 파티션 지정이 없을 경우 **파티션별로 돌아가면서 저장**

      ![alt text](image-45.png)
  - Key Base
    - 키가 결정되어 있으면 **같은 키의 데이터끼리 묶어서 처리**
    - 순서 보장이 특징임(hash 함수 사용)

      ![alt text](image-46.png)
    - 사용 시 **파티션 수 변경 금지**

      ![alt text](image-47.png)
    - 파티션 수 변경 시, 기존에 같은 키로 묶여 있던 데이터들이 다른 파티션으로 흩어져서 '순서 보장이 깨짐'
    
  - 파티션 지정
    - **저장될 파티션을 직접 지정**하는 방식

      ![alt text](image-48.png)
    - 파티션 지정 시, 키 값은 무시됨
    - 따라서, 키 값이 동일하더라도 파티션 번호가 다르다면 서로 다른 파티션에 저장됨(파티션 번호가 명시되어 있으면 해싱 무시)

  - Sticky
    - 정식 명칭: Uniform sticky (균등 끈적)
    - 기본 파티셔너
    - 하나의 **목표 파티션을 빠르게 채우고**, 목표 파티션을 바꿈

      ![alt text](image-49.png)

      ![alt text](image-50.png)
    - buffer에 일정량 이상의 데이터가 쌓이거나, 일정 시간이 지나면 목표 파티션을 변경
    - 즉, 버퍼에 데이터를 쌓아놓고 한 번에 전송하여 전송 효율을 높임
    - 버퍼가 flush(비워지는) 되는 시점에 목표 파티션을 변경

### Kafka Producer의 압축  
- Kafka 압축  
  - **효율적인 데이터 전송** 가능  
  - 브로커에서 **데이터 복사가 쉬움**

- Producer 설정에서 압축 옵션을 켜놓으면
  - 메시지가 파티션 버퍼에 저장되기 '전에' 압축 과정을 거침

    ![alt text](image-52.png)

  - 압축 알고리즘 종류
    - none: 압축하지 않음
    - `gzip`: 높은 압축률, 느린 속도 (cpu 부하가 큼)
    - `snappy`: 빠르고 가벼운 압축률 (카프카 기본값)
    - `lz4`: 빠르고 압축률도 괜찮은 편 (중간 포지션)

### Kafka Producer의 버퍼  
- Kafka RA와 버퍼  
  - RA(Record Accumulator)
    - 전송될 레코드를 모아두는 메모리 공간, 전송 효율을 높이는 버퍼의 역할  
  - 배치(Batch)
    - 한 번에 전송되는 레코드의 단위
  
  - 파티션마다 버퍼가 큐 형태로 공간을 가지고 있고, 메시지 write 시 해당 파티션의 버퍼에 저장됨
  - 이때, 전송 스레드가 주기적으로 버퍼를 확인하여, 일정 조건(배치 크기, 대기 시간 등)을 만족하면 브로커로 전송 -> 이 과정을 Drain 이라고 함
    - `batch.size`: 배치 크기 설정 (기본값 16KB)

      ![alt text](image-51.png)
    - `linger.ms`: 대기 시간 설정 (기본값 0ms)

      ![alt text](image-53.png)
    - `buffer.memory`: 버퍼 전체 크기 설정 (기본값 32MB)

      ![alt text](image-54.png)

- PlggyBack
  - Kafka Producer의 버퍼 최적화 기법으로,
  - 조건을 만족하지 않은 배치가 만족한 배치와 같은 브로커를 향할 때 함께 보내는 최적화 기법

    ![alt text](image-55.png)
    - 파티션1이 배치크기를 만족하여 브로커로 전송될 때, 파티션2도 같은 브로커를 향하고 있으므로 하나의 네트워크 호출로 함께 전송

### Kafka Producer의 전송 스레드  
- Kafka Sender Thread  
  - 동기(Sync) 전송
    - 메시지(레코드)가 확실히 브로커에 전송될 때까지 메인 스레드가 대기  

      ![alt text](image-57.png)
    - 즉, 메시지를 브로커에 보내고, 브로커가 정상적으로 받았다는 응답을 받을 때까지 기다림

  - 비동기(Async) 전송
    - 메시지(레코드)가 전송될 때까지 기다리지 않고 작업을 넘어감

      ![alt text](image-56.png)
    - 즉, 메시지를 브로커에 보내고, 응답을 기다리지 않고 바로 다음 일을 처리함
    - 전송이 끝난 뒤 성공/실패 여부를 콜백 함수로 확인
  
  - 주로 **비동기 전송을 사용**하여 전송 효율을 높임
  
- Kafka Sender의 Acknowledge 옵션
  - 메시지 전송은 비동기로 진행되지만, 메시지가 어느정도까지 저장되었는지 프로듀서가 '어느정도 확인할 것인가'를 설정하는 옵션
  - `Acks == 0`: 브로커가 정상적으로 받았는지 확인하지 않음

    ![alt text](image-58.png)
    - 가장 빠름, 그러나 데이터 유실 가능성 큼
  - `Acks == 1`: '리더'가 받았으면 다음 메시지로 넘어감, 못 받았으면 재전송
    
    ![alt text](image-59.png)
    - 팔로워 복제 여부는 확인하지 않음
  - `Acks == -1` or `Acks == all`: 리더가 받은 후 팔로워까지 모두 복제 완료되면 넘어감

    ![alt text](image-60.png)
    - 가장 안전함, 그러나 속도 느림
    - 주로 이 옵션을 사용하여 데이터 유실을 방지
 
  - `min.insync.replicas`
    - 최소 몇 개의 파티션이 ISR이 됐는지를 보장하는 옵션  
    - `Ack == -1`인 상태로 위 옵션을 적용하면 원하는 ISR을 정확히 설정할 수 있음
      - ISR(In-Sync Replica): 리더와 동기화된 상태인 복제본 파티션
      - 즉, 리더 + 리더의 데이터를 일정 시간 내에 잘 따라오고 있는 팔로워 목록

      ![alt text](image-61.png)
    - ex. ISR이 3개인 파티션에서 min.insync.replicas를 2로 설정하면,
      - 리더와 최소 1개의 팔로워가 복제 완료돼야 메시지가 성공적으로 전송된 것으로 간주하여 Acks가 리턴됨
    
    - 만약 ISR이 리더 1개만 남아있다면, `Ack == -1` 설정 시 리더만 확인하면 됨
      - 단, `min.insync.replicas` 조건에 따라 전송이 실패할 수 있음
      - ex. 팔로워 없이 리더 1개 뿐인데, min.insync.replicas가 2로 설정되어 있으면 복제본이 부족하므로 메시지 전송이 실패하게 됨

### Kafka Producer의 멱등성  
- 멱등성 프로듀서(Idempotence Producer)  
  - 데이터가 **중복해서 전송되지 않게** 하는 프로듀서 설정
  - 현재는 기본값으로 활성화되어 있음

    ![alt text](image-62.png)
    - 기존 프로듀서는 **At-Least-Once** 규칙에 따라 전달되어, 브로커에 데이터가 중복 저장될 수 있음
    - ex. 메시지 전송은 완료되었는데, 프로듀서가 응답을 받지 못해 재전송하는 경우 중복 전송이 발생할 수 있음
  
  - 멱등성 프로듀서는 각 메시지에 고유한 ID를 부여하여, 브로커가 이미 처리한 메시지인지 확인하고 중복된 메시지를 무시함
    - `Producer ID` (PID): 프로듀서 인스턴스를 식별하는 고유 ID
    - `Sequence Number`: 각 메시지에 부여되는 고유한 번호로, 메시지의 순서를 나타냄
  
  - 즉, 프로듀서가 동일한 메시지를 여러번 전송하는 것은 피할 수 없으니, 브로커 측에서 '한번만' 저장하도록 처리하자
    - `enable.idempotence = true`로 설정하여 멱등성 프로듀서를 활성화

  
## Kafka Consumer
## Kafka Consumer  
- Kafka Consumer란?  
  - 컨슈머(Consumer): Kafka Topic의 데이터를 읽는 역할을 수행하며, 이를 **구독(Subscribe)** 이라고도 함  
  - 배치하게 ETL 과정을 통해 적재하거나, 실시간으로 데이터를 가져와 처리

## Kafka Consumer 기본 용어  
- Kafka Consumer 기본 용어  
  - 컨슈머 랙(Consumer Lag): 프로듀서가 넣은 최신 메시지의 Offset과 컨슈머가 읽고 있는 Offset의 차이  
  - record-lag-max: 가장 높은 파티션의 랙

## Kafka Consumer의 용어  
- Kafka Consumer 용어  
  - 페치(Fetch): 컨슈머가 브로커로부터 레코드를 읽어오는 행위  
  - 커밋(Commit): 특정 Offset까지 처리했다고 선언하는 행위

## Kafka Consumer의 Group Coordinator  
- Kafka Consumer의 Group Coordinator  
  - 코디네이터(Coordinator): Consumer 그룹을 관리하는 브로커, 컨슈머 그룹별로 지정됨  
  - Heartbeat: 컨슈머 그룹들이 정상적으로 동작 중인지 확인 (Polling, Commit 때마다)  
  - 리밸런싱(Rebalancing): 컨슈머 그룹의 변경이 있을 때 파티션을 다시 배정하는 것

## Consumer Rebalance란?  
- Consumer Rebalance 종류  
  1. 새로운 Consumer 추가 → 기존 파티션을 일부 재할당  
  2. Consumer 제거 → 남은 Consumer가 기존 Consumer의 파티션을 담당  
  3. 파티션 개수 변경 → 전체 Consumer에 대한 Rebalance 발생

## Consumer Rebalance 과정  
- Consumer Rebalance의 과정  
  1. 그룹 코디네이터가 모든 컨슈머들의 소유권을 박탈하고 일시정지시킴

## Consumer Rebalance 과정  
- Consumer Rebalance의 과정  
  1. 그룹 코디네이터가 모든 컨슈머들의 소유권을 박탈하고 일시정지시킴  
  2. JoinGroup 요청을 기다리고, 가장 빠르게 응답한 컨슈머를 리더로 선정  
  3. 리더는 재조정한 결과를 코디네이터에게 알리고 컨슈머들에게 전달

## Consumer Rebalance 과정  
- Consumer Partitioning  
  1. RangeAssignor: 토픽별로 순서대로 나누어줌 (과거 기본값)  
  2. RoundRobinAssignor: 모든 파티션을 보고 하나씩 고르게 나누어줌  
  3. StickyAssignor: 이전 할당 정보를 활용하여 최대한 비슷하게 (현재 기본값)

## Kafka Transaction  
- 트랜잭션 프로듀서(Transaction Producer)  
  - 프로듀서와 컨슈머가 연계해서 **EOS(Exactly Once Semantics)** 를 지키는 방법  
  - 일정 단위의 메시지를 ‘커밋’으로 묶어 하나의 트랜잭션으로 설정  
  - 일정 시간 안에 트랜잭션 커밋이 오지 않으면 실패로 간주하고 처음부터 다시 메시지를 받음

## Kafka에 메시지 전송하기  
- 메시지 전송 기본 예제  
  - kafka-python: 간단하게 Kafka를 조작할 수 있는 Python 프레임워크  
  - kafka-python 설치  
  - bootstrap_servers: Kafka Broker 주소  
  - value_serializer: 인코딩 방식  
  - 실제 메시지 전송 부분  
  - 버퍼에 남아 있는 메시지를 완전히 보내고 프로듀서 종료

  - 토픽명
  - bootstrap_servers: Kafka Broker 주소 
  - auto_offset_rest: 컨슈머 초기 데이터 시작 설정
  - enable_auto_commit: 자동 커밋 설정
  - value_serializer: 디코딩 방식
  - 실제 메시지 수신부분

## Kafka의 메시지 받기  
- 메시지 수신 기본 예제  
  - 정상 출력 시 아래와 같은 모습

## Kafka에 메시지 전송하기  
- 메시지 전송 기본 예제  
  - confluent-kafka: Kafka를 조작할 수 있는 Python 프레임워크

## Kafka의 메시지 받기  
- 메시지 수신 기본 예제  
  - confluent-kafka: Kafka를 조작할 수 있는 Python 프레임워크  
  - group.id가 필수

## Kafka의 메시지 받기  
- 메시지 수신 기본 예제  
  - confluent-kafka: Kafka를 조작할 수 있는 Python 프레임워크  
  - group.id가 필수 없으면 오류 발생
  - Group을 없이 하는 방법도 있으나, Consumer가 하나뿐이어도 group.id를 지정해서 Consumer Group으로 구성

## Kafka의 메시지 받기  
- 메시지 수신 기본 예제  
  - 정상 출력 시 아래와 같은 모습
