import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

#Navegação

browser.maximize_window()
browser.get("https://demo.applitools.com")

#Finding elements

username = browser.find_element(By.ID, "username")
checkbox = browser.find_element(By.XPATH, "//*[@type='checkbox']")


# is displayed
print("Username is displayed:", username.is_displayed())
assert username.is_displayed()

# is enabled
print("Checkbox is enabled:", checkbox.is_enabled())    
assert checkbox.is_enabled()

# is selected
print("Checkbox is selected:", checkbox.is_selected())
assert not checkbox.is_selected()   

checkbox.click()
print("Checkbox is selected:", checkbox.is_selected())
assert checkbox.is_selected()   


browser.get_screenshot_as_file("Evidences/screenshot.png")


time.sleep(3)
browser.quit()



