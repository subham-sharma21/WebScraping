from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
for i in range(1, 20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&ref=nb_sb_noss")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    for elem in elems:
        print(elem.text)
        
    # print(elem.get_attribute("outerHTML"))
    time.sleep(1)
    driver.close()