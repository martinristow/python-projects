import requests
from flask import Flask, render_template

app = Flask(__name__)

BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route("/")
def home():
    return "<a href='/blog'>Go to Blog</a>"


@app.route("/blog")
def blog():
    response = requests.get(url=BLOG_URL)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/blog/<int:id>")
def read_blog(id):
    response = requests.get(url=BLOG_URL)
    all_posts = response.json()
    selected_post = None
    for post in all_posts:
        if post["id"] == id:
            selected_post = post
            break

    if selected_post:
        return render_template("post.html", post=selected_post)
    else:
        return "Post not found", 404



if __name__ == "__main__":
    app.run(debug=True)
