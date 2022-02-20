import cv2,datetime,os
from pyzbar.pyzbar import decode

capture = 0
barcodeVal = ""


def read_barcodes(frame):
    global barcodeVal
    barcodes = decode(frame)
    for barcode in barcodes:
        barcode_text = barcode.data.decode('utf-8')
        barcodeVal = barcode_text
        return barcodeVal
    return frame
    
def generateVideo(video):
    global capture
    
    while True:
        success, image = video.read()
        text = read_barcodes(image)
        if success:
            if type(text) == str:
                print(text)
                os.environ['QR_VAL'] = text
            try:
                ret, jpeg = cv2.imencode('.jpg', image)
                frame = jpeg.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

            except Exception as e:
                pass
