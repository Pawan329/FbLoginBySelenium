import time
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=options)

# s = Service("chromedriver.exe")
# driver = webdriver.Chrome(service = s)
driver.maximize_window()
driver.get("https://www.facebook.com/")

time.sleep(1)
driver.find_element_by_id('email').send_keys("username")
time.sleep(1)
driver.find_element_by_id('pass').send_keys("Password")
time.sleep(1)
driver.find_element(By.XPATH, "//*[text()='Log In']").click()
time.sleep(1)





