import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://saucedemo.com")
print(browser.title)
print(browser.current_url)
print(browser.page_source)






