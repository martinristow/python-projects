from ZillowClass import Zillow
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

GOOGLE_SHEETS_URL = "https://docs.google.com/forms/d/e/1FAIpQLSe66PLaocbJfwN1y7x2NyMlYrhUNlaGySEpecqmXB44344lCg/viewform"


def spreadsheets():
    for i in range(len(prices)):
        time.sleep(2)
        address_input = driver.find_element(By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(address[i])
        price_input = driver.find_element(By.XPATH,
                                          value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input.send_keys(prices[i])
        link_input = driver.find_element(By.XPATH,
                                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input.send_keys(links[i])
        submit_button = driver.find_element(By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        submit_button.click()
        time.sleep(3)
        submit_another_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        submit_another_response.click()


google_options = webdriver.ChromeOptions()
google_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=google_options)
driver.get(url=GOOGLE_SHEETS_URL)


obj = Zillow()
prices = obj.get_price()
address = obj.get_address()
links = obj.get_link()

spreadsheets()
