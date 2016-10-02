import pickle
g=open('toi.p','rb')
lo=pickle.load(g)
print lo
print len(lo['title']),len(lo['content'])
