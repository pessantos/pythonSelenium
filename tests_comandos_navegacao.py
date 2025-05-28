import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://saucedemo.com")
time.sleep(2)
#browser.refresh()
#browser.back()
#browser.forward()

browser.switch_to.new_window("tab")
time.sleep(2)
browser.close()
time.sleep(2)
browser.quit()





