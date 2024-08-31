from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
URL = "https://www.instagram.com/"


class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url=URL)


    def login(self, email, password):
        email_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_input.send_keys(email)

        password_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)

        time.sleep(1)

        log_in_button = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        log_in_button.click()

        time.sleep(13)

        continue_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, '//div[@role="button" and text()="Continue"]'))
        )
        continue_button.click()
