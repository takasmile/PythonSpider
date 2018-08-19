# python3中urllib与urllib2已经整合在一起
import urllib.request
response = urllib.request.urlopen('http://www.zhihu.com')
html = response.read()
print(html)
