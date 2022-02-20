import cv2
from pyzbar.pyzbar import decode

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
        else:
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')