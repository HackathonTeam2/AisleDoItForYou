from dotenv import find_dotenv, load_dotenv
from flask import Flask, Response, redirect, render_template, url_for, request
from barcode_reader import *
from db_model import *

load_dotenv(find_dotenv())

load_dotenv(find_dotenv())

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

db.init_app(app)
with app.app_context():
    db.create_all()

video = cv2.VideoCapture(0)


@app.route("/")
def index():
    return redirect("/intro")

@app.route("/intro")
def intro():
    return render_template("intro.html")


@app.route("/home")
def after():
    return render_template("index.html")


@app.route("/scanner")
def scanner():
    return Response(
        generateVideo(video), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/product_list", methods=["POST"])
def product_list():
    if request.method == "POST":
        barcode=os.getenv("QR_VAL")
        productList = Products.query.filter_by(product_location="1")
        return render_template("productList.html", productList = productList)

#Uneccessary route, used to create test data
@app.route("/add")
def add():
    from random import randrange
    name=["Product1","Product2","Product3","Product4","Product5"]
    type=["Food", "Electronic", "Drink", "Outdoors","Toys"]
    location=[1,2,3,4,5,6,7,8,9]
    count = 0
    while count < 20:
        newProduct = Products(name[randrange(0,len(name))],type[randrange(0,len(type))],location[randrange(0,len(location))],randrange(1,100))
        db.session.add(newProduct)
        db.session.commit()
        count += 1
        


if __name__ == "__main__":
    app.run(debug=True,host=os.getenv("IP","0.0.0.0"), port=int(os.environ.get("PORT", 2204)))
