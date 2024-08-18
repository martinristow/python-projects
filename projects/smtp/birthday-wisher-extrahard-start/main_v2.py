from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = ""
PASSWORD = ""
today = datetime.now()
today_tuple = (today.month, today.day)
# print(today_tuple)
data = pandas.read_csv("birthdays.csv")
# print(data["name"])
# print(data.iterrowss())
birthday_dict = {(data_row["month"], data_row["day"]): data_row for index, data_row in data.iterrows()}
# print(birthday_dict)
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    # print(birthday_person)
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    # print(file_path)
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        # print(contents)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}".encode("utf-8")
        )
