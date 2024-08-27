from bs4 import BeautifulSoup
import requests
import smtplib

MY_EMAIL = ""
MY_PASSWORD = ""

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


# ====================== Send an Email ===========================

# Get the product title
title = soup.find(id="productTitle").getText().strip()
print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="",
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
                            )
        