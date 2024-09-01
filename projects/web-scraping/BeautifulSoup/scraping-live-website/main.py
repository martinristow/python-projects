from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_texts = []
article_links = []

articles = soup.find_all(name="span", class_="titleline")
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)

    link = article_tag.find(name="a").get("href")
    article_links.append(link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

biggest_number = max(article_upvotes)
index_number = article_upvotes.index(biggest_number)

print(article_texts[index_number])
print(article_links[index_number])
