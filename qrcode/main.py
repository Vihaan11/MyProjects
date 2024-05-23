import qrcode

url = input("URL: https://")
name = input("Image name (Do not put file extension): ")

img = qrcode.make("https://{}".format(url))
img.save("C://Users//vyass//OneDrive//Desktop//{}".format(name + ".jpg"))

print("The QR code is saved to your desktop")


