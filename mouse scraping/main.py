from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "mouse"
files = 0
for i in range (1, 10):
    driver.get(f"https://www.amazon.in/s?k={query}&crid=26VSPZPYZOXG1&sprefix={query}%2Caps%2C227&ref=nb_sb_noss_{i}")
    # mouse = 0
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")    
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"D:\CODING\Python\webscraping using python and selenium\mouse scraping\data\{query}_{files}.html", 'w', encoding="utf-8") as f:
            f.write(d)
            files += 1
        # print(elem.get_attribute(outerHTML)) 
        
    time.sleep(2)
driver.close()

