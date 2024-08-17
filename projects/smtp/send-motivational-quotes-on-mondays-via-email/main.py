import smtplib
import datetime as dt
import random

MY_EMAIL = ""
PASSWORD = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)

    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        message = f"Subject:Monday Motivation\n\n{random_quote}"
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=message.encode("utf-8")
        )
