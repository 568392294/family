#coding=utf-8
import urllib.request

#keywd='hello'
url='http://www.baidu.com'
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()
fhandle=open("D://python/html/4.html","wb")
fhandle.write(data)
print(data)
fhandle.close()