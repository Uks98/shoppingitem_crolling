from lib2to3.pgen2 import driver
from random import random
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
# 어떤 엘리먼트가 나올때 까지 기다리는데 기다리는 조건을 넣을 수 있다.
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
import pyautogui
import pyperclip
import random

browser = webdriver.Chrome('c:/chromedriver.exe')
#browser.maximize_window()
browser.get("https://www.naver.com/")
browser.implicitly_wait(10) #로딩이 될때까지 10초기다림
#쇼핑메뉴클릭
browser.find_element(By.CSS_SELECTOR,"a.nav.shop").click()
browser.implicitly_wait(time_to_wait=2)
#검색하기
selector = pyautogui.prompt("검색어를 입력해주세요")
search = browser.find_element(By.CSS_SELECTOR,"._searchInput_search_input_QXUFf")
search.click()
browser.implicitly_wait(time_to_wait=2)
search.send_keys(selector)
#pyautogui.write(selector,interval=0.15)
pyautogui.press("Enter")

#무한 스크롤

#스크롤 전 높이
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 끝까지 스크롤
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 대기 1초 (로딩으로 인해 알맞는 초 조절)
    browser.implicitly_wait(time_to_wait=1)

    # 스크롤 길이 비교로 끝까지 갔는지 확인
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#엑셀 저장
f = open(f"C:\python_file\py_item_crolling\csv123_file\{selector}.csv",'w',encoding='CP949',newline='')
    
   

#상품정보 div
items = browser.find_elements(By.CSS_SELECTOR,".basicList_info_area__TWvzp")
csv_writer = csv.writer(f)

for item in items:
    name = item.find_element(By.CSS_SELECTOR,".basicList_title__VfX3c").text
    try:
        price = item.find_element(By.CSS_SELECTOR,".price_num__S2p_v").text
    except:
        price = "empty price"
    link = item.find_element(By.CSS_SELECTOR,".basicList_title__VfX3c > a").get_attribute("href")
    print(name,price,link)
    csv_writer.writerow([name,price,link])
browser.close()
f.close()
