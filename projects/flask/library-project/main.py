from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)
all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"],
        }
        all_books.append(new_book)

        return redirect(url_for('home'))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

