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
driver.get("https://rahulshettyacademy.com/angularpractice/")

#Maximize to fullscreen
driver.maximize_window()

# ID, Xpath, CSSSelector, Classname, name, linkText
# By Name > name
driver.find_element(By.NAME, "name").send_keys("Baguette")
# By Name > email
driver.find_element(By.NAME, "email").send_keys("kys@gmail.com")
# By ID > password
driver.find_element(By.ID, "exampleInputPassword1").send_keys("password")
# By ID > clickCheckbutton to check the checkBox
driver.find_element(By.ID, "exampleCheck1").click()
# By CSS SELECTOR
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
time.sleep(4)

# to scroll down the webpage
driver.execute_script('window.scrollBy(0, 1000)')

# XPATH = //tagname[@attributes='value'] -> //input[@type='submit']
# CSS = tagname[@attributes='value'] -> //input[@type='submit']
# By XPATH > //input[@value='Submit'] to click the Submit button
driver.find_element(By.XPATH, "//input[@value='Submit']").click()

# By XPATH > Two Way Data Binding example
driver.find_element(By.XPATH, "//input[@class='ng-untouched ng-pristine ng-valid']").send_keys(" ayaw sa")

# Clear but specified the value = (//tagname[@attribute='value'])[indexes]
driver.find_element(By.CSS_SELECTOR, "(//input[@type='text'])[3]").clear()
time.sleep(5)


# By CLASS NAME > alert-success to see the message prompt
message = driver.find_element(By.CLASS_NAME, "alert-success").text
#print the message if its success
print(message)

time.sleep(5)