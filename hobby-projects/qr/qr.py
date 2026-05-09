import qrcode
img = qrcode.make("https://www.google.com")
img.save('C:/Users/Ellen/Downloads/qr.png') # pyright: ignore[reportArgumentType]
