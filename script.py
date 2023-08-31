from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

website = 'https://eduadvance.net'

driver = webdriver.Edge()
driver.get(website)

ActionChains(driver).scroll_by_amount(0, 5000).perform()

time.sleep(10)
driver.quit()