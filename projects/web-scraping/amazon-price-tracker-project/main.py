from bs4 import BeautifulSoup
import requests

URL = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(url=URL)
amazon_website_html = response.text

soup = BeautifulSoup(amazon_website_html, "html.parser")
# print(soup.prettify())

# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").text

# Remove the dollar sign using split
price_without_currency = price.split("$")[1]

# Convert to floating point number
price_as_float = float(price_without_currency)
print(price_as_float)