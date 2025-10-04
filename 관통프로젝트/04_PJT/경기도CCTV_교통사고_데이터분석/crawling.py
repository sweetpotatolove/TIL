import os
import time
import shutil  # 파일 이동/이름 변경을 위해 추가
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException

# --- 1. 다운로드 폴더 설정 (가장 먼저 실행) ---
# 현재 스크립트가 있는 위치에 'downloaded_data' 라는 폴더를 생성하고 그곳에 저장합니다.
DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloaded_data")
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)


def setup_driver():
    """Chrome WebDriver 설정 및 다운로드 폴더 지정"""
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # 다운로드 폴더를 지정하는 옵션 추가
    prefs = {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(options=options)
    return driver


def navigate_to_page(driver):
    """TOPIS 서울교통정보 웹사이트로 이동 및 로딩 대기"""
    driver.get("https://tmacs.kotsa.or.kr/web/TG/TG200/TG2100S/Tg2102.jsp?mid=S1203")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "container")))
    print("페이지에 접속했습니다.")


# --- 2. 파일명 변경 로직이 추가된 함수 ---
def check_alert_and_download(driver, jijace, year):
    """팝업 확인, 다운로드, 파일명 변경 후 상태 반환"""
    time.sleep(0.5)
    try:
        alert = driver.switch_to.alert
        print(f"-> {year}년 데이터 없음. 팝업 발생.")
        alert.accept()
        return 'failed_popup'
    except NoAlertPresentException:
        try:
            # 다운로드 전 현재 폴더의 파일 목록 기록
            before_files = os.listdir(DOWNLOAD_DIR)
            
            download_button = driver.find_element(By.CLASS_NAME, "exbtn")
            download_button.click()
            
            # 다운로드가 완료될 때까지 대기
            waited_time = 0
            while waited_time < 30:
                after_files = os.listdir(DOWNLOAD_DIR)
                new_files = [f for f in after_files if f not in before_files]
                if new_files and not any('.crdownload' in f for f in new_files):
                    downloaded_file = new_files[0]
                    
                    # 파일명 변경
                    new_filename = f"{jijace}_{year}.xlsx"
                    original_path = os.path.join(DOWNLOAD_DIR, downloaded_file)
                    new_path = os.path.join(DOWNLOAD_DIR, new_filename)
                    shutil.move(original_path, new_path)

                    print(f"-> {year}년 데이터 다운로드 성공. 파일명: {new_filename}")
                    return 'success'
                
                time.sleep(1)
                waited_time += 1
            else: # 시간 초과
                print(f"   (경고) {year}년: 파일 다운로드 시간 초과.")
                return 'failed_timeout'

        except NoSuchElementException:
            print(f"   (경고) {year}년: 다운로드 버튼을 찾을 수 없습니다.")
            return 'failed_no_button'
        except Exception as e:
            print(f"   (경고) {year}년: 다운로드 중 예상치 못한 오류 발생: {e}")
            return 'failed_exception'


def select_and_search_by_year(driver):
    """지자체와 연도를 순회하며 데이터 다운로드 및 로그 저장"""
    sido_dropdown = driver.find_element(By.ID, "sido")
    sido_select = Select(sido_dropdown)
    sido_select.select_by_value("41000")
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#jijace > option:nth-child(2)"))
    )
    print("'jijace' 드롭다운 옵션 로딩 완료.")

    download_log = []

    for jijace in jijaces:
        jijace_dropdown = driver.find_element(By.ID, "jijace")
        Select(jijace_dropdown).select_by_value(jijace)
        print(f"\n====== 지자체: {jijace_dict.get(jijace, jijace)} 데이터 조회 시작 ======")
        
        for year in years:
            Select(driver.find_element(By.ID, "std_year")).select_by_value(str(year))
            Select(driver.find_element(By.ID, "end_year")).select_by_value(str(year))
            driver.find_element(By.CLASS_NAME, "btn_primary").click()
            print(f"'{year}'년 조회 클릭.")

            # --- 3. jijace와 year를 함수에 전달 ---
            status = check_alert_and_download(driver, jijace, year)
            
            download_log.append({
                'jijace': jijace,
                'year': year,
                'status': status
            })

    # 최종 크롤링 결과 로그 저장 및 출력
    log_df = pd.DataFrame(download_log)
    print("\n" + "="*50)
    print("             최종 크롤링 결과 로그")
    print("="*50)
    print(log_df)
    
    try:
        log_df.to_csv("crawling_log.csv", encoding='utf-8-sig', index=False)
        print("\n✅ 크롤링 로그를 'crawling_log.csv' 파일로 성공적으로 저장했습니다.")
    except Exception as e:
        print(f"\n❌ 로그 파일 저장 중 오류 발생: {e}")
    
    return log_df


def main():
    """메인 실행 함수"""
    driver = None # finally 블록에서 사용하기 위해 미리 선언
    try:
        driver = setup_driver()
        navigate_to_page(driver)
        select_and_search_by_year(driver)
    except Exception as e:
        print(f"\n크롤링 실행 중 오류가 발생했습니다: {e}")
    finally:
        if driver:
            driver.quit()
            print("\n드라이버를 종료했습니다.")


if __name__ == "__main__":
    jijaces = [
        "41280", "41110", "41460", "41590"
    ]
    years = range(2015, 2025)
    
    jijace_dict = {
        "41280": "고양시",
        "41110": "수원시",
        "41460": "용인시",
        "41590": "화성시"
    }

    main()