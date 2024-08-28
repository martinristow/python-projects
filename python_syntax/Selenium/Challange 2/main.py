from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to Wikipedia
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

# test = driver.find_element(By.ID, value="articlecount")
# print(test.text)

# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# print(article_count.text)

# None in on anchor tag using CSS selectors
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)

driver.quit()
