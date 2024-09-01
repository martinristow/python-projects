from bs4 import BeautifulSoup
import requests
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"


class Zillow:
    def __init__(self):
        self.header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
            "Dnt": "1",
            "Priority": "u=1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Sec-Gpc": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
        }
        self.response = requests.get(url=ZILLOW_URL, headers=self.header)
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
        return all_prices

    def get_address(self):
        address_html = self.soup.find_all(name="address", attrs={"data-test": "property-card-addr"})
        # print(address_html)
        address_list = [address.text.strip() for address in address_html]
        # print(address_list[0])
        return address_list

    def get_link(self):
        link_html = self.soup.find_all(name="a", attrs={"data-test": "property-card-link"})
        all_links = [link["href"] for link in link_html]
        return all_links
