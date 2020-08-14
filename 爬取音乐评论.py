
import requests
# 引用requests模块
url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'

for i in range(5):
    params = {
'g_tk':'5381',
'loginUin':'0',
'hostUin':'0',
'format':'json',
'inCharset':'utf8',
'outCharset':'GB2312',
'notice':'0',
'platform':'yqq.json',
'needNewCode':'0',
'cid':'205360772',
'reqtype':'2',
'biztype':'1',
'topid':'102065756',
'cmd':'6',
'needmusiccrit':'0',
'pagenum':str(i),
'pagesize':'15',
'lasthotcommentid':'song_102065756_3202544866_44059185',
'domain':'qq.com',
'ct':'24',
'cv':'10101010'
}
res_comments = requests.get(url,params=params)
json_comments = res_comments.json()
list_comments = json_comments['comment']['commentlist']
for comment in list_comments:
    print(comment['rootcommentcontent'])