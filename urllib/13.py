from urllib.request import urlopen
from urllib import request
import urllib.parse
import http.cookiejar
import os

headers	={
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        #'Connection':'keep-alive',
        'Host': 'www.yika66.com',
        'Origin': 'http://www.yika66.com',
        'Referer':' http://www.yika66.com/Login.aspx?act=logout',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest'
}
data={
    'type': 'login',
    'username': 'vipqjt',
    'password':'cb242873',
    'logintype':'0'
    }
data=urllib.parse.urlencode(data).encode('utf-8')

#将cookie保存在本地，并命名为cookie.txt
cookie_filename = 'cookie.txt'
cookie_aff = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie_aff)
opener = urllib.request.build_opener(handler)

req=request.Request('http://www.yika66.com/UserManage/action.aspx',headers=headers,data=data,method="POST")
try:
    response=opener.open(req)
except urllib.error.URLError as e:
    print(e.reason)

cookie_aff.save(ignore_discard=True,ignore_expires=True)
#打印出cookie
for item in cookie_aff:
    print('Name='+item.name)
    print('Value='+item.value)

headers1={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Connection':'keep-alive',
    'Host': 'www.yika66.com',
    'Upgrade-Insecure-Requests': '1',
    'Referer':'http://www.yika66.com/Login.aspx?act=logout',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.9'
}
index=request.Request('http://www.yika66.com/userManage/index.aspx',headers=headers1)
get_response=opener.open(index)
html=get_response.read()
print(html.decode('utf-8'))
path=os.getcwd()
f=open(path+'\\111.html','wb')
f.write(html)
f.close()
