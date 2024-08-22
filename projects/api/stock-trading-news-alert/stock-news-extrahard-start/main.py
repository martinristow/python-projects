import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""


# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News"). DONE
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
# print(response)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
#This dict is convert into a list
data_list = [value for (key, value) in data.items()]

#Get yesterday's closing stock price
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)

#Get the day before yesterday's closing stock price
day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]
# print(day_before_yesterday)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#Abs function return positive number. If the result is -5, after abs function we have +5
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)


# STEP 2: Use https://newsapi.org# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if abs(diff_percent) > 5:
    news_params = {
            "apiKey": NEWS_API_KEY,
            "q": COMPANY_NAME,
        }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    # print(articles)

    three_articles = articles[:3]
    # print(three_articles)
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief:{article['description']}" for article in three_articles]

    # Send a separate message with the percentage change and each article's title and description to your phone number.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="",
            to=""
        )
        # print(message.status)
