from flask import Flask, render_template, redirect, url_for, flash, session
from models import db, User, Activity, Fiscal_Account, FieldYield
from forms import RegistrationForm, LoginForm, ActivityForm, Fiscal_AccountForm, YieldForm
from flask_bootstrap import Bootstrap5
from werkzeug.security import generate_password_hash, check_password_hash
import os, datetime
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


@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/prices')
def price():
    return render_template('prices.html')


@app.route('/yield', methods=['POST', 'GET'])
def yields():
    if 'user_id' in session:
        form = YieldForm()
        if form.validate_on_submit():
            field_name = form.field_name.data
            agricultural_culture = form.agricultural_culture.data
            field_area = form.field_area.data
            field_yield = form.field_yield.data
            new_yield = FieldYield(field_name=field_name, agricultural_culture=agricultural_culture, field_area=field_area, field_yield=field_yield)
            db.session.add(new_yield)
            db.session.commit()
            return redirect(url_for('home'))
        return render_template('yield.html', form=form)
    return redirect(url_for('home'))


@app.route('/activity', methods=['POST', 'GET'])
def activity():
    if 'user_id' in session:
        form = ActivityForm()
        if form.validate_on_submit():
            activity_name = form.activity_name.data
            cultivated_agricultural_area = form.cultivated_agricultural_area.data
            field_name = form.field_name.data
            field_area = form.field_area.data
            new_activity = Activity(activity_name=activity_name, cultivated_agricultural_area=cultivated_agricultural_area, field_name=field_name, field_area=field_area)
            db.session.add(new_activity)
            db.session.commit()
            flash('You have been add new activity!', 'success')
            return redirect(url_for('home'))
        return render_template('activity.html', form=form)
    return redirect(url_for('home'))


@app.route('/fiscal_account', methods=['POST', 'GET'])
def fiscal_account():
    if 'user_id' in session:
        form = Fiscal_AccountForm()
        if form.validate_on_submit():
            products_name = form.products_name.data
            price = form.price.data
            buy_date = form.buy_date.data
            new_fiscal_account = Fiscal_Account(products_name=products_name, price=price, buy_date=buy_date)
            db.session.add(new_fiscal_account)
            db.session.commit()
            return redirect(url_for('records'))
        return render_template('fiscal_account.html', form=form)
    return redirect(url_for('home'))

@app.context_processor
def current_year():
    return {'current_year': datetime.datetime.now().year}

@app.route('/records')
def records():
    accounts = Fiscal_Account.query.order_by(Fiscal_Account.id.desc()).all()
    return render_template('records.html', accounts=accounts)

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