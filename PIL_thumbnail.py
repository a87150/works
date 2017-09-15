from PIL import Image

im = Image.open(r'C:\Users\a8715\Desktop\teKtfZq.jpg')
w = im.size[0]//2
h = im.size[1]//2
size = (w, h)
im.thumbnail(size)
im.save('s.JPEG', "JPEG")