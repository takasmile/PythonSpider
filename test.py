import urllib.request  #python3.6中url请求模块只能用这种方式导入，其他方式亲测失败。。。
from bs4 import BeautifulSoup  #同上，python3.6中的beautifulsoup导入方式，其他方式亲测失败。。。
import re
import time
with open('ipresult.txt', 'w') as out:  #创建并打开结果存储文本
    with open('ipurl.txt', 'r') as list:  #打开已经存在的需查询域名文本
        for data in list:  #以下为打印出所查询域名以及分割线
            print('-' * 50, file=out)
            print("网站域名", data, file=out)
            url = "http://www.hao123.com/"  #查询请求网址
            full_url = url + data  #构造每个域名的查询url
            data = urllib.request.urlopen(full_url).read()  #发起请求并读取回应
            data = data.decode('UTF-8')
            soup = BeautifulSoup(data, "html.parser")  #使用beautifulsoup分析回应
            #time.sleep(20)
            #以下为抓取回的页面中涉及ip地址及物理位置的html内容，根据其中的标签及class提取出想要的内容
            for link in soup.find_all(
                    'span'):  #此for循环为通过匹配html标签“span”，大体定位ip地址
                text_span = link.get_text()
                ip_finder = re.compile(r'(\d{1,3}\.){3}\d{1,3}')  #此处正则匹配ip地址
                ip = ip_finder.search(text_span)
                if ip:
                    print("IP地址为：", ip.group(), file=out)  #正则导出ip地址内容
                lo_finder = link.get(
                    'class')  #使用lo_finder代表从span标签中提取出全部class标签
                lo_class = [
                    'Whwtdhalf', 'w50-0'
                ]  #观察以上html发现标记物理位置的class为class="Whwtdhalf w50-0"，与其他class明显不同，故作if判断进一步提取，但是此时还有（IP的物理位置）这一文本内容也是此class
                if lo_finder == lo_class:
                    lo_text = link.get_text()
                    #print(lo_text)
                    if lo_text != 'IP的物理位置':  #排除相同class标签的另一文本内容（IP的物理位置），即可提取出想要的物理位置
                        print("服务器位于", lo_text, file=out)
                    #lo_patten = re.compile(r'')
                    #lo = lo_patten.match(lo_text)
                    #if lo :
                    #   print("服务器位于",lo.group(),file=out)
                    #print(lo,file=out)
    print('-' * 50, file=out)
print("运行结束")