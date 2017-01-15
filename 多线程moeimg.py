import re
from queue import Queue
from threading import Thread
from time import time
from urllib.request import urlopen , Request


def url_open(url):
    request = Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
    response = urlopen(request)
    return response.read()

	
def get_links(url):
    page = url_open('http://moeimg.net/' + str(url) + '.html').decode('utf-8')
    pattern = re.compile(r'<img src="http://(.*?)" alt="\d*"',re.S)
    imgs = re.findall(pattern,page)
    return imgs

			
def download_link(link):
    conn = url_open('http://' + link)
    filename = link[-14:]
    with open("E:/新建文件夹 (2)/" + filename,"wb") as f:
        f.write(conn)
        print("%s 写入成功" %link)
		
		
class DownloadWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            if item is None:
                break
            link = item
            download_link(link)
            self.queue.task_done()


def main():
    ts = time()
    url = 5555
    queue = Queue()
    for i in range(5):
        links = get_links(url)
        url = url + 1
        for link in links:
            queue.put(link)
            
    for x in range(4):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()

		
    queue.join()
    print('一共下载了 {} 张图片'.format(len(links)))
    print('Took {}s'.format(time() - ts))


if __name__ == '__main__':
    main()