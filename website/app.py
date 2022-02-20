from flask import Flask, Response, redirect, render_template,url_for
from barcode_reader import *

app = Flask(__name__)

app.config['SERVER_NAME'] = '0.0.0.0:2204'

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def after():
    return render_template('index.html')

@app.route('/scanner')
def scanner():
    video = cv2.VideoCapture(0)
    return Response(gen(video),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True, debug=True)
