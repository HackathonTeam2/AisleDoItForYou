from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80), unique=False, nullable=False)
    product_type = db.Column(db.String(80), unique=False, nullable=False)
    product_location = db.Column(db.String(3), unique=False, nullable=False)
    product_aisle = db.Column(db.String(3), unique=False, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self,product_name,product_type,product_location,price):
        self.product_name = product_name
        self.product_type = product_type
        self.product_location = product_location
        self.price = price