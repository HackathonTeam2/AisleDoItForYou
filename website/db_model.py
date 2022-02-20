import imp
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80), unique=False, nullable=False)
    product_location = db.Column(db.String(3), unique=False, nullable=False)
    price = db.Column(db.Integer, unique=True, nullable=False)
