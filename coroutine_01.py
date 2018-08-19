# corotine µÄ gevent°ü²âÊÔ
from gevent import monkey;monkey.patch_all()
import gevent
import urllib
import urllib.request

def run_task(url):
    print('Visit --> %s' % url)
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        print('%d bytes recieved from %s.' % (len(data), url))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    urls = ['https://github.com/', 'https://www.python.org/', 'https://www.cnblogs.com/']
    # spawn£ºcreate corotine
    greenlets = [gevent.spawn(run_task, url) for url in urls]
    # joinall: add these corotine task and start to run them
    gevent.joinall(greenlets)
