import pickle
import nltk
import requests,bs4,os
print "remove toi-list.txt"
f=open('toi-list.txt','ab')
for i in range(42248,42278):
	url="http://timesofindia.indiatimes.com/2015/9/1/archivelist/year-2015,month-9,starttime-"+str(i)+".cms"
	res=requests.get(url)
	res.raise_for_status()
	im=bs4.BeautifulSoup(res.text)
	heading=im.select('td > span > a')
	#print heading
	print i-42247,len(heading)
	for m in heading:
		hurl=m.get('href')
		#print hurl
		f.write(hurl+"\n")
	
f.close()
