from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service

#-- Chrome
from  selenium.webdriver.common.by import By

import time


#"C:\Users\NCTV_User_002\Documents\chromedriver-win64\chromedriver.exe"
service_obj = Service("/Users/NCTV_User_002/Documents/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

#The website to use
driver.get("https://rahulshettyacademy.com/client")

#Maximize to fullscreen
driver.maximize_window()
time.sleep(2)
# By Link Text > Forgot password
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

#By CSS SELECTOR > input email address
#driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your email address']").send_keys("kys@gmail.com")

#parent travel //parent[indexes]/tagname[indexes]/childtag[indexes]
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("kys@gmail.com")

# CSS SELECTOR > password
#parent travel = parent[indexes]_tagname:nth-child(indexes)_childtag[indexes]
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("password")

driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("password")

# //button[text()='Save New Password']
driver.find_element(By.XPATH, "//button[@type='submit']").click()



time.sleep(4)