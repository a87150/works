from urllib import request
import re
import sqlite3

from bs4 import BeautifulSoup



def crawl_yinwang(url):
    response = request.urlopen(url).read().decode('utf-8')
    blog = BeautifulSoup(response, 'html.parser')
    page = {}

    for link in blog.find_all('a'):
        title = link.get_text()
        blog_url = url + link.get('href')

        if  title not in ['博客', '付费', '当然我在扯淡']:
            print(title, blog_url)
            page[title] = blog_url

    return page

def save_article(page):
    conn = sqlite3.connect('article.db')

    try:
        conn.execute('create table article (title varchar(100) primary key, content varchar(20000))')
    except:
        pass

    for title, url in page.items():
        response = request.urlopen(url).read().decode('utf-8')
        article = BeautifulSoup(response, 'html.parser')
        content = str(article.div)

        try:
            with conn:
                conn.execute('insert into article (title, content) values (?, ?)', (title, content))
            print('成功')

        except sqlite3.IntegrityError as e:
            with conn:
                conn.execute('update article set content = ? where title = ?', (content, title))
            print('更新')

    conn.close()


url = 'http://www.yinwang.org'
page = crawl_yinwang(url)

save_article(page)
