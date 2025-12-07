from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com") 

time.sleep(2)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("HELLO")


time.sleep(10)
driver.quit()