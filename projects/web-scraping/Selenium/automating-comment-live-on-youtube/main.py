from selenium import webdriver
from selenium.webdriver.common.by import By

URL = ""

google_options = webdriver.ChromeOptions()
google_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=google_options)
driver.get(url=URL)

sing_button = driver.find_element(By.CSS_SELECTOR, value="#buttons .yt-spec-button-shape-next")
sing_button.click()

mail = driver.find_element(By.NAME, value="identifier")
mail.send_keys("")

# But google not allow to log in :(
log_in = driver.find_element(By.XPATH, value='//*[@id="identifierNext"]/div/button/span')
log_in.click()

chat = driver.find_element(By.ID, value="input")
chat.send_keys("TEST TEST TEST PYTHON SKRIPTA")
