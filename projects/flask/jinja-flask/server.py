from flask import Flask, render_template
import random
import datetime
import requests
app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    my_name = "Martin"
    return render_template("index.html", number=random_number, year=current_year, name=my_name)
    # ovde imeto number nie sami mu go davame, mozeme bilo koe ime da mu go zadademe i kje raboti bez problem


@app.route("/guess/<string:name>")
def guess_name(name):
    agify = requests.get(url=f"https://api.agify.io?name={name}")
    agify_json_data = agify.json()
    age = agify_json_data["age"]
    name = agify_json_data["name"]

    genderize = requests.get(url=f"https://api.genderize.io?name={name}")
    genderize_json_data = genderize.json()
    gender = genderize_json_data["gender"]

    return render_template("guess.html", person_name=name, person_age=age, person_gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
