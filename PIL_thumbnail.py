from PIL import Image

import os

def thumbnail(path):
    im = Image.open(path)
    w = im.size[0] // 1
    h = im.size[1] // 1
    size = (w, h)
    im.thumbnail(size)
    print len(im.split())

    if len(im.split()) == 4:
        r, g, b, a = im.split()
        im = Image.merge("RGB", (r, g, b))
        im.save(path, "JPEG")
    else:
        im.save(path, "JPEG")


def file(path):
    l = []
    for p in path:
        l.append([p + '/' + file for p, _, files in os.walk(p) for file in files if '.jpg' in file])
    return l

fl = file(['/0/' + f for f in os.listdir('/0/') if f != 'img'])

for fileList in fl:
    for f in fileList:
        print(f)
        try:
            thumbnail(f)
        except Exception as identifier:
            print(identifier)
        