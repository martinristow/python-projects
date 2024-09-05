from flask import Flask, render_template
import requests, datetime
time_now = datetime.datetime.now().date()
year = datetime.datetime.now().year
app = Flask(__name__)


@app.route("/")
def index():
    respond = requests.get(url="https://api.npoint.io/f5ff69b0c317d2aed364")
    json_data = respond.json()
    return render_template("index.html", all_posts=json_data, time_now=time_now, year=year)


@app.route("/about")
def about():
    return render_template("about.html", year=year)

@app.route("/contact")
def contact():
    return render_template("contact.html", year=year)

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


if __name__ == "__main__":
    app.run(debug=True)