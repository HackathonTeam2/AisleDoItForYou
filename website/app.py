from dotenv import find_dotenv, load_dotenv
from flask import Flask, Response, redirect, render_template, url_for, request
from barcode_reader import *
from db_model import *

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


# @app.route("/add")
# def add():
#     count = 0
#     while count < 20:
#         obj = table("name")


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


@app.route("/tasks", methods=["POST"])
def tasks():
    if request.method == "POST":
        return render_template("Daniel.html", barcode=os.getenv("QR_VAL"))


app.run(debug=True,host=os.getenv("IP","0.0.0.0"), port=int(os.environ.get("PORT", 2204)))
