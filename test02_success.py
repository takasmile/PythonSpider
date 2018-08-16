import urllib.request
from bs4 import BeautifulSoup

url1 = 'http://bbs.ustc.edu.cn/cgi/bbstdoc?board=PieBridge&Start=3558'
fp = urllib.request.urlopen(url1)
s = fp.read()
soup = BeautifulSoup(s, features='html5lib')
polist = soup.findAll('span')
print(polist[0].contents[0])
