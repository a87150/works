from urllib.request import urlopen , Request
import re
import time

def url_open(url):
	request = Request(url)
	request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
	response = urlopen(request)
	time.sleep(1)
	return response.read()

for number in range(5008,8000):
	page_number = str(number)
	page = url_open('http://moeimg.net/' + page_number + '.html').decode('utf-8')
	pattern = re.compile(r'<img src="http://(.*?)" alt="\d*"',re.S)
	imgs = re.findall(pattern,page)
	print(imgs)
	for img in imgs:
		conn = url_open('http://' + img)
		filename = img[-10:]
		with open("E:/新建文件夹 (2)/" + filename,"wb") as f:
			f.write(conn)
			print("%s写入成功" %img)