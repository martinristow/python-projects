from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_SHEETS_URL = ""


class Zillow:
    def __init__(self):
        self.response = requests.get(url=ZILLOW_URL)
        self.zillow_html = self.response.text
        self.soup = BeautifulSoup(self.zillow_html, "html.parser")


    def get_price(self):
        price_html = self.soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
        all_prices = []
        for pr in price_html:
            if "+/mo" in pr.text:
                all_prices.append(pr.text.split("+/mo")[0])
            elif "/mo" in pr.text:
                all_prices.append(pr.text.split("/mo")[0])
            elif "+ 1 bd" in pr.text:
                all_prices.append(pr.text.split("+ 1 bd")[0])

        # print(len(all_prices))
