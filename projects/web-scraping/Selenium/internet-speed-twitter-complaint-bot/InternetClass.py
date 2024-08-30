from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url=driver_path)
        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".js-start-test .start-text")
        go_button.click()
        time.sleep(50)
        self.down = self.driver.find_element(By.CSS_SELECTOR, value=".result-data .download-speed").text
        print(f"down: {self.down}")
        self.up = self.driver.find_element(By.CSS_SELECTOR, value=".result-data .upload-speed").text
        print(f"up: {self.up}")

    def tweet_at_provider(self, twitter_path):
        self.driver.get(url=twitter_path)
        print(self.driver.title)
