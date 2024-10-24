# =============================================================================
# 程序名: three_three_sou_zhen_1.py
# 功能: 批量下载与关键字匹配的视频
# 作者: afeng
# 日期: 2024-10-05
#
# 例子：
# =============================================================================

import requests
import time
import hashlib

# =============================================================================

# _platform=web,_ts=1729602460221,_versioin=0.2.5,keyword=火车呼啸而过,limit=12,page=16,
# 算出一个md5
keyword = '机器人'
ts = str(int(time.time() * 1000) - 9999)
page = 1
e = f'_platform=web,_ts={ts},_versioin=0.2.5,keyword={keyword},limit=12,page={page},'
obj = hashlib.md5()
obj.update(e.encode('utf8'))
x_signature = obj.hexdigest()

# =============================================================================

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-signature' : x_signature
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

for info in response.json()['data']['list']:
    m3u8_url = info['video']['url']            # https://ssv-video.agilestudio.cn/942_9syz0w/942_9syz0w.m3u8
    ts_url = m3u8_url[:m3u8_url.rfind('/')+1]  # https://ssv-video.agilestudio.cn/942_9syz0w/
    mp4_name = info['video']['rawUrl']

    # 获取所有.ts片段
    response = requests.get(m3u8_url, headers=headers)
    m3u8_data = response.text
    
    print("正在下载：" + mp4_name)

    with open(mp4_name, 'wb') as f:
        for line in m3u8_data.split('\n'):
            # 遍历一个视频的所有.ts片段
            if '.ts' in line:
                ts_url += line                 # https://ssv-video.agilestudio.cn/942_9syz0w/ + 4688_6ddf5a-00016.ts
                response = requests.get(ts_url, headers=headers)
                f.write(response.content)
                print(f'{line} 已经下载完成')

# https://ssv-video.agilestudio.cn/342_20277091_1_7b94e9/342_20277091_1_7b94e9.m3u8

# https://ssv-video.agilestudio.cn/342_20277091_1_7b94e9/342_20277091_1_7b94e9228.ts
#                                                        4688_6ddf5a-00001.ts 