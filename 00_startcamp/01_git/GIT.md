# git
**분산 버전 관리 시스템**

- 버전 관리: 변화를 기록하고 추적하는 것
  - 각 버전은 이전 버전으로부터의 **변경사항**을 기록하고 있음
  - 코드 버전관리 필수 !
  - 수정된, 추가된 코드가 각 버전에 들어있는 것이므로 부분 수정 가능
  - 이를 자동화 해주는 것이 git

- .git 폴더에 만들어진 파일은 내 컴퓨터에 있음. 

### 중앙 vs 분산
- 중앙 집중식
  - 버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와 다시 중앙에 업로드
  - 각자 수정한 파일을 서버에서 합치는데, 같은 부분을 수정했을 때 합치면 충돌 일어남
  - 각자가 가진 파일이 원본이기 때문
- 분산식
  - 버전을 여러 개의 복제된 저장소에 저장 및 관리
  - 변경사항이 기록되어있는 .git 안의 파일을 내려받으면 관리되고 있는 파일을 똑같이 받을 수 있음
  - 두 사람이 같은 파일을 둘 다 작업했을 때 수정사항을 업로드 하면, 다음 버전으로 넘어갈 때 충돌이 일어나는 것 같지만 이는 원본을 해치는 것이 아니기 때문에 괜찮음(버전만 충돌?되는 상황)
  - 장점
    1. 중앙 서버에 의존하지 않고 동시에 다양한 작업 수행 가능(작업 충돌↓, 개발 생산성↑)
    2. 중앙 서버의 장애/손실에 대비해 백업과 복구 용이
    3. 변경 이력과 코드를 로컬 저장소에 기록하고, 나중에 중앙 서버 동기화하면 되므로 인터넷 연결 안돼있어도 작업 가능

### git의 역할
1. 코드 버전(history) 관리
2. 개발되어 온 과정 파악
3. 이전 버전과의 변경 사항 비교

코드의 **변경 이력**을 기록하고 **협업**을 원활하게 하는 도구

### git의 영역
1. Working Directory: 현재 작업중인 영역
2. Staging Area: 기록 대상 모아놓는 영역. Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
3. Repository: 버전 이력과 파일들이 영구적으로 저장되는 영역(모든 버전commit과 변경 이력이 기록됨)

※ .git 폴더 생성: git으로 관리하기 위한 영역

※ .git으로 관리하는 것은 워킹 디렉토리 안에 폴더가 있는 것 -> SA 폴더 안의 임시 파일들 등록해놓음 -> 변경한 부분들을 버전1 파일에 넣는다(repository) -> v1에 등록하면 SA 폴더 임시 파일들은 사라짐

※ Commit: 변경된 파일들을 저장하는 행위

### git의 동작
- `git init` 로컬 저장소 설정(초기화) -> git의 버전 관리를 시작할 디렉토리에서 진행
  - git 로컬 저장소 내에 또다른 git 로컬 저장소 만들지 말 것!!!
  - git 저장소 안에 git 저장소가 있을 경우 가장 바깥 쪽의 git 저장소가 안쪽의 git저장소의 변경사항을 추적할 수 없기 때문
- `git add` 변경사항이 있는 파일을 staging area에 추가
- `git commit` SA에 있는 파일들을 저장소에 기록 -> 해당 시점 버전 생성하고 변경 이력 남기는 것

### git 기타 명령어
- `git status` 현재 로컬 저장소의 파일 상태 보기
- `git log commit history` 보기
- `git log --oneline` commit목록 한 줄로 보기
- `git config --global -l` git global 설정 정보 보기


## 실습
1. `cd ../..` ~/Desktop/study/00_startcamp/01_git
2. `git init` .git 파일 생성 -> git의 관리를 받기 시작한 디렉토리 내에서는 **(master)** 붙음
3. `ls -a` 현재 작업중인 디렉토리 내부 파일 목록 출력(숨김파일 포함)
4. `git add 00_startcamp/01_git/markdown.md ` markdown.md 파일만 SA에 등록
5. `git status` 상태 출력 -> Changes to be committed:
6. markdown.md 파일 수정
7. `git status` 상태 출력 -> Changes not staged for commit:(너 수정했는데 커밋 안했다)
8. `git add 00_startcamp/01_git/markdown.md`  다시 SA에 등록
9. `git commit -m "마크다운 연습"` version1 등록
10. 등록 하려니 에러 메시지 나옴 -> Author identity unknown 니 누구?
11. 이메일, 이름 등록하자(전역에! 이 컴퓨터에!) ` git config --global user.email "sarangx1227@gmail.com"` , `git config --global user.name "박사랑"`
12. `git config --global --list` 등록 확인
13. `code ~/.gitconfig` 오타났을 시 수정
14. `git commit -m "마크다운 연습"` 다시 등록
15. `git log` 언제 누가 어떤 이름으로 commit 만들었는지 확인
16. `git push -u origin master` push하기

8-1. SA에 실수로 add한 파일이 있다면 `git restore --staged filename`로 삭제

---
### 참고
1. local: 현재 사용자가 직접 접속하고 있는 기기 또는 시스템
2. 원격 저장소: 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장해 여러 개발자가 협업, 코드 공유할 수 있는 저장 공간 -> GitLab, GitHub


## github
1. new
2. repository name 설정
3. public / private
4. 깃허브에서 먼저 저장소를 만들었다면 Add a README file 체크(우리는 study->.git->commit 3개 이미 했음. 즉, local repository 존재하므로 체크X)

### git과 github
```bash
echo "# TIL" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/sweetpotatolove/TIL.git
git push -u origin master
```
- `git remote add origin https://github.com/sweetpotatolove/TIL.git` : git아. 원격 저장소(remote) 추가할건데(add) origin이라 부를 것이며, 주소는 ~ 여기야
  - 주소를 매번 입력하기 힘드니 origin으로 이름 설정

- `git push -u origin master` 입력하면 push안되고 깃허브 로그인 뜸(최초 push시)
  - 아까 설정한 이메일, 이름은 '커밋 작성사 정보(깃)'
  - 이건 깃'허브'에 접근할 수 있는 권한
  - 해당 원격 저장소에 push할 수 있는 권한이 있는지 확인하기 위함!
  - 깃허브 연결 후 다시 입력

- `git pull origin master` 원격 저장소의 변경사항만을 받아옴 - 업데이트

- `git clone 주소` github에 있는 파일 불러오기(원격 저장소 전체를 복제 - 다운로드)
  - `shift + insert` git에서 복사 붙이기
  - clone으로 받은 프로젝트는 이미 git init 되어 있음
  - 해당 프로젝트 처음 받을 때 clone -> 이후엔 변경사항만 다운로드 push

- `git add .` 파일 한번에 SA에 등록

※ 원격 저장소에는 commit이 올라가는 것 -> commit 이력이 없다면 push할 수 없음

※ clone -> add -> commit -> (add commit 반복) -> push

※ (이미 파일 존재) -> pull -> add -> commit -> (add commit 반복) -> push

※ commit 메시지에 뭘 수정했는지 기입할 것

### 참고
- gitlab에서 clone으로 내려받은 파일을 로컬에서 작업하던 폴더에 복사 붙이기 후 해당 파일에 대한 .git 생성하면 문제가 생김
  - 로컬에서 작업하던 폴더의 .git이 존재하는데, 내부에 해당 파일만 관리하는 .git을 만드는 것을 서브모듈이라 함
  - 제대로 사용 못하면 문제 생김
  - 만약 .git이 관리하는 폴더 내부에 파일만 관리하는 .git이 들어간 채 push됐다면?
  - 로컬 폴더에서 보이지 않게한 후 git add . 하여 원격 저장소에 push -> 파일 관리하던 .git 없애고 폴더에 파일만 넣어서 add commit push

- clone으로 내려받은 파일은 로컬 폴더에 **복사 붙이기** (드래그해서 옮기는거XXX)