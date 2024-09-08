from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies.db"
# initialize the app with the extension
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    ranking: Mapped[str] = mapped_column(String(250), nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5')
    review = StringField('Your Review')
    submit = SubmitField('Done')


# New Find Movie Form
class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    img_url = StringField("IMG URL", validators=[DataRequired()])
    year = StringField("Year", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    ranking = StringField("Ranking", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

# with app.app_context():
#     for movie in movies:
#         db.session.add(movie)
#         db.session.commit()



@app.route("/")
def home():
    # Read All Records
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.id))
        all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["POST", "GET"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["POST", "GET"])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        img_url = form.img_url.data
        year = form.year.data
        description = form.description.data
        ranking = form.ranking.data

        with app.app_context():
            new_movie = Movie(title=movie_title, img_url=img_url, year=year, description=description, ranking=ranking, review="", rating=0)
            db.session.add(new_movie)
            db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
