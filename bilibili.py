import re
from selenium import webdriver
import time, requests
from browsermobproxy import Server

browser = webdriver.Chrome()
# browser = webdriver.phantomJS(executable_path = "")

rank_url = "https://www.bilibili.com/ranking#!/all/119/0/3/"

browser.get(rank_url)
content = browser.page_source
browser.quit()

pattern = re.compile('<div class="rank-item"><div class="num">(.*?)</div><div class="content clearfix"><a href="(.*?)" target="_blank"><div class="preview">.*?<div class="title">(.*?)</div>', re.S)
                    
item = re.findall(pattern, content)

base_url = "https://www.bilibili.com"



for i in range(5):
    print(item[i])
    # 代理
    server = Server("F:\\Software\\Python\\Lib\\site-packages\\browsermobproxy\\Browsermob-Proxy\\bin\\browsermob-proxy")
    server.start()
    proxy = server.create_proxy()
    # 浏览器
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
    browser = webdriver.Chrome(chrome_options = chrome_options)

    proxy.new_har("bilibili")
    browser.get(base_url + item[i][1])
    
    # browser.find_element_by_name("pause_button").click()
    time.sleep(1)
    content = proxy.har
    server.stop()
    browser.quit()
    
    video_box = []
    data = content['log']['entries']
    for j in range(len(data)):
        url = data[j]['request']['url']
        if url.find("flv") != -1:
            print(url)
            video_box.append(url)
            hd_video_url = video_box[0]
    
    try:
        video = requests.get(hd_video_url, timeout = 10)
        
    except requests.exceptions.ConnectionError:
        print('error can not download')
        
    string = "E:/" + item[i][0] + item[i][2] + '.flv'
    fp = open(string, 'wb')
    fp.write(video.content)