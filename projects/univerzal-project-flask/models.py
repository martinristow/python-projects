from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(50), nullable=False)
    cultivated_agricultural_area = db.Column(db.String(50), nullable=False)
    field_name = db.Column(db.String(50), nullable=False)
    field_area = db.Column(db.String(50), nullable=False)


class FieldYield(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.String(50), nullable=False)
    agricultural_culture = db.Column(db.String(50), nullable=False)
    field_area = db.Column(db.String(50), nullable=False)
    field_yield = db.Column(db.String(50), nullable=False)