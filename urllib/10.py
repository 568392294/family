#coding=utf-8
import urllib.request
import re
from selenium import webdriver

url="http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml"
# header={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
# }
# req=urllib.request.Request(url,headers=header)
driver = webdriver.PhantomJS()
driver.get(url)
data = driver.title
html=driver.page_source
# html=urllib.request.urlopen(req).read()
# html=html.decode("utf-8")
pat1='<tr.*?>(.*?)</tr>'
result1=re.compile(pat1).findall(html)
if bool(result1):
    print(len(result1))
    for td_result in result1:
        pat2='<td.*?>(.*?)</td>'
        td_list=re.compile(pat2).findall(td_result)
        if bool(td_list):
            for td_value in td_list:
                print(td_value)
            print("-"*120)
else:
    print("没有匹配到数据！") 