import cv2
import hashlib

def m5(s):
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()

def snapshot(file, path, l=3):
    vc = cv2.VideoCapture(file) #读入视频文件
    c = 1
    n = 1
    interval = 2000  #视频帧计数间隔频率
    name = m5(file.split('\\')[-1][0:-4])
    imglist = []

    if vc.isOpened(): #判断是否正常打开  
        rval, frame = vc.read()
        img = path + name + str(c) + '.jpg'
        cv2.imwrite(img, frame)
        imglist.append(img)
        print(img)
    else:
        rval = False

    while rval and n<l:   #循环读取视频帧
        rval, frame = vc.read()

        if c % interval == 0:
            img = path + name + str(c) + '.jpg'
            cv2.imwrite(img, frame)
            n = n + 1
            imglist.append(img)
            print(img)

        c = c + 1

    vc.release()
    return imglist

if __name__ == '__main__':
    f = r'F:\0\新建文件夹 (4)\【R-18 MMD】ミクちゃんでおしおきハイファイレイヴァー【すりガラス】.mp4'
    p = 'F:/0/img/'
    snapshot(f, p)