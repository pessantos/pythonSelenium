import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

#Navegação

browser.maximize_window()
browser.get("https://saucedemo.com")

#Finding elements

username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")

#Sending keys
username.send_keys("standard_user")
password.send_keys("secret_sauce")



browser.get_screenshot_as_file("Evidences/screenshot.png")

time.sleep(3)
browser.quit()



