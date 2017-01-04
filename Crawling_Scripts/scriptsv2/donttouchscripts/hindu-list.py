import pickle
import nltk
import requests,bs4,os
print "remove hindu-list.txt"
f=open('hindu-list.txt','ab')
for i in range(1,31):
	if i>=10:
		url="http://www.thehindu.com/archive/web/2015/09/"+str(i)+"/"
	else:
		url="http://www.thehindu.com/archive/web/2015/09/0"+str(i)+"/"
	res=requests.get(url)
	res.raise_for_status()
	im=bs4.BeautifulSoup(res.text)
	heading=im.select('.archiveWebListHolder')
	print len(heading)
	for k in heading :
		print k
	break


