import requests
from bs4 import BeautifulSoup
import hashlib
import time
import os

# ============================================================================

keyword = input("请输入关键字：")
#'胡彦斌'

# ============================================================================

# 加密伪造的请求数据
def createSign(r):
    r += '0b50b02fd0d73a9c4c8c3a781c30845f'
    return hashlib.md5(r.encode('utf8')).hexdigest()

# ============================================================================

# 发送请求
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}
response = requests.get('https://music.91q.com/search?word=%s' % keyword, headers=headers)

# ============================================================================

# 解析数据
soup = BeautifulSoup(response.text, 'html.parser')

# 翻页数量
page_tags = soup.find_all(name='li', class_='number')

total_pages = 0
if len(page_tags) == 0:
    total_pages = 1
else:
    total_pages = int(page_tags[-1].string)

# ============================================================================

for cur_page in range(1, total_pages+1):
    """ 处理所有页 """

    print("正在处理第 %d 页" % cur_page)

    # 伪造请求
    appid = '16073360'
    word = keyword
    timestamp = str(int(time.time()))
    r = 'appid=16073360&pageNo=%d&pageSize=20&timestamp=%s&type=1&word=%s' % (cur_page, timestamp, word)
    sign = createSign(r)
    params = {
        'sign':sign,
        'appid':appid,
        'word':word,
        'timestamp':timestamp,
        'type':'1',
        'pageNo':cur_page,
        'pageSize':'20'
    }
    response = requests.get('https://music.91q.com/v1/search', params=params)

    song_info = response.json()
    for track in song_info['data']['typeTrack']:
        # 伪造请求
        TSID = track['TSID']
        song_name = track['title']
        singer_name = ''
        for singer in track['artist']:
            singer_name += singer['name'] + '_'
        r = 'TSID=' + TSID + '&appid=' + appid + '&timestamp=' + timestamp
        sign = createSign(r)
        params = {
            'sign': sign,
            'appid': appid,
            'timestamp': timestamp,
            'TSID':TSID
        }
        response = requests.get('https://music.91q.com/v1/song/tracklink', params=params)

        info = response.json()
        if 'path' in info['data']:
            # 获取mp3文件地址
            response = requests.get(info['data']['path'])
            try:
                if not os.path.exists('./music/'):
                    os.mkdir('./music/')
                with open('./music/%s+%s.mp3' % (singer_name, song_name), 'wb') as f:
                    f.write(response.content)
                print(singer_name, song_name, "下载完成")
            except:
                print(singer_name, song_name, "文件名有问题")