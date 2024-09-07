from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library-project.db"
# initialize the app with the extension
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)

with app.app_context():
    db.create_all()

# with app.app_context():
#     # new_book = Book(id=1, title="Martin Ristov", author="J. K. Rowling", rating=9.3)
#     # id poleto moze i da ne go popolnuvame nie bidejki toa samo se azurira za +1
#     new_book = Book(title="Martin Ristov", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()


@app.route('/')
def home():
    # Read All Records
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"],
        }

        with app.app_context():
            # new_book = Book(id=1, title="Martin Ristov", author="J. K. Rowling", rating=9.3)
            # id poleto moze i da ne go popolnuvame nie bidejki toa samo se azurira za +1
            new_book = Book(title=new_book["title"], author=new_book["author"], rating=new_book["rating"])
            db.session.add(new_book)
            db.session.commit()


        return redirect(url_for('home'))

    return render_template("add.html")



@app.route("/edit/<int:book_id>", methods=["POST", "GET"])
def edit(book_id):
    with app.app_context():
        # Get the book by its id
        book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()

    if request.method == "POST":
        # Update the book's rating
        new_rating = request.form["rating"]
        with app.app_context():
            book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
            book_to_update.rating = new_rating
            db.session.commit()

        return redirect(url_for('home'))

    return render_template("edit.html", book=book)


@app.route("/delete/<int:book_id>")
def delete(book_id):
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        if book_to_delete:
            db.session.delete(book_to_delete)
            db.session.commit()
        return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)
