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

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Approach to money
        money = driver.find_element(By.ID, value="money")
        money_text = money.text.replace(",", "")
        if money_text.isdigit():
            converted_money = int(money_text)
        else:
            converted_money = 0

        # Approach to amount in items
        items = driver.find_elements(By.CSS_SELECTOR, value="#store b")  # Refresh the items list
        first_words = [item.text.split()[0] for item in items if item.text]

        cost = [int(pri.text.replace(",", "").split()[-1]) for pri in items if pri.text.split()]

        # Every name and price put into dictionary
        dict_for_names_and_prices = {}
        for n in range(len(first_words)):
            dict_for_names_and_prices[first_words[n]] = cost[n]

        # Find the most expensive item you can afford and click it
        affordable_items = {name: price for name, price in dict_for_names_and_prices.items() if
                            converted_money >= price}
        if affordable_items:
            most_expensive_item = max(affordable_items, key=affordable_items.get)
            item_index = first_words.index(most_expensive_item)

            # Refresh the specific item before clicking
            items = driver.find_elements(By.CSS_SELECTOR, value="#store b")
            items[item_index].click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
