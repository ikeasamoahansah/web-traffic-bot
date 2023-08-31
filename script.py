from selenium import webdriver
from selenium.webdriver.common.by import By
import time

website = 'https://eduadvance.net'
# location = 'C:\Development\msedgedriver.exe'

driver = webdriver.Edge()
driver.get(website)

# element = driver.find_element(By.ID, 'sb_form_q')
# element.send_keys('WebDriver')
# element.submit()

time.sleep(10)
driver.quit()