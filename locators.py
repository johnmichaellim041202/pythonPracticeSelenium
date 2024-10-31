from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service

#-- Chrome
from  selenium.webdriver.common.by import By

import time


#"C:\Users\NCTV_User_002\Documents\chromedriver-win64\chromedriver.exe"
service_obj = Service("/Users/NCTV_User_002/Documents/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Classname, name, linkText
# By Name > name
driver.find_element(By.NAME, "name").send_keys("Baguette")
# By Name > email
driver.find_element(By.NAME, "email").send_keys("kys@gmail.com")
# By ID > password
driver.find_element(By.ID, "exampleInputPassword1").send_keys("password")
# By ID > clickCheckbutton to see password
driver.find_element(By.ID, "exampleCheck1").click()


time.sleep(5)