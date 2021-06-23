#import module
from PIL import Image
from pyzbar.pyzbar import decode

# welcome message
print("Welcome to QR code reader")

img = Image.open("QRcode.png")

#decode the QR code
d = decode(img)

print(d[0].data.decode())