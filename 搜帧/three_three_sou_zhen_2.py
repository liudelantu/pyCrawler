# =============================================================================
# 程序名: three_three_sou_zhen_2.py
# 功能: 批量下载与关键字匹配的视频
# 作者: afeng
# 日期: 2024-10-05
# 描述：js逆向
#
# 例子：
# =============================================================================

import requests
import time
import execjs

# =============================================================================

keyword = '机器人'
ts = str(int(time.time() * 1000) - 9999)
page = 3

e = f'_platform=web,_ts={ts},_versioin=0.2.5,keyword={keyword},limit=12,page={page},'

jscode = None
with open('搜帧/three_three_sou_zhen_2.js', 'r', encoding='utf8') as f:
    jscode = f.read()
myjs = execjs.compile(jscode)
result = myjs.call('getXSignature', e)

# =============================================================================

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-signature' : result
}
params = {
    'keyword' : keyword, # ?
    'page' : page,  # ?
    'limit' : '12',
    '_platform' : 'web',
    '_versioin' : '0.2.5',
    '_ts' : ts, # ?
}

# =============================================================================
response = requests.get('https://fse-api.agilestudio.cn/api/search', headers=headers, params=params)
print(response.text)