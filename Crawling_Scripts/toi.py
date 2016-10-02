#!/usr/bin/python
import pickle
import nltk
import requests,bs4,os
url="http://timesofindia.indiatimes.com/2015/9/1/archivelist/year-2015,month-9,starttime-42248.cms"
if not os.path.exists('omarticles'):
	os.makedirs('omarticles')
imFile=open(os.path.join('omarticles','corpus.p'),'wb')
mg=[]
f=open('toi.p','wb')
cnt=0
mnt=0
kl=0
jer={'title':[],'content':[]}
#stopwords = nltk.corpus.stopwords.words('english')
if 1:
	res=requests.get(url)
	res.raise_for_status()
	im=bs4.BeautifulSoup(res.text)
	heading=im.select('td > span > a')
	
	for m in heading:
		try:
			hurl=m.get('href')
			resp=requests.get(hurl) 
			resp.raise_for_status()
			im=bs4.BeautifulSoup(resp.text)
			kn=im.select('.Normal')
		
			if kn==[]:
				cnt+=1
				pass
			if kn!=[]:
				mnt+=1
				phi=kn[0].getText()
				gn=im.select('.heading1')
				#print gn[0].getText()
				jer['title'].append(gn[0].getText())
				jer['content'].append(phi)
				#print phi
			kl+=1
			if kl%10==0:
				print kl
		except :
			print "Pagenotfound"
pickle.dump(jer,f)
print cnt,mnt	
f.close()
