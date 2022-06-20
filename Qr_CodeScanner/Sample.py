import os
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='./chromedriver.exe')


def test_whatsapp_test_app():
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://web.whatsapp.com/")
    time.sleep(11)
    res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=8))
    QR_CODE = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/div')
    time.sleep(3)
    QR_CODE.screenshot('qr_codes_wtsapp/'+res + '.png')
    driver.delete_all_cookies()
    driver.back()
    driver.quit()
