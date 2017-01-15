#!/usr/bin/env python
import sys
from lib2to3.main import main

sys.exit(main("lib2to3.fixes"))

'''
1. 如果给的target是folder,2to3会把目录下所有的py scripts都作一次转换 
2. 如果给的target是file,2to3只会转换该文件 

二、将2to3.py和你要转换的文件换到同一文件夹

三、执行命令
输入2to3.py -w 1.py回车运行即可

四、直接定位到python自带2to3.py的文件夹位置，不用复制2to3出来，然后转换其他文件夹下的python2脚本文件。
1、定位到python自带2to3.py的文件夹位置cd C:\Python34\Tools\Scripts
2、输入2to3.py -w 文件完整路径 例如d:\1.py或者D:\G-GameDev\1.py

注意：

（1）如果上述不加-w参数，则默认只是把转换过程所对应的diff内容打印输出到当前窗口而已。
（2）加了-w，就是把改动内容，写回到原先的文件了。
（3）不想要生成bak文件，再加上-n即可。
（4）不想看到那一堆输出的内容，加上–no-diffs，即可。
（5）这个帮助是2to3.py自带的，只需在后面加上 -h参数就行。
1、定位到2to3.py所在文件夹位置
2、输入2to3.py -h回车即可。
'''