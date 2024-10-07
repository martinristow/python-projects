from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

URL = (
    'https://www.sinpeks-shop.mk/index.php?pageid=A2&kategorija=%D0%A2%D1%80%D0%B0'
    '%D0%BA%D0%BE%D1%80%D0%B8%20%D0%B4%D0%BE%2085%20%D0%9A%D0%A1&id=A107')

google_options = webdriver.ChromeOptions()
google_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=google_options)
driver.get(url=URL)

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

data = []
all_tractors = driver.find_elements(By.CLASS_NAME, value='artikal-desc')

for index, tractor in enumerate(all_tractors):
    name = tractor.find_element(By.CLASS_NAME, value='naziv-artikla').text
    model_name = tractor.find_element(By.CLASS_NAME, value='proizvodjac-artikla').text
    short_description = tractor.find_element(By.CLASS_NAME, value='kratak-opis-artikla').text

    try:
        price = tractor.find_element(By.CLASS_NAME, value='cenacifra').text
        number_price = float(price.replace(',', ''))
    except:
        number_price = 0.0

    print(f"{name}: {model_name}")
    if number_price >= 1000000:
        data.append({
            'Name': name,
            'Model Name': model_name,
            'Short Description': short_description,
            'Price': number_price
        })

df = pd.DataFrame(data)

df.to_csv('tractors_over_1milion-denars.csv', index=False, encoding='utf-8-sig')

driver.quit()
