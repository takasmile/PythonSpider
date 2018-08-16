import urllib
import urllib.request


def load_page(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    print('the data is: ', data)


def testFunc():
    if(__name__):
        print('we are in %s' % __name__)


if __name__ == '__main__':
    testFunc()