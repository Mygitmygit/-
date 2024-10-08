from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
import pandas as pd 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# ChromeDriver 경로 설정
chrome_driver_path = "C:/chromedriver.exe"


# Service 객체를 사용해 ChromeDriver 실행 (detach 옵션 포함)
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # 브라우저가 닫히지 않도록 설정
browser = webdriver.Chrome(service=service, options=options)


# 네이버쇼핑 웹사이트 열기
browser.get('https://shopping.naver.com/home')


# 로딩이 끝날 때까지 기다림 (암시적 대기)
browser.implicitly_wait(3)  # 요소가 나타날 때까지 최대 5초 대기


# 요소를 찾기 
search_box = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='input_text']"))
)
search_box.send_keys("쌀")


""" 
# 검색어 입력 
search_box.send_keys("네이버웹툰")


# 검색 실행 (엔터 키 입력)
search_box.send_keys(Keys.ENTER)

time.sleep(2)

element = browser.find_element(By.CSS_SELECTOR, "a.l")

element.click()

time.sleep(2)

#"태그명.클래스명" 으로 선택하려했으나 동일한 "태그명.클래스명" 을 갖는 놈들이 너무 많아 일단 모두 불러온다.(elements 를 써서)
elements = browser.find_elements(By.CSS_SELECTOR,"a.SubNavigationBar__link--PXX5B")

#그 후에 내가 원하는 elements 들 중에서 3번째에 위치하는 요소(화요웹툰) 클릭. (인덱스로는 2)
elements[2].click()



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


# 웹툰 제목 전부 선택 
titles = browser.find_elements(By.CSS_SELECTOR,"span.text")
# 각 제목의 텍스트 정보만 가져와서 리스트로 변환
title_list = [title.text for title in titles]
title_list = title_list[::2]  #약간의 튜닝 (홀수번째 요소만 선택 )


# 웹툰 작가 전부 선택 
authors = browser.find_elements(By.CSS_SELECTOR,"a.ContentAuthor__author--CTAAP")
# 각 작가의 텍스트 정보만 가져와서 리스트로 변환
author_list = [author.text for author in authors]

print(title_list)



# 리스트를 합쳐서 데이터프레임으로 만들기 

df = pd.DataFrame({
    '웹툰제목': pd.Series(title_list),  
    '작가': pd.Series(author_list)   
})



df.to_csv("output.csv")


"""