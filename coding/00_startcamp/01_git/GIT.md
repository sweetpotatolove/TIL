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
  - 두 사람이 같은 파일을 둘 다 작업했을 때 수정사항을 업로드 하면, 다음 버전으로 넘어갈 때 충돌이 일어나는 것 같지만 이는 원본을 해치는 것이 아니기 때문에 괜찮음(버전만 충돌되는 상황)
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

※ .git 폴더 생성 == git으로 관리하기 위한 영역 생김

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
- `git log` commit history 보기
- `git log --oneline` commit 목록 한 줄로 보기
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
11. 이메일, 이름 등록하자(전역에! 이 컴퓨터에!) `git config --global user.email "sarangx1227@gmail.com"` , `git config --global user.name "박사랑"`
12. `git config --global --list` 등록 확인
13. `code ~/.gitconfig` 이메일, 이름에 오타났을 시 수정
14. `git commit -m "마크다운 연습"` 다시 등록
15. `git log` 언제 누가 어떤 이름으로 commit 만들었는지 확인
16. `git push -u origin master` push하기

8-1. SA에 실수로 add한 파일이 있다면 `git restore --staged filename`로 삭제

16-1. **-u** 의 의미: 지정된 원격 브랜치(현재 origin master)에 로컬 브랜치(현재 master)로 git push, git pull만 해도 원격 브랜치로 push되게 하겠다는 의미


### 참고
1. local: 현재 사용자가 직접 접속하고 있는 기기 또는 시스템
2. 원격 저장소: 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장해 여러 개발자가 협업, 코드 공유할 수 있는 저장 공간 -> GitLab, GitHub


## github
1. new repository
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
  - 아까 설정한 이메일, 이름은 '커밋 작성자 정보(깃)'
  - 이건 깃'허브'에 접근할 수 있는 권한
  - 해당 원격 저장소에 push할 수 있는 권한이 있는지 확인하기 위함!
  - 깃허브 연결 후 다시 입력

- `git pull origin master` 원격 저장소의 변경사항만을 받아옴 - 업데이트

- `git clone 주소` github에 있는 파일 불러오기(원격 저장소 전체를 복제 - 다운로드)
  - `shift + insert` git에서 복사 붙이기
  - clone으로 받은 프로젝트는 이미 git init 되어 있음
  - 해당 프로젝트 처음 받을 때 clone -> 이후엔 변경사항만 다운로드 pull

- `git add .` 파일 한꺼번에 SA에 등록

※ 원격 저장소에는 commit이 올라가는 것 -> commit 이력이 없다면 push할 수 없음

※ clone -> add -> commit -> (add commit 반복) -> push

※ (이미 파일 존재) -> pull -> add -> commit -> (add commit 반복) -> push

※ commit 메시지에 뭘 수정했는지 기입할 것

### 참고
- gitlab에서 clone으로 내려받은 파일을 로컬에서 작업하던 폴더에 복사 붙이기 후 해당 파일에 대한 .git 생성하면 문제가 생김
  - 로컬에서 작업하던 폴더의 .git이 존재하는데, 내부에 해당 파일만 관리하는 .git을 만드는 것을 submodule 이라 함
  - 제대로 사용 못하면 문제 생김
  - 만약 .git이 관리하는 폴더 내부에 파일만 관리하는 .git이 들어간 채 push됐다면?
  - 로컬 폴더에서 보이지 않게한 후 git add . 하여 원격 저장소에 push -> 파일 관리하던 .git 없애고 폴더에 파일만 넣어서 add commit push

- clone으로 내려받은 파일은 로컬 폴더에 **복사 붙이기** (드래그해서 옮기는거XXX)

- 파일 만들고 add 하지 않은 채 commit 했다면? 메모장 메시지 화면(vim)가 뜸
  - `:q` 눌러서 나가기

- 원격 저장소의 commit 내역과 로컬 저장소의 commit 내용이 다르다면? **push** 불가능
  - git pull 하면 원격 저장소 내용을 로컬로 가져옴(commit 하나 추가하는 것임. 이때의 commit은 원격의 commit과 로컬의 수정 사항이 반영된 commit이 생성됨)
  - 그럼 vim 창이 뜨는데, `:q`로 나가기 하면 됨


## branch
여러 명이 **작업 공간을 나누어** 독립적으로 작업할 수 있도록 도와주는 Git 도구

- 장점
  1. 완전히 독립된 개발 환경 형성 -> 원본(master)에 대해 안전
  2. 하나의 작업은 하나의 브랜치로 나누어 진행하므로 체계적인 협업 및 개발 가능
  3. 손쉽게 브랜치 생성, 브랜치 사이를 이동할 수 있음

### 순서
- `git init` .git 생성
- `touch settings.py` 파일 생성
- `git add settings.py` 파이썬 파일 생성
- `git commit -m "초기설정"` 변경사항 커밋
- `git branch -c sweetpotato/login` sweetpotato/login 이름의 브랜치 생성
  - 브랜치 이름은 '담당자/담당업무'로 설정하는 것이 일반적
- `git branch` 
  - ```
    * master
    sweetpotato/login
    ```
    -> 기존에 있던 master와 고구마가 로그인 만들거라는 브랜치 생김(*로 현재 브랜치 확인)
- `git switch sweetpotato/login` (master) -> (sweetpotato/login)으로 바뀌며 고구마 브랜치에 setting.py 복사됨
- 고구마 브랜치에 `touch login.py` 파일 생성 후 `git add .`  `git commit -m "수정"`
- `git switch master` (sweetpotato/login) -> (master)로 다시 변경하면 폴더에 login 안보이고 setting만 있음
- `git merge sweetpotato/login` 하면 master 계정에서도 login.py가 보인다!
- 다른 브랜치 만들어서 파일 만들었을 때 여러 브랜치를 merge하는 경우 vim이 뜸
  - 1번 branch에서 만든 파일1
  - 2번 branch에서 만든 파일2
  - 1번 브랜치에선 파일2가 안보이고, 2번 브랜치에선 파일1이 안보임
  - master에서 merge할 때 파일1을 받을 땐 문제 없음
  - 파일1을 받고 파일2를 받으려니 2번 branch에는 파일1의 정보가 없는 상태
  - 그래서 파일1에 대한 설명을 vim으로 슥슥 해주는거
  - `:q`로 나가면 됨

- merge 2종류
  - Fast-forward: ex. 위에서 파일1 받아오는 상황(바로 받아짐)
  - 3-way: ex. 위에서 파일2 받아오는 상황(2번 브랜치에 파일1이 없는데 파일1,파일2를 합치려니까 vim 등장)

- `git branch -d sweetpotato/login` 브랜치 삭제

### gitlab에 레포 생성하는 방법
- 팀장의 경우
  1. gitlab -> new project -> create blank project -> 프로젝트 이름 설정 -> Project URL에 내 이름 눌러야함 -> Initialize repository with a README 체크 (readme.md 파일이 만들어 졌다는 것은 파일이 들어있는 레포가 만들어져서 .git이 관리는 것까지 설정되었다는 뜻)
  2. Manage -> Members -> invite members -> 초대할 멤버 이름 입력 + 게스트 말고 Maintainer로 초대해야 함

- 팀원인 경우
  1. 팀장이 만든 레포 -> clone으로 받아오기
  2. 그 폴더의 git에서 `git branch -c sarang`으로 생성
  3. `git switch sarang`하여 해당 브랜치로 작업

### gitlab에 레포 삭제하는 방법
settings -> general -> Advanced -> delete -> 파일 이름 그대로 입력 

### 서로 다른 branch의 작업물 가져오는 방법
1. `git push origin sarang` : 내가 commit한 것을 다른 사람이 받아가려면 원격 저장소(origin(원격저장소 별명))를 통해 push해놔야 함
2. 원격 저장소에 개별 branch에서 작업한 것 저장됨
3. merge requests -> new merge request 합병 요청 보내기
4. source branch : **sarang** (**내**가 작업한 것을) Target branch : **master** (마스터에게 보낸다(마스터 말고 다른 브랜치에 보내려면 수정해야함))
5. 팀장이 각각 merge 누름 -> 원격 저장소에 합병됨
6. git pull해서 로컬에서도 병합된거 받게 함
7. (작업 끝났으면) 개인 브랜치 삭제

### 서로 다른 branch에서 같은 파일의 같은 줄을 수정했을 때
- VS Code 등 로컬 환경에서 Git 명령어로 병합하는 과정
  1. A, B가 같은 파일을 각자 수정함
  2. A가 팀장에게 merge 요청 -> 팀장이 merge
  3. B도 팀장에게 merge 요청 -> 팀장이 merge 시도

      -> 같은 파일의 같은 줄을 수정해서 충돌 발생

      -> 이때 Git은 병합 중단하고, 병합을 시도한 사람(팀장)의 로컬 master 브랜치를 (master|MERGING) 상태로 만듦

      -> (master MERGING) : 마스터가 merge과정에서 문제가 생겼다는 표시

      ※ (master MERGING)은 git이 병합 중이라는 표시로, 충돌 해결될 때까지 커밋 못하게 보호하는 상태

  4. Accept Current Change, Accept Incoming Change, Accept Both Changes, Compare Changes 중 선택
  5. 수정이 됐으니 add & commit `git add .` `git commit -m "A작업과 B작업 merge하였음"`

      -> A, B가 수정한 파일을 합칠 때 commit 해야함(A, B가 합쳐진 버전의 파일이 없으니까), 수정한 파일이 안겹치면 컴퓨터가 알아서 두 파일이 합쳐진 새 파일 만듦(알아서 버전 생성)

      -> 그런데 A, B가 수정한 파일이 같은 파일이라면 컴퓨터가 알아서 병합할 수 없는 상황이 벌어짐

      -> 그래서 수정하라고 선택지 4개 나오는 것임

  6. A, B는 `git merge master`를 통해 master에 합쳐진 A,B 작업을 자신의 브랜치로 가져올 수 있음

- GitLab에서 Merge Request 병합을 시도하는 과정  
  1. gitlab에서 A꺼 먼저 merge하면 A의 작업물이 master에 합쳐짐
  2. 다음 B꺼 merge하면 merge버튼 사라지고 conflicts(충돌) 메시지 생김
      - ① Resolve locally 로컬에서 작업할래? ② Resolve confilicts 여기서 작업할래?
  3. 충돌이 일어났음을 B에게 알리고, B의 로컬에서 수정 -> 다시 merge request 하라고 하자

※ 왜 gitlab에서 하지 않고 로컬에서 수정하는 걸까?

    -> git branch 구성을 보면, A의 로컬에는 master(origin master를 기준으로 clone 받은 기본 브랜치)와 a(A가 작업 중인 브랜치)가 존재
    
    -> B또한 로컬에는 master, B 두 개의 브랜치가 있고 원격에는 origin master가 있음

    -> B가 b 브랜치로 원격의 마스터에 push해서 merge하려고 하는데 conflict 발생하는 것

    -> 왜? origin master는 A 작업물까지 merge된 최신 버전인데, b 브랜치는 origin master의 최신 내용을 모름(B의 로컬 master는 구버전)

    -> A 작업물과 B 작업물을 모두 merge한 commit을 만들어야 하는데, 그게 gitlab 페이지에서는 힘듦

    -> 때문에 `git pull origin master`을 통해 B의 로컬 master를 일단 최신화 하자(그럼 A 작업물이 로컬에 들어왔을 것임)

    -> master에서 지금까지 `git merge A` 이런식으로 했는데, 우리는 B는 마스터가 아니므로 **마스터가 가진 내용 가져와서 본인(B)꺼에 merge**하면 됨

    -> 즉, `git merge master`로 현재 브랜치 b에 master와 merge 시도

    -> 그럼 B 환경에서 충돌 발생했을 때 나오는 선택지 4개 나옴

    -> VS code에서 충돌 해결 후 `git add .` , `git commit -m ""` , `git push origin b`

    -> 또는!!

    -> `git pull origin master`로 원격 마스터의 내용을 b 브랜치가 바로 가져가서 merge(B 로컬에서)

    -> 충돌 발생하면 vs code에서 해결 후 git add. git commit -m "" git push

    -> 로컬 마스터도 원격 마스터꺼 받아와야 하니까 로컬 마스터가 git pull하면 진짜 끝

- 실제 팀플할 땐 로컬 master 브랜치에 직접 합치지 않고, 별도의 합병용 브랜치(develop 등) 생성해서 사용함
- 즉, master 브랜치는 배포용으로만 유지. 실제 개발은 중간 브랜치로 관리
  1. master 브랜치는 아무도 수정하지 않는다.
  2. master 브랜치는 최초 설정 (모든 팀원이 함께 쓸 내용 생성시에만 사용)
      - git add, git commit, push까지 모두 진행
      - master 브랜치의 초기 상태를 원격 저장소에 올리는 전 과정 진행
  3. develop (혹은 dev) 브랜치를 생성한다

※ 팀장의 역할: 팀원들의 작업물을 비교해 보는 사람으로써 merge 충돌 시 어떻게 합칠지 결정하고, 누구한테 어떻게 수정하라고 명령하는 역할을 수행함


## branch 실습
1. 팀장이 새 래포 생성
2. 팀원 초대
3. 팀장은 clone 받은 뒤, develop 브랜치 생성, setting.py 만들어서 push한다(단, merge request 하지 않는다) `git push origin develop`
4. 팀원은 master를 클론 받은 뒤, 로컬에서 develop 브랜치 생성하고, develop 브랜치에서 git pull origin develop 진행한다
5. 그 후 개인 브랜치 생성한다. 개인 브랜치에서 settimgs.py 수정 또는 새 파일 생성하고, push origin 개인브랜치, merge request 수행
6. 팀장은 팀원이 MR 남겼다고 하면, merge를 develop에 시도한다
6-1. 시도해서 성공하면? merge 완료했다고 알리고 하던일 마저한다.
6-2. 시도해서 실패하면? MR 보낸 사람에게 conflict 해결하고 다시 MR 보내라고 한다 `git switch develop` `git pull` `git switch 내 브랜치` `git merge develop` (기왕이면 어디서 문제 발생했는지 알려주기)
7. 팀원 1 혹은 2는 MR발생 후, 팀장이 merge 했다고 알리면, 본인은 브랜치에서 `git pull origin develop`해서, 추가 작업 진행하거나 develop 브랜치에서 pull 받은 뒤, 본인 브랜치에서 merge develop을 한다

