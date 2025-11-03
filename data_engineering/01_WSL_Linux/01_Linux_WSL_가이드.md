# WSL Ubuntu 설정 가이드

## 1. 필수 Windows 기능 활성화
**(PowerShell을 관리자 권한으로 실행, 이미 설정된 경우 생략)**

```powershell
# WSL 설치
wsl --install

# Windows 기능 활성화
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# WSL 2를 기본으로 설정
wsl --set-default-version 2
```
- 위 명령어 실행 후 **Windows 재부팅 필요**
- Windows 검색창 → **Windows 기능 켜기/끄기** → 아래 항목 모두 체크
  - **Linux용 Windows 하위 시스템**
  - **Virtual Machine Platform**


## 2. Ubuntu (WSL 2용 리눅스 배포판) 설치

### 2-1. Microsoft Store에서 설치
1. **Microsoft Store 실행**
2. `Ubuntu` 검색 → **Ubuntu 22.04 LTS** 선택
3. **[설치]** 버튼 클릭
4. 설치 완료 후 **Ubuntu 실행 → 사용자 이름 및 비밀번호 설정**
   - 예)
     - 사용자 이름: `ssafy`
     - 비밀번호: `ssafy`

```powershell
# 설치 후 Ubuntu를 기본 배포판으로 설정
wsl --set-default Ubuntu-22.04
```

### 2-2. 만약 기존 Ubuntu WSL 환경 삭제 후 재설치 (필요한 경우)

```bash
# 설치된 WSL 배포판 목록 확인
wsl --list --verbose

# 기존 Ubuntu 종료 및 삭제가 필요한 경우
wsl --terminate Ubuntu-24.04
wsl --unregister Ubuntu-24.04

# Windows에서 앱 자체 제거
Get-AppxPackage *Ubuntu* | Remove-AppxPackage
```


## 3. VS Code에서 WSL Ubuntu 개발 환경 연결

1. **VS Code 실행 후 Extension 설치**
   - `WSL` 검색 → 설치
2. `Ctrl + Shift + P` → `WSL` 입력
3. **WSL: Connect to WSL in New Window** 선택 → 리눅스 환경에서 코드 편집 가능


## 4. root 사용자로 전환하는 방법

```bash
sudo -i      # root 권한으로 전환 (비밀번호: ssafy)
exit         # 다시 기존 ssafy 계정으로 복귀
```


## 5. chmod (Change Mode) 실습

### 5-1. 간단한 실행권한 부여

```bash
# 빈 파일 생성 후 내용 추가
touch sample.sh
echo 'echo "Hello, Linux!"' > sample.sh
cat sample.sh

# 실행권한 추가
chmod +x sample.sh

# 실행
./sample.sh
```


## 6. 간이 로그 확인 실습

### 6-1. 작업 디렉토리 생성 및 로그 작성

```bash
ls                # 현재 디렉토리 상태 확인
pwd               # 현재 디렉토리 위치 확인
mkdir my_ssafy_project
cd my_ssafy_project

# 더미 로그 생성
touch system.log
echo "INFO: 시스템 시작" >> system.log
echo "ERROR: 데이터베이스 연결 실패" >> system.log
echo "INFO: 유저 로그인" >> system.log
echo "WARNING: 디스크 공간 부족" >> system.log
echo "ERROR: 서비스 중단" >> system.log
```

### 6-2. 로그 확인

```bash
vi system.log         # vi로 파일 내용 확인 (Esc → :q로 종료)
cat system.log        # 전체 내용 보기
head -n 3 system.log  # 처음 3줄만 보기
tail -n 2 system.log  # 마지막 2줄만 보기
grep ERROR system.log # "ERROR" 포함된 로그만 보기
```

### 6-3. 로그 백업 및 파일 이동

```bash
cp system.log backup.log  # 백업 파일 생성
mv backup.log old.log     # 파일 이름 변경
ls -l                     # 파일 목록 확인

rm old.log                # old.log 삭제

mkdir archive             # archive 디렉토리 생성
mv system.log archive/    # system.log을 archive로 이동
rmdir archive             # 실패 (내용이 있어 삭제 불가)
rm archive/system.log     # 내용 삭제 후
rmdir archive             # 디렉토리 삭제 가능 (rm -rf archive를 활용하면 바로 강제 삭제)
```

### 6-4. vi로 파일 작성

```bash
touch system.log
vi system.log

# vi 편집
i                                   # 입력 모드 전환
[INFO] System initialized at 10:23:01
[WARNING] Disk space low
[ERROR] Failed to load configuration
:wq                                 # 저장 후 종료
```

---

## 7. 파일 권한 및 프로세스 확인

### 7-1. 파일 권한 변경

```bash
ls -l system.log       # 현재 권한 확인
chmod 700 system.log   # 권한 변경 (소유자만 읽기/쓰기/실행 가능)
ls -l system.log
```

### 7-2. 프로세스 확인 및 종료

```bash
ps aux | grep bash     # bash 프로세스 확인
kill [PID]             # PID로 프로세스 종료 (주의: 현재 셸 종료 시 로그아웃됨)
```

---

## 8. 기타 명령어

```bash
history                # 입력했던 명령어 기록
history | grep vi      # vi 관련 명령어만 필터링
clear                  # 터미널 창 정리
man [명령어]           # 명령어 매뉴얼 보기 (예: man grep)
```
---