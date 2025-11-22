import qrcode

img = qrcode.make("www.linkedin.com/in/vijayvar")
img.save("your.png")
print("QR code created!")
