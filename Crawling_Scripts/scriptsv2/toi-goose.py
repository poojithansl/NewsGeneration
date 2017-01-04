from goose import Goose
import json
#remove toi-data.json
inf=open('toi-list.txt','r')
outf=open('toi-data.json','wb')
lines=inf.read().splitlines()
print len(lines),"lines"
g=Goose()
titles=[]
contents=[]
i=0
for line in lines:
	url=line
	article = g.extract(url=url)
	titles.append(article.title)
	contents.append(article.cleaned_text)
	i+=1
	if i%100==0:print i
dit={'title':titles,'content':contents}
print dit
json.dump(dit,outf)	
	

