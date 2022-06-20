import qrcode

data = "Hello there"

img = qrcode.make(data)
img.save('.\qrcodes\image.png')