#coding=utf-8
import urllib.request

keywd='hello'
url='http://www.baidu.com/s?wd='+keywd
req=urllib.request.Request(url)
