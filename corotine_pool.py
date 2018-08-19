from gevent import monkey
monkey.patch_all()
import urllib.request
import urllib
from gevent.pool import Pool

def run_task(url):
    print('Visit --> %s' % url)
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        print('%d bytes recevied from %s.' % (len(data), url))
    except Exception as e:
        print(e)
    return 'url: %s ---> finish' % url

if __name__ == '__main__':
    pool = Pool(2)
    urls = ['https://github.com', 'https://www.python.org', 'https://www.cnblogs.com/']
    results = pool.map(run_task, urls)
    print(results)
