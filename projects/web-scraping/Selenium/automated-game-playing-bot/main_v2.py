from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://orteil.dashnet.org/experiments/cookie/"

options_google = webdriver.ChromeOptions()
options_google.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options_google)
driver.get(url=URL)

# Approach to cookie
cookie = driver.find_element(By.ID, value="cookie")





# Approach to items for buy
items = driver.find_elements(By.CSS_SELECTOR, value="#store b")

# Approach to names in items
first_words = []
for item in items:
    if item.text:
        first_words.append(item.text.split()[0])



test = True
while test:
    cookie.click()

    # Approach to money
    money = driver.find_element(By.ID, value="money")
    converted_money = float(money.text)
    # print(converted_money)

    # Approach to amount in items
    price = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    cost = [float(pri.text.replace(",", "").split()[-1]) for pri in price if pri.text.split()]
    print(cost)

    recnik = {}
    for n in range(len(first_words)):
        recnik[first_words[n]] = cost[n]

    print(recnik)

    break