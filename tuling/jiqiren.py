import requests
import json

key = '45f281bb0a65492ba4fa5f68471a8028'
while True:
    url = 'http://www.tuling123.com/openapi/api?key=' + key + '&info=' + input('我：')

    resp = requests.get(url)
    data = json.loads(resp.text)
    print('机器人：' + data['text'])
