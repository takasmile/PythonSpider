from urllib import request
from urllib import error
import re
import itertools

def download(url, user_agent='wswp', num_retries=2):
    print('Downloading: ', url)
    headers = {'User-agent': user_agent}
    req = request.Request(url, headers = headers)
    try:
        html = request.urlopen(req).read()
    except error.URLError as e:
        print('Download error: ', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_retries-1)
    return html

#def crawl_sitmap(url):
#   sitemap = download(url)
#   links = re.findall('<loc>(.*?)</loc>', sitemap)
#   for link in links:
#       html = downloas(link)

num_errors = 0
max_errors = 5
for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/-%d' % page
    html = download(url)
    if html == None:
        print('Error occured!')
        num_errors += 1
        if num_errors == max_erorrs:
            break
    else:
        num_errors = 0
