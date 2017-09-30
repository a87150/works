from urllib import request
import re

class Tool:
    removeIns = re.compile('<ins.*?></ins>', re.S)
    removeHead = re.compile('<script>.*?</script>', re.S)
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeIns,"",x)
        x = re.sub(self.removeHead,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()

tool = Tool()
response = request.urlopen('http://www.yinwang.org/').read().decode('utf-8')
pattern = re.compile(r'title">.*?<a href="(.*?)">(.*?)</a>', re.S)
blog = re.findall(pattern, response)
pattern2 = re.compile(r'<td width="60%">.*?</td>', re.S)

for item in blog:
    print(item)
    blogurl = 'http://www.yinwang.org' + item[0]
    blogpage = request.urlopen(blogurl).read().decode('utf-8')
    body = re.findall(pattern2, blogpage)
    article = "\n"*4 + tool.replace(body[0])
    fileName = 'blog.txt'
    with open(fileName,"a", encoding='utf-8') as f:
        f.write(article)
        print("写入成功")