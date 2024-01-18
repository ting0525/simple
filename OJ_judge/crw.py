from selenium import webdriver
## BY: 也就是依照條件尋找元素中XPATH、CLASS NAME、ID、CSS選擇器等都會用到的Library
from selenium.webdriver.common.by import By
## keys: 鍵盤相關的Library
from selenium.webdriver.common.keys import Keys
## Select: 下拉選單相關支援，但前端框架UI工具不適用(ex: Quasar、ElementUI、Bootstrap)
from selenium.webdriver.support.ui import Select
## WebDriverWait: 等待頁面加載完成的顯性等待機制Library
from selenium.webdriver.support.ui import WebDriverWait
## ActionChains: 滑鼠事件相關
from selenium.webdriver.common.action_chains import ActionChains
## expected_conditions: 條件相關
from selenium.webdriver.support import expected_conditions as EC
## BeautifulReport: 產生自動測試報告套件
from BeautifulReport import BeautifulReport
## Chrome WebDriver 需要DRIVER Manager的支援
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
import pandas as pd
import numpy as np


driver = webdriver.Chrome()

class crawler:
    def __init__(self, debug = True):
        self.debug = debug

    def login(self) -> None:
        driver.get('https://oj.zxzinn.com/')
        time.sleep(1)
        login_button = driver.find_element(By.XPATH, "//*[@id='header']/ul/div[2]/button[1]")
        login_button.click()
        time.sleep(1)
        input_username = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/form/div[1]/div/div/input")
        input_username.send_keys("root")
        input_password = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/form/div[2]/div/div/input")
        input_password.send_keys("fju@@123")
        submit_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/button")
        submit_button.click()

    def crawling(self, student_number):
        self.login()
        AC_list = []
        for i in range(len(student_number)):
        #for i in range(3):
            time.sleep(1)
            url = f'https://oj.zxzinn.com/user-home?username={student_number[i]}'
            driver.get(url)
            time.sleep(1)
            AC_elements = driver.find_elements(By.XPATH, "//*[@class='ivu-btn ivu-btn-ghost']")
            AC_values = [element.text for element in AC_elements]
            AC_list.append(AC_values)
        return AC_list
        
        

