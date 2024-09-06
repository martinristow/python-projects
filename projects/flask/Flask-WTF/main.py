from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5
email = ""
password = ""


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(message="Ne moze prazno da go ostaves poleto"), Email(message="Greska Email")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Mora povekje od 8 karakteri")])
    submit = SubmitField(label="Log In")

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():

    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == email and login_form.password.data:
            return render_template("success.html")
        return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)