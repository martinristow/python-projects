from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options_google = webdriver.ChromeOptions()
options_google.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options_google)

driver.get(url="https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Martin")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Ristov")

email = driver.find_element(By.NAME, value="email")
email.send_keys("hi_angela@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()
