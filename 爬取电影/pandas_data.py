import pandas as pd

# df = pd.read_excel('moves.xlsx')
# df = df.dropna()
#
# def clear_data(x):
#     return x[:x.find(' ')]
#
# df['name'] = df['name'].apply(clear_data)
# df['time'] = df['time'].apply(clear_data)
# df['year'] = df['year'].apply(clear_data)
#
# df.to_excel('new_moves.xlsx', index=False)

df2 = pd.read_excel('new_moves.xlsx')

# 获取电影时长最长的记录
# print(df2['time'].argmax())  # 电影的下标
# print(df2['time'].max())  # 时长的值
# print(df2.iloc[df2['time'].argmax()])

# 获取评分比总平均分高的电影
# print(df2['score'] > df2['score'].mean())
# print(df2[df2['score'] > df2['score'].mean()][['name', 'score']])

# 获取评分比总平均分高的电影,并且是包含中国的电影
# def hasChina(x):
#     return '中国' in x
# print(df2[df2['city'].apply(hasChina) & (df2['score'] > df2['score'].mean())])

# 获取评分比总平均分高的电影,并且是包含中国或日本的电影
# def hasChina(x):
#     return '中国' in x
# def hasJapan(x):
#     return '日本' in x
# print(df2[(df2['city'].apply(hasChina) | df2['city'].apply(hasJapan)) & (df2['score'] > df2['score'].mean())])

# 获取评分比总平均分高的电影,并且不是中国的电影
# def hasChina(x):
#     return '中国' in x
# print(df2[~df2['city'].apply(hasChina) & (df2['score'] > df2['score'].mean())])

# 统计有多少个上映时间是2000年及以后的电影
def getYear(x):
    return int(x[:4])
# print(df2[df2['year'].apply(getYear) >= 2000]['year'].count())

# 统计每一年上映了多少部电影
print(df2.groupby(df2['year'].apply(getYear)).count())