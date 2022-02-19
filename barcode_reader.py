import cv2
from pyzbar.pyzbar import decode

def reader(img):
    readImg = cv2.imread(img)

    barcodes = decode(readImg)

    if not barcodes:
        print(barcodes)
        print("Not a barcode")
    else:
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(img, (x, y),
                          (x + w, y + h),
                          (255, 0, 0), 2)
            if barcode.data!="":
                
            # Print the barcode data
                print(barcode.data)
    
    cv2.imshow("Barcode",readImg)
    cv2.destroyAllWindows()

image = "SmartWater.jpg"
reader(image)