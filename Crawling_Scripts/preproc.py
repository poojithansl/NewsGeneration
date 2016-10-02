from gensim import corpora, models, similarities 
import pickle,nltk
stopwords = nltk.corpus.stopwords.words('english')
import string
f=open('toi.p','rb')
prep=open('prep/toi.p','wb')
jer={'title':[],'content':[]}
loa=pickle.load(f)
def strip_proppers(text):
	# first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
	tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent) if word.islower()]
	#print "tokens",tokens
	return "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()
#print loa['content']
for k in range(len(loa['content'])):
		#m=[strip_proppers(loa['title'][k])]
		m1=[strip_proppers(loa['content'][k])]
		#print m,m1
		#t=[word for word in m if word not in stopwords]
		t1=[word  for word in m1 if word not in stopwords]
		#print t1
		jer['title'].append(loa['title'][k])
		jer['content'].append(t1[0])
		if k%10==0:
			print k
		#break
pickle.dump(jer,prep)
prep.close()
