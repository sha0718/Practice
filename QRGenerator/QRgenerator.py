import qrcode
# from pyzbar.pyzbar import decode
# from PIL import Image
myqr = qrcode.make("https://www.youtube.com/watch?v=PyDn2gU9DJo")
myqr.save("myqr.png", scale = 8)

myqr1 = qrcode.make("https://www.youtube.com/watch?v=IUQVO97zcE0")
myqr1.save("myqr1.png",scale = 7)

# b = decode(Image.open("myqr.png"))
# print(b[0].data.decode("ascii"))
