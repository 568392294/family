import re
import urllib.request

def craw(url,page):
	html1=urllib.request.urlopen(url).read()
	html1=str(html1)
	pat1='<div class="MeinvTuPianBox">.+?<div class="hr10">'
	result1=re.compile(pat1).findall(html1)
	result1=result1[0]
	#print(result1)
	pat2='<a href="http://(.{10,50}?\.html)"'
	imagelist=re.compile(pat2).findall(result1)
	imagelist_new=list(set(imagelist))
	imagelist_new.sort(key=imagelist.index)
	#print(imagelist)
	for imageurl in imagelist_new:
		imageurl="http://"+imageurl
		#print(imageurl)
		html2=urllib.request.urlopen(imageurl).read()
		html2=str(html2)
		pat3='<div class="articleV4Body" id="picBody">.+?</div>'
		result2=re.compile(pat3).findall(html2)
		result2=result2[0]
		#print(result2)
		pat4='src="http://(.+?\.jpg)"'
		img_lj=re.compile(pat4).findall(result2)
		img_lj=img_lj[0]
		img_dir="D:/python/urllib/img/"+img_lj[-13:]
		img_url="http://"+img_lj
		try:
			urllib.request.urlretrieve(img_url,filename=img_dir)
			print(img_url)
		except urllib.error.URLError as e:
			if hasattr(e,"code"):
				print(e.code)
			if hasattr(e,"reason"):
				print(e.reason)
	# x=1
	# for imageurl in imagelist:
	# 	print(imageurl)
	# 	imagename="D:/python/urllib/img/"+str(page)+str(x)+".jpg"
	# 	imageurl="http://"+imageurl
	# 	try:
	# 		urllib.request.urlretrieve(imageurl,filename=imagename)
	# 	except urllib.error.URLError as e:
	# 		if hasattr(a,"code"):
	# 			x+=1
	# 		if hasattr(a,"reason"):
	# 			x+=1
	# 	x+=1
#for i in range(1,2):
	#url="http://www.27270.com/ent/meinvtupian/list_11_"+str(i)+".html"
#url="https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page=1&s=1&click=0"
url="http://www.27270.com/ent/meinvtupian/list_11_1.html"
craw(url,1)