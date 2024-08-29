from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

URL = ("https://www.linkedin.com/jobs/search/?currentJobId=4010470258&f_AL=true&f_TPR=r2592"
       "000&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20K"
       "ingdom&origin=JOB_SEARCH_PAGE_JOB_FILTER")

load_dotenv()

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]

google_options = webdriver.ChromeOptions()
google_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=google_options)
driver.get(url=URL)

# Click Sign in Button
sing_in_button = driver.find_element(By.CLASS_NAME, value="nav__button-secondary")
sing_in_button.click()

# Sign in
username_input = driver.find_element(By.ID, value="username")
password_input = driver.find_element(By.ID, value="password")
username_input.send_keys(MY_EMAIL)
password_input.send_keys(MY_PASSWORD)

log_in_button = driver.find_element(By.CLASS_NAME, value="btn__primary--large")
log_in_button.click()

# save_job = driver.find_element(By.CSS_SELECTOR, value=".mt5 .jobs-save-button")
# save_job.click()

easy_apply_button = driver.find_element(By.CSS_SELECTOR, value=".mt5 .jobs-s-apply")
easy_apply_button.click()

submit_application = driver.find_element(By.CSS_SELECTOR, value=".mt3 .pv4 span")
# mt3 glaven div, pv4 vtor div, span element od vtor div
# print(submit_application.text)
submit_application.click()
