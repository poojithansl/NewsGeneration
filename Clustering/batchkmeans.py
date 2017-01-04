from time import time
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn import metrics

dat=open('toi.p','r')
clusters=open('clusters/jk.p','wb')
datai=pickle.load(dat)
datas=datai['content']
titles=datai['title']
dataseto=map((lambda x,y: x+' '+y),titles,datas)
true_k=20
print("true_k %d" %true_k)
vectorizer = TfidfVectorizer(max_df=0.5, max_features=opts.n_features,
                                 min_df=2, stop_words='english',
                                 use_idf=opts.use_idf)
print("TFIDF")
X = vectorizer.fit_transform(dataseto)

print("done in %fs" % (time() - t0))
print("n_samples: %d, n_features: %d" % X.shape)
print()
mit={'title':[],'content':[]}
dit={}
if True:
    km = MiniBatchKMeans(n_clusters=true_k, init='k-means++', n_init=1,
                         init_size=1000, batch_size=1000, verbose=opts.verbose)
    clu=km.fit_predict(X)
    print(X.shape)
    print("clu.shape %d\n" %clu.shape)
    cluster_0 = np.where(clu==0)
    for k in range(true_k):
	pooj=np.where(clu==k)
	#print(pooj)
	#print(k)
	dit[k]=mit
	for jk in pooj[0]:
		print("jk %s\n"%jk)
		dit[k]['title'].append(titles[jk])
		dit[k]['content'].append(datas[jk])
		#print("%s\n" %dataseto[jk])
	
    #print(clu[0])
    #print(cluster_0[0])
    #for phi in range(len(cluster_0))
    #for jer in cluster_0[0]:
	#print("jer %s\n"% jer)
        #print("%s\n"% dataseto[jer])
    X_cluster_0 = X[cluster_0]
    pickle.dump(dit,clusters)
    print(X_cluster_0)
print("Clustering sparse data with %s" % km)
t0 = time()
km.fit(X)
print("done in %0.3fs" % (time() - t0))
if True:
    print("Top terms per cluster:")

    if opts.n_components:
        original_space_centroids = svd.inverse_transform(km.cluster_centers_)
        order_centroids = original_space_centroids.argsort()[:, ::-1]
    else:
        order_centroids = km.cluster_centers_.argsort()[:, ::-1]

    terms = vectorizer.get_feature_names()
    for i in range(true_k):
        print("Cluster %d:" % i, end='')
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind], end='')
        print()
