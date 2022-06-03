from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
def test_lambdatest_todo_app():
     driver.get("https://www.google.com/")
     Search=driver.find_element(by=By.NAME, value="q")
     Search.send_keys("John")
     time.sleep(3)
     Search.send_keys(Keys.ENTER)
     driver.maximize_window()
     time.sleep(2)
     driver.close()



