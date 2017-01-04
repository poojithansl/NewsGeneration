import ijson
import json
f=open('toi-data.json','r')
#for line in f:
obj=json.load(f)
print len(obj['title']),"titles"
print len(obj['content']),"content"
#for k in obj:
#	print k
#	print 1
#print obj


