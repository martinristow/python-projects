from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep screen active after done of program
options_chrome = webdriver.ChromeOptions()
options_chrome.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options_chrome)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

# print(converted_money)
timeout = time.time() + 60 * 5   # 5 minutes from now

check_interval = 5
next_check = time.time() + check_interval

while timeout > time.time():
    cookie.click()
    if time.time() >= next_check:
        money = driver.find_element(By.ID, value="money")
        converted_money = float(money.text.replace(",", ""))

        portal_money = driver.find_element(By.CSS_SELECTOR, value="#buyPortal b").text.split()[2].replace(",", "")
        alchemy_money = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b/text()[2]').text.split()[2].replace(",", "")
        shipment_money = driver.find_element(By.CSS_SELECTOR, value="#buyShipment b").text.split()[2].replace(",", "")
        mine_money = driver.find_element(By.CSS_SELECTOR, value="#buyMine b").text.split()[2].replace(",", "")
        factory_money = driver.find_element(By.CSS_SELECTOR, value="#buyFactory b").text.split()[2].replace(",", "")
        grandma_money = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b").text.split()[2].replace(",", "")
        cursor_money = driver.find_element(By.CSS_SELECTOR, value="#buyCursor b").text.split()[2].replace(",", "")

        if converted_money > float(portal_money):
            buyPortal = driver.find_element(By.CSS_SELECTOR, value="#buyPortal b")
            buyPortal.click()

        elif converted_money > float(alchemy_money):
            buyAlchemyLab = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b/text()[2]')
            buyAlchemyLab.click()

        elif converted_money > float(shipment_money):
            buyShipment = driver.find_element(By.CSS_SELECTOR, value="buyShipment b")
            buyShipment.click()

        elif converted_money > float(mine_money):
            buyMine = driver.find_element(By.CSS_SELECTOR, value="#buyMine b")
            buyMine.click()

        elif converted_money > float(factory_money):
            buyFactory = driver.find_element(By.CSS_SELECTOR, value="#buyFactory b")
            buyFactory.click()

        elif converted_money > float(grandma_money):
            buyGrandma = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b")
            buyGrandma.click()

        elif converted_money > float(cursor_money):
            buyCursor = driver.find_element(By.CSS_SELECTOR, value="#buyCursor b")
            buyCursor.click()

        next_check = time.time() + check_interval
