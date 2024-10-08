from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

import time



# ChromeDriver 경로 설정

chromedriver_path = "C:/chromedriver.exe"  # 여기에 ChromeDriver의 경로를 입력하세요.





# 브라우저 꺼짐 방지 옵션

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)







# Chrome 드라이버 서비스 설정

service = Service(executable_path=chromedriver_path)



# Chrome 드라이버 설정

driver = webdriver.Chrome(service=service,options=chrome_options)



# 웹 페이지 열기

url = "https://www.gojobs.go.kr/sysLogin.do"  # 여기에 크롤링할 웹 페이지의 URL을 입력하세요.

driver.get(url)



time.sleep(3)



ID = driver.find_element(By.ID, "usid")

ID.send_keys("실제 내 아이디 ")   # 내 실제아이디 치기



PW = driver.find_element(By.ID, "password")

PW.send_keys("실제 내 비번")   #내 실제 비번 치기 



login_button = driver.find_element(By.CSS_SELECTOR,"button.btn_login")

login_button.click()



time.sleep(3)





# 그냥은 요소 클릭이 안돼서 자바스크립트를 이용하여 요소를 클릭하기 

element = driver.find_element(By.XPATH, "//a[contains(text(), '인사교류센터')]")

driver.execute_script("arguments[0].click();", element)




# 페이지 끝까지 스크롤하기

scroll_pause_time = 1  # 스크롤 후 대기 시간 (초)



last_height = driver.execute_script("return document.body.scrollHeight")



while True:

    # 페이지의 끝까지 스크롤 다운

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")



    # 페이지가 로딩될 시간을 기다림

    time.sleep(scroll_pause_time)



    # 새로운 페이지 높이를 계산

    new_height = driver.execute_script("return document.body.scrollHeight")

    

    # 새로운 높이가 이전과 같으면 스크롤이 끝난 것임

    if new_height == last_height:

        break



    last_height = new_height





    

elements = driver.find_elements(By.CSS_SELECTOR, 'a[href^="javascript:fn_mtchgView("]')



my_list = []



for i in elements:

    my_list.append(i.text)


# 그룹의 크기

group_size = 5



# 각 그룹의 첫 번째 요소를 뽑기

신청자직급 = [my_list[i] for i in range(0, len(my_list), group_size)]


신청일자 = [my_list[i + 1] for i in range(0, len(my_list), group_size) if i + 1 < len(my_list)]


신청자근무지 = third_elements = [my_list[i + 2] for i in range(0, len(my_list), group_size) if i + 2 < len(my_list)]


신청자현재기관 = [my_list[i + 3] for i in range(0, len(my_list), group_size) if i + 3 < len(my_list)]


희망기관 = [my_list[i + 4] for i in range(0, len(my_list), group_size) if i + 4 < len(my_list)]



import pandas as pd



# 데이터프레임 생성

data = {

    '신청자직급': 신청자직급,

    '신청일자': 신청일자,

    '신청자근무지': 신청자근무지,

    '신청자현재기관': 신청자현재기관,

    '희망기관': 희망기관

}


df = pd.DataFrame(data)


df.to_csv("output.csv",encoding='utf-8-sig')