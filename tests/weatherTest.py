import urllib
import urllib.request
import re


def load_page(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data


def get_image(html):
    regx = r'http://[\S]*jpg'
    pattern = re.compile(regx)
    get_image = re.findall(pattern, repr(html))

    num = 1
    for img in get_image:
        image = load_page(img)
        with open(
                'C:\\Users\\Alex\\Documents\\GitHub\\PythonSpider\\image\\%s.jpg'
                % num, 'wb') as fb:
            fb.write(image)
            print('downloading the %s th image' % num)
            num += 1
    print('downloading complete')


url = 'http://p.weather.com.cn/2017/06/2720826.shtml#p=1'
html = load_page(url)
get_image(html)
