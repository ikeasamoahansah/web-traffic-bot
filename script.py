from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

website = 'https://eduadvance.net'

driver = webdriver.Edge()
driver.get(website)

footer = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/div/div/div/div[2]")
# delta_y = footer.rect['50']
ActionChains(driver).scroll_by_amount(0, 5000).perform()

time.sleep(10)
driver.quit()