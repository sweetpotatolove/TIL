# Command Line Interface
**명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식**

(GUI: 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식)

### CLI에서 ' . ' (점)의 역할
1. `.` 현재 디렉토리 ex. A.txt
2. `..` 현재의 상위 디렉토리

### 기초 문법
- `touch` 파일 생성
  - 예시: touch some_file.txt
  - 파일 이름에 띄어쓰기 불가
- `mkdir x` 새 디렉토리 생성
- `ls` 현재 작업중인 디렉토리 내부의 폴더/파일 목록을 출력
  - 숨김 파일을 봐야 한다면 `ls -a` 사용
- `cd` 현재 작업 중인 디렉토리 변경(위치이동; change directory)
  1. **cd ..** [~/Desktop/study/00_startcamp/01_git]
  2. **mkdir 02_git_adv** [~/Desktop/study/00_startcamp]
  3. **cd 02_git_adv** [~/Desktop/study/00_startcamp/02_git_adv]
  4. **cd ../01_git/** [~/Desktop/study/00_startcamp/01_git]
- `start` 폴더/파일 열기
- `rm` 파일 삭제(디렉토리 삭제는 -r 옵션을 추가 사용)
  - `rm some some_file.txt` 공백으로 한번에 여러개 삭제 가능
  - `rm -r` 디렉토리 삭제는 -r 옵션(재귀) 추가 사용
  - rm으로 삭제하면 휴지통에도 안남으니 정말 지워도 될지 다시 생각해보기

#### ※ CLI에서 가장 중요한 것: 내가 '어디 있는지' 경로를 알아야 한다

### 절대 경로
Root 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것 

ex. C:/User/ssafy/Desktop

### 상대 경로
현재 작업하고 있는 디렉토리 기준으로 계산된 상대적 위치를 작성한 것

ex. 현재 작업 디렉토리가 C:/Users 일 때, 윈도우 바탕 화면으로의 상대 경로는 ssafy/Desktop

