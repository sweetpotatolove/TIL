# git
분산 버전 관리 시스템

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
  - 두 사람이 같은 파일을 둘 다 작업했을 때 수정사항을 업로드 하면, 다음 버전으로 넘어갈 때 충돌이 일어나는 것 같지만 이는 원본을 해치는 것이 아니기 때문에 괜찮음(버전이 충돌?되는 상황)

### git의 영역
1. Working Directory: 현재 작업중인 영역
2. Staging Area: 기록 대상 모아놓는 영역. Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
3. Repository: 버전 이력과 파일들이 영구적으로 저장되는 영역

※ .git 폴더 생성: git으로 관리하기 위한 영역

※ .git으로 관리하는 것은 워킹 디렉토리 안에 폴더가 있는 것 -> SA 폴더 안의 임시 파일들 등록해놓음 -> 변경한 부분들을 버전1 파일에 넣는다(repository) -> v1에 등록하면 SA 폴더 임시 파일들은 사라짐

※ Commit: 변경된 파일들을 저장하는 행위

## 실습
1. `cd ../..` ~/Desktop/study/00_startcamp/01_git
2. `git init` .git 파일 생성 -> (master) 붙음
3. `ls -a` 
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

8-1. SA에 실수로 add한 파일이 있다면 `git restore --staged filename`로 삭제

---
### 참고
1. local: 현재 사용자가 직접 접속하고 있는 기기 또는 시스템
2. 원격 저장소: 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장해 여러 개발자가 협업, 코드 공유할 수 있는 저장 공간 -> GitLab, GitHub


## github

2. repository name 설정
3. public / private
4. 깃허브에서 먼저 저장소를 만들었다면 Add a README file 체크(우리는 study->.git->commit 3개 이미 했음. 즉, local repository 존재하므로 체크X)

```
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

- `git push -u origin master` 입력하면 push안되고 깃허브 로그인 뜸
  - 아까 설정한 이메일, 이름은 '커밋 작성사 정보(깃)'
  - 이건 깃'허브'에 접근할 수 있는 권한
  - 깃허브 연결 후 다시 입력

- `git add .` 파일 한번에 SA에 등록
