# =============================================================================
# 程序名: ku_gogu_music.py
# 功能: 批量下载酷狗音乐的试听片段
# 作者: afeng
# 日期: 2024-09-23
# 描述：
#
# 例子：
# =============================================================================

import requests
import time
import execjs
import datetime
import json

# =============================================================================

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'referer' : 'https://www.kugou.com/'
}
keyword = '周杰伦'
page = '1'

# =============================================================================

# 执行js逆向代码
jscode = None
with open('酷狗音乐/ku_gou.js', 'r', encoding='utf8') as f:
    jscode = f.read()
myjs = execjs.compile(jscode)
mid = myjs.call('GetMid')

timestamp = str(int(time.time() * 10000))
u = {
    "appid": "1014",
    "platid": 4,
    "clientver": 0,
    "clienttime": timestamp,
    "signature": "",
    "mid": mid,
    "uuid": "1b3b62c4c25a2a74c07c91edb73e2b0e",
    "userid": 0,
    "p.token": ""
}
signature = myjs.call('signatureParam', u, '1014')

dt = datetime.datetime.now().strftime('%Y-%m-%d')
time_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
formdata = myjs.call('getFormData', dt, time_str, mid)

# =============================================================================

# dfid是从请求中带过来的，不是js代码生成的
params = {
    'appid' : '1014',
    'platid' : '4',
    'clientver' : '0',
    'clienttime' : timestamp, 
    'signature' : signature,
    'mid' : mid,
    'userid' : '0',
    'uuid' : '1b3b62c4c25a2a74c07c91edb73e2b0e',
    'p.token' : '',
}
response = requests.post('https://userservice.kugou.com/risk/v1/r_register_dev', headers=headers, params=params, data=formdata)
dfid = response.json()['data']['dfid']
# print(dfid)

# =============================================================================

# 'encode_album_audio_id' : '10qgrdcc',
# 生成 请求里的signature参数
timestamp = str(int(time.time() * 1000))
s = [
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt",
    "appid=1014",
    "bitrate=0",
    "callback=callback123",
    f"clienttime={timestamp}",
    "clientver=1000",
    f"dfid={dfid}", 
    "filter=10",
    "inputtype=0",
    "iscorrection=1",
    "isfuzzy=0",
    f"keyword={keyword}",
    f"mid={mid}",
    f"page={page}",
    "pagesize=30",
    "platform=WebFilter",
    "privilege_filter=0",
    "srcappid=2919",
    "token=",
    "userid=0",
    f"uuid={mid}",
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
]
signature = myjs.call('calcMD5', s)

# =============================================================================

# 'encode_album_audio_id' : '10qgrdcc', # ?
# 从上个页面获取10qgrdcc

params = {
    'callback' : 'callback123',
    'srcappid' : '2919',
    'clientver' : '1000',
    'clienttime' : timestamp, # ?
    'mid' : mid,  # ?
    'uuid' : mid,  # ?
    'dfid' : dfid,
    'keyword' : keyword,  # ?
    'page' : page,  # ?
    'pagesize' : '30',
    'bitrate' : '0',
    'isfuzzy' : '0',
    'inputtype' : '0',
    'platform' :  'WebFilter',
    'userid' : '0',
    'iscorrection' : '1',
    'privilege_filter' : '0',
    'filter' : '10',
    'token' : '',
    'appid' : '1014',
    'signature' : signature,  # ?
}
response = requests.get('https://complexsearch.kugou.com/v2/search/song', headers=headers, params=params)

#print(response.text[response.text.find('{') : -2])
#print(response.text)

json_str = response.text[response.text.find('{') : -2]
json_data = json.loads(json_str)
#print(type(json_data))

for song_info in json_data['data']['lists']:
    song_id = song_info['EMixSongID']
    song_name = song_info['FileName']
    print(f'正在下载 {song_name}')
    clienttime = str(int(time.time() * 1000))
    s = [
        "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt",
        "appid=1014",
        f"clienttime={clienttime}",
        "clientver=20000",
        f"dfid={dfid}",
        f"encode_album_audio_id={song_id}",
        f"mid={mid}",
        "platid=4",
        "srcappid=2919",
        "token=",
        "userid=0",
        f"uuid={mid}",
        "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
    ]
    signature = myjs.call('calcMD5', s)
    params = {
        'srcappid' : '2919',
        'clientver' : '20000',
        'clienttime' : clienttime,
        'mid' : mid, 
        'uuid' : mid, 
        'dfid' : dfid, 
        'appid' : '1014',
        'platid' : '4',
        'encode_album_audio_id' : song_id, 
        'token' : '',
        'userid' : '0',
        'signature' : signature, 
    }
    response = requests.get('https://wwwapi.kugou.com/play/songinfo', headers=headers, params=params)
    play_url = response.json()['data']['play_url']
    audio_name = response.json()['data']['audio_name']
    with open(f'酷狗音乐/songs/{audio_name}.mp3', 'wb') as f:
        response = requests.get(play_url, headers=headers)
        f.write(response.content)
    print(f'{song_name} 下载完成')