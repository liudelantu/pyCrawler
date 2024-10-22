# =============================================================================
# 程序名: baidu_images.py
# 功能: 批量下载与关键字匹配的图片
# 作者: afeng
# 日期: 2024-10-22
#
# 例子：
# 请输入关于图片的关键词: 机器人
# 你想下载多少页的图片(一页30张图片): 10
# =============================================================================

import requests
import time
import os
import re

# =============================================================================

keyword = input("请输入关于图片的关键词:")
pages = input("你想下载多少页的图片(一页30张图片):")
#keyword = '杯子'
#pages = '1'

# =============================================================================

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

# =============================================================================

# 创建 图片的存储位置
cur_dir = os.path.dirname(os.path.abspath(__file__))

images_dir = os.path.join(cur_dir, 'images')
keyword_dir = os.path.join(images_dir, keyword)

if not os.path.exists(images_dir):
    os.makedirs(images_dir)
if not os.path.exists(keyword_dir):
    os.makedirs(keyword_dir)

# =============================================================================

for page in range(int(pages)):
    params = {
        'tn' : 'resultjson_com',
        'logid' : '8777705988266505980',  
        'ipn' : 'rj',
        'ct' : '201326592',
        'is' : '',
        'fp' : 'result',
        'fr' : 'ala',
        'word' : keyword,  # 搜索的关键字
        'queryWord' : keyword,  # 搜索的关键字
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
        'pn' : str(page * 30),  # 翻页相关
        'rn' : '30',
        f'{int(time.time() * 1000)}' : '',   # 时间戳
    }

    print(f'开始下载第 {page+1} 页的图片.....')

    response = requests.get('https://image.baidu.com/search/acjson', headers=headers, params=params)
    
    for info in response.json()['data']:
        img_url = None
        cleaned_img_name = None

        if len(info) > 0:
            # 获取图片名字
            img_name = info['fromPageTitle']
            if len(img_name) > 0:
                cleaned_img_name = re.sub(r'[^a-zA-Z\u4e00-\u9fa5]', '', img_name)
            else:
                cleaned_img_name = f'{int(time.time() * 1000)}'
            
            # 获取图片的URL
            img_url = info['objURL']
            if 'http' not in img_url or 'https' not in img_url:
                img_url = info['middleURL']
            
            # 下载图片
            with open(f'{keyword_dir}/{cleaned_img_name}.jpg', 'wb') as f:
                response = requests.get(img_url, headers=headers)
                f.write(response.content)
            print('下载完成', cleaned_img_name)
# =============================================================================
# END
# =============================================================================