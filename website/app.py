from flask import Flask, Response, redirect, render_template,url_for,make_response
from pyzbar.pyzbar import decode
import cv2
from sqlalchemy import false
app = Flask(__name__)

app.config['SERVER_NAME'] = '0.0.0.0:2204'

@app.route('/')
def index():
    return redirect('/scanner')

def read_barcodes(frame):
    barcodes = decode(frame)
    for barcode in barcodes:
        barcode_text = barcode.data.decode('utf-8')
        return barcode_text
    return frame
    
def gen(video):
    while True:
        success, image = video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        text = read_barcodes(image)
        if type(text) == str:
            print(type(text))
            print(text)
            with app.app_context():
                print(url_for('after'))
                return render_template("index.html")
        else:
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/scanner')
def scanner():
    video = cv2.VideoCapture(0)
    scanner = Response(gen(video),mimetype='multipart/x-mixed-replace; boundary=frame')
    bypass = False
    while bypass == False:
        if gen(video) is True:
            bypass = True
        return scanner
    return redirect('/after')

    # if gen(video) is False:
    #     print(gen(video))
    #     return redirect('/after')
    # else:
    #     print(type(gen(video)))
    #     return Response(gen(video),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/after')
def after():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True, debug=True)
