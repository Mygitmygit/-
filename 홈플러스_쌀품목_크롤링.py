from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
import pandas as pd 



# ChromeDriver 경로 설정
chrome_driver_path = "C:/chromedriver.exe"


# Service 객체를 사용해 ChromeDriver 실행 (detach 옵션 포함)
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # 브라우저가 닫히지 않도록 설정
browser = webdriver.Chrome(service=service, options=options)


# 웹사이트 열기
browser.get('https://mfront.homeplus.co.kr/')


# 로딩이 끝날 때까지 기다림 (암시적 대기)
browser.implicitly_wait(3)  # 요소가 나타날 때까지 최대 3초 대기


# 찾기 
search_box = browser.find_element(By.CSS_SELECTOR, "input.wordInput.css-r4ghzr")

# 클릭 
search_box.click()



# 검색어 입력
search_box.send_keys("쌀")

# 엔터 입력 
search_box.send_keys(Keys.ENTER)

"""
# 다 내려갈때까지 무한으로 스크롤 밑으로 내리기 
before_h = browser.execute_script("return window.scrollY")


while True:
    browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)
    time.sleep(2)
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h 


time.sleep(5)

"""

# 스크롤 10번 밑으로 내리기 ---------------------------
max_scrolls = 10
scroll_count = 0

before_h = browser.execute_script("return window.scrollY")

while scroll_count < max_scrolls:
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    time.sleep(2)
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break  

    before_h = after_h
    scroll_count += 1  
#------------------------------------------------------

# 스크롤을 내린 후 모든 데이터가 로딩될떄까지 10초 기다린다. 
time.sleep(10)


# 제품 정보를 담을 리스트 준비 
data = []  

#쌍으로 크롤링하기-----------------------------------------------------------------------------
products = browser.find_elements(By.CSS_SELECTOR, "div.detailInfo")  

for product in products:
    # 각 제품에서 제품명과 가격 추출
    name = product.find_element(By.CSS_SELECTOR, "p.css-xktqki").text  # 제품명
    price = product.find_element(By.CSS_SELECTOR, "strong.priceValue").text  # 가격
    data.append({
        '제품명': name,
        '가격': price
    })
#-----------------------------------------------------------------------------------------



# 데이터프레임 생성
df = pd.DataFrame(data)

df.to_csv("홈플러스에서_크롤링한_쌀품목.csv")



