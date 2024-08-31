from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException
import time
URL = "https://www.instagram.com/"


class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url=URL)


    def login(self, email, password):
        email_input = self.driver.find_element(By.XPATH,
                                               value='//*[@id="loginForm"]/div/div[1]/div/label/input')
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


    def find_followers(self, similar_acc):
        time.sleep(5)
        self.driver.get(url=f"{URL}{similar_acc}/followers")
        time.sleep(5)
        modal_xpath = '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[4]'
        modal = self.driver.find_element(By.XPATH, value=modal_xpath)

        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required.
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
                # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
