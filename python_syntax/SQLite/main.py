# import sqlite3
#
# db = sqlite3.connect("books-collection.db") # pravime konekcija so bazata
#
# cursor = db.cursor() # kreirame kursor koj sto ke ni sluzi za da ja kontrolirame bazata
#
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(2, 'Martin Ristov', 'Martin', '9.3')")
# db.commit()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

##CREATE DATABASE
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False) # nullable=False znaci deka nema da dozvoli NULL vrednosti
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
with app.app_context():
    new_book = Book(id=2, title="Martin Ristov", author="J. K. Rowling", rating=9.9)
    db.session.add(new_book)
    db.session.commit()
