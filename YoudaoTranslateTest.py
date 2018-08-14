from urllib import request
from urllib import parse
import json

if __name__ == '__main__':
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    Form_Data = {}
    Form_Data['action'] = 'FY_BY_CLICKBUTTION'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['doctype'] = 'json'
    Form_Data['from'] = 'AUTO'
    Form_Data['i'] = 'jack'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['salt'] = '1534248847269'
    Form_Data['sign'] = 'bb8b5bf5361f502a6e2469f1096fcd83'
    Form_Data['smartresult'] = 'dict'
    Form_Data['to'] = 'AUTO'
    Form_Data['typoResult'] = 'false'
    Form_Data['version'] = '2.1'

    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(Request_URL, data)
    html = response.read().decode('utf-8')
    translate_results = json.loads(html)
    translate_results = translate_results['translateResult'][0][0]['tgt']
    print('the result is ', translate_results)