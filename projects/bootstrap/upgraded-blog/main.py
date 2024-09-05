from flask import Flask, render_template, request
import requests, datetime, smtplib, os
from dotenv import load_dotenv

load_dotenv()
time_now = datetime.datetime.now().date()
year = datetime.datetime.now().year
app = Flask(__name__)

FROM_EMAIL = os.environ["FROM_EMAIL"]
PASSWORD = os.environ["PASSWORD"]


@app.route("/")
def index():
    respond = requests.get(url="https://api.npoint.io/f5ff69b0c317d2aed364")
    json_data = respond.json()
    return render_template("index.html", all_posts=json_data, time_now=time_now, year=year)


@app.route("/about")
def about():
    return render_template("about.html", year=year)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        send_email(name, email, phone, message)
        return render_template("contact.html", year=year, msg_send=True)
    return render_template("contact.html", year=year, msg_send=False)


@app.route("/post/<int:id>")
def post(id):
    respond = requests.get(url="https://api.npoint.io/f5ff69b0c317d2aed364")
    json_data = respond.json()
    post1 = None
    for post in json_data:
        if post["id"] == id:
            post1 = post
            break
    print(post1)  # Debugging line to see the post data
    return render_template("post.html", post=post1, time_now=time_now, year=year)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(FROM_EMAIL, PASSWORD)
        connection.sendmail(FROM_EMAIL, "", email_message)


if __name__ == "__main__":
    app.run(debug=True)
