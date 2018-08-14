# coding='UTF-8'
from bs4 import BeautifulSoup  # 引入beautifulsoup 解析html事半功倍
import re
import urllib
import urllib.request
import sys
import io
import json
from collections import deque
import time


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  
# 改变标准输出的默认编码（这个比较重要一点，可以有效解决编码异常）
def gethtml(soup):
    data = soup.find_all("img")
    for x in data:
        path = "k:/asd/" + '%s.jpg' % time.time()
        fileurl = x.get("src")
        print(fileurl)
        try:
            urllib.request.urlretrieve(fileurl, path)
        except:
            pass


url = "http://www.baidu.com/"
queue = deque()
visited = set()
cnt = 0

queue.append(url)


while queue:
    url = queue.popleft()  # 队首元素出队
    visited |= {url}  # 标记为已访问

    print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
    cnt += 1

    try:
        urlop = urllib.request.urlopen(url)
    except:
        continue

    try:
        html = urlop.read().decode()
    except:
        pass
    soup = BeautifulSoup(html)
    data = gethtml(soup)
    # print(data)

    for x in soup.find_all('a'):  
    # 这里提现引入beautifulsoup 的方便之处  可以直接解析html 拿到elm 
    #这个是beautifulsoup 文档可以看下　https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id37 
        try:
            if 'http' in x.get("href") and x.get("href") not in visited:
                queue.append(x.get("href"))
                print('加入队列 --->  ' + x.get("href"))

        except:
            pass

print("----------------------end-------------------")