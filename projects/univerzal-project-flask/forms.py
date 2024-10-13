from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField(label='Корисничко име', validators=[DataRequired(), Length(min=3, max=12)])
    email = StringField(label='Емаил', validators=[DataRequired(), Email()])
    password = PasswordField(label='Лозинка', validators=[DataRequired(), Length(min=7)])
    confirm_password = PasswordField(label='Потврди лозинка', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрирај се')



class LoginForm(FlaskForm):
    email = StringField(label='Емаил', validators=[DataRequired(), Email()])
    password = PasswordField(label='Лозинка', validators=[DataRequired()])
    submit = SubmitField(label='Најави се')



class ActivityForm(FlaskForm):
    activity_name = StringField(label='Име на активноста', validators=[DataRequired()])
    cultivated_agricultural_area = StringField(label='Обработена површина', validators=[DataRequired()])
    field_name = StringField(label='Име на нивата', validators=[DataRequired()])
    field_area = StringField(label='Целата површина на нивата', validators=[DataRequired()])
    submit = SubmitField('Креирај активност')


class YieldForm(FlaskForm):
    field_name = StringField(label='Име на нивата', validators=[DataRequired()])
    agricultural_culture = StringField(label='Тип на култура', validators=[DataRequired()])
    field_area = StringField(label='Целата површина на нивата', validators=[DataRequired()])
    field_yield = StringField(label='Приност на нивата', validators=[DataRequired()])
    submit = SubmitField('Додај принос')


class Fiscal_AccountForm(FlaskForm):
    products_name = StringField(label='Имиња на продукти', validators=[DataRequired()])
    price = StringField(label='Цена', validators=[DataRequired()])
    buy_date = StringField(label='Датум на купување', validators=[DataRequired()])
    submit = SubmitField('Креирај фискална сметка')