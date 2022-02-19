import qrcode

img = qrcode.make("Sum 2 Prove")
img.save("sumn.jpg")

img = qrcode.make("Caramel Macchiato")
img.save("coffee.jpg")

import cv2
d = cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("coffee.jpg"))
print(val)