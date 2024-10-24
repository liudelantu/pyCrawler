import requests  # 请求数据
from bs4 import BeautifulSoup  # 解析数据
import pandas as pd  # 保存数据

headers = {
    'referer' : 'https://ssr1.scrape.center/',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

# response = requests.get('https://p0.meituan.net/movie/283292171619cdfd5b240c8fd093f1eb255670.jpg@464w_644h_1e_1c', headers=headers)
#
# with open('test.jpg', 'wb') as f:
#     f.write(response.content)
cnt = 0
movies = {'name':[], 'type':[], 'city':[], 'time':[], 'year':[], 'score':[]}
for page in range(1, 11):
    print('正在处理第 %d 页的数据' % page)
    response = requests.get('https://ssr1.scrape.center/page/%d' % page, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all(name='div', class_='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16')

    for i in range(len(results)):
        movies['name'].append(results[i].h2.string)
        #print(results[i].h2.string, end=';')
        cnt += 1
        bnt_list = results[i].find_all(name='button', class_='el-button category el-button--primary el-button--mini')
        movies_type = ''
        for bnt in bnt_list:
            movies_type += bnt.span.string + ','
            #print(bnt.span.string, end='/')
        movies['type'].append(movies_type)
        #print('', end=';')
        maps = results[i].find_all(name='div', class_='m-v-sm info')
        span_list = maps[0].find_all(name='span')
        movies['city'].append(span_list[0].string)
        movies['time'].append(span_list[2].string)
        span_list = maps[1].find_all(name='span')
        if len(span_list) > 0:
            movies['year'].append(span_list[0].string)
        else:
            movies['year'].append('')
        # for map in maps:
        #     span_list = map.find_all(name='span')
        #     for s in span_list:
        #         if s.string != ' / ':
        #             print(s.string, end=';')
        # print('')
        score = soup.find_all(name='p', class_='score m-t-md m-b-n-sm')
        movies['score'].append(score[i].string.strip())

print('总共爬取了 %d 条电影数据' % cnt)

data = pd.DataFrame(movies)
data.to_excel('moves.xlsx', index=False)
