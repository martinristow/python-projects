from flask import Flask, render_template, redirect, url_for, flash, session
from models import db, User
from forms import RegistrationForm, LoginForm
from flask_bootstrap import Bootstrap5
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

db.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/records')
def records():
    return render_template('records.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if 'user_id' in session:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('You have been registered!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)



@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'user_id' in session:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login Successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    return render_template('login.html', form=form)



@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)