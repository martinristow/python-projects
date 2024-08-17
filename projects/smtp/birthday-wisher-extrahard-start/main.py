import pandas
import random
import smtplib
import datetime as dt

MY_MAIL = ""
PASSWORD = ""

letter_text = "letter_templates"
letters = [f"{letter_text}/letter_1.txt", f"{letter_text}/letter_2.txt", f"{letter_text}/letter_3.txt"]
random_letter = random.choice(letters)

birthdays = pandas.read_csv("birthdays.csv")
birth_dict = birthdays.to_dict(orient="records")
now = dt.datetime.now()
month = now.month
day = now.day


for item in birth_dict:
    month1 = item["month"]
    day1 = item["day"]
    if month == month1 and day == day1:
        name = item["name"]
        email = item["email"]
        with open(random_letter) as letter:
            content = letter.read()
            new_content = content.replace("[NAME]", name)
            # print(content)
            # print(new_content)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_MAIL, password=PASSWORD)
                message = f"Subject:Happy Birthday\n\n{new_content}"
                connection.sendmail(
                    from_addr=MY_MAIL,
                    to_addrs=email,
                    msg=message.encode("utf-8")
                )
