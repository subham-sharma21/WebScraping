from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&ref=nb_sb_noss")

# driver.get(f"https://www.amazon.in/s/ref=nb_sb_noss?url=node%3D1389401031&field-keywords={query}")
elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
print(elem.get_attribute("outerHTML"))
time.sleep(5)
driver.close()