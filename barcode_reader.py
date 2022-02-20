import cv2
from pyzbar.pyzbar import decode


def read_barcodes(frame):
    barcodes = decode(frame)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        barcode_text = barcode.data.decode('utf-8')
        print(barcode_text)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return frame


def main():
    camera = cv2.VideoCapture(0)

    while(True):
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow('Barcode reader', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


main()
