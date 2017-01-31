from urllib.request import urlopen , Request
import re

class Tool:
    replaceHEAD = re.compile(r'<script>.*?</script>',re.S)
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
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
    def replace(self,x):
        x = re.sub(self.replaceHEAD,"",x)
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip('\u22ef')

tool = Tool()
request = Request('http://www.yinwang.org/')
response = urlopen(request)
pattern = re.compile(r'title">.*?<a href="(.*?)">(.*?)</a>',re.S)
page = response.read().decode('utf-8')
blog = re.findall(pattern,page)
blogurl = []
for item in blog:
      blogurl.append([item[0].strip()])#,item[1].strip()
print(blogurl)
for item in blogurl:
     blogURL = item[0]
     blogpage = tool.replace(urlopen(blogURL).read().decode('utf-8'))
     fileName = 'blog' + ".txt"
     with open(fileName,"a",encoding='utf-8') as f:
          f.write(blogpage)
          print("写入成功")