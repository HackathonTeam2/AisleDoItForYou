from flask import Flask, Response, redirect, render_template, url_for, request
from barcode_reader import *

app = Flask(__name__)
video = cv2.VideoCapture(0)


@app.route('/')
def index():
    return redirect('/intro')

@app.route('/intro')
def intro():
    return render_template('intro.html')


@app.route('/home')
def after():
    return render_template('index.html')


@app.route('/scanner')
def scanner():
    return Response(generateVideo(video), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/tasks', methods=['POST'])
def tasks():
    if request.method == 'POST':
        return render_template("Daniel.html", barcode=os.getenv("QR_VAL"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True, debug=True)
