## Python 가상환경 구성 (앞으로 다룰 모든 python 패키지는 여기서 통일합니다.)

### Python 3.10 설치용 PPA 추가
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

### Python 3.10 및 venv 설치
sudo apt install -y python3.10 python3.10-venv python3.10-distutils

### 가상환경 생성 및 활성화()
python3.10 -m venv ~/data_env
source ~/data_env/bin/activate

### Python 버전 확인
python --version  # Python 3.10.x

pip install -r requirements.txt
