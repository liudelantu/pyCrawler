import requests
import time

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

# vscode 正则匹配，全局替换
# (\w+): (.*)?
# '$1' : '$2',
params = {
    'tn' : 'resultjson_com',
    'logid' : '8777705988266505980',
    'ipn' : 'rj',
    'ct' : '201326592',
    'is' : '',
    'fp' : 'result',
    'fr' : 'ala',
    'word' : '坤坤',
    'queryWord' : '坤坤',
    'cl' : '2',
    'lm' : '-1',
    'ie' : 'utf-8',
    'oe' : 'utf-8',
    'adpicid' : '',
    'st' : '',
    'z' : '',
    'ic' : '',
    'hd' : '',
    'latest' : '',
    'copyright' : '',
    's' : '',
    'se' : '',
    'tab' : '',
    'width' : '',
    'height' : '',
    'face' : '',
    'istype' : '',
    'qc' : '',
    'nc' : '',
    'expermode' : '',
    'nojc' : '',
    'isAsync' : '',
    'pn' : '60',
    'rn' : '30',
    'gsm' : '3c',
    '1729583044818' : '',
}

response = requests.get('https://image.baidu.com/search/acjson', headers=headers, params=params)

for info in response.json()['data']:
    img_url = None

    if len(info) > 0:
        # 获取图片的URL
        img_url = info['objURL']
        if 'http' not in img_url or 'https' not in img_url:
            img_url = info['middleURL']
        
        # 下载图片
        with open(f'百度图片/图片/{int(time.time() * 1000)}.jpg', 'wb') as f:
            response = requests.get(img_url, headers=headers)
            f.write(response.content)
        print('下载完成')
