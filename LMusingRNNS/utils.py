import tensorflow as tf
import numpy as np
import re
import collections
import os
import pickle

class InputText():
    def __init__(self,batch_size,seq_length):
        input_file="input.txt"
        vocab_file="vocab.pkl"
        tensor_file="tensor.npy"
        if not os.path.exists(vocab_file):
            print("preprocessing ")
            self.preprocess(input_file,vocab_file,tensor_file)
        else:
            print("Loading the vocab and tensor files")
            self.load_preprocessed(vocab_file,tensor_file)
        ##
        self.num_batches=int(self.tensor.size / (self.batch_size *self.seq_length))
        self.tensor=self.tensor[:self.num_batches * self.batch_size * self.seq_length]
        xdata=self.tensor
        ydata=np.array([0]*len(xdata)
        ydata[:-1]=xdata[1:]
        ydata[-1]=xdata[0]
        self.x_batches = np.split(xdata.reshape(self.batch_size, -1), self.num_batches, 1)
        self.y_batches = np.split(ydata.reshape(self.batch_size, -1), self.num_batches, 1)
        print("Batches Created")
        self.reset_batch_pointer()
    def reset_batch_pointer(self):
        self.batch_pointer=0
    def next_batch(self):
        x=self.x_batches[self.pointer]
        y=self.y_batches[self.pointer]
        self.pointer+=1
        #print("Next batch")
        return self.pointer
    def load_preprocessed(self,vocab_file,tensor_file):
        with open(vocab_file,'rb') as f:
            self.words=pickle.load(f)
        self.vocab_size=len(self.words)
        self.vocab=dict(zip(self.words,range(self.vocab_size))
        self.tensor=np.load(tensor_file)
        self.num_batches=int(self.tensor.size / (self.batch_size *
                                                   self.seq_length))
    def clean_data(self,string):
        string = re.sub(r"[^가-힣A-Za-z0-9(),!?\'\`]", " ", string)
        string = re.sub(r"\'s", " \'s", string)
        string = re.sub(r"\'ve", " \'ve", string)
        string = re.sub(r"n\'t", " n\'t", string)
        string = re.sub(r"\'re", " \'re", string)
        string = re.sub(r"\'d", " \'d", string)
        string = re.sub(r"\'ll", " \'ll", string)
        string = re.sub(r",", " , ", string)
        string = re.sub(r"!", " ! ", string)
        string = re.sub(r"\(", " \( ", string)
        string = re.sub(r"\)", " \) ", string)
        string = re.sub(r"\?", " \? ", string)
        string = re.sub(r"\s{2,}", " ", string)
        return string.strip().lower()
    def get_vocab(self,text):
        wordict=collections.Counter(text)
        print(wordict)
        vocabulary_words=[x for x in wordict.keys()]
        vocabulary_words=list(sorted(vocabulary_words))
        vocabulary={x:i for i,x in enumerate(vocabulary_words)}
        print(vocabulary)
        vocab_len=len(vocabulary)
        return vocabulary,vocabulary_words,vocab_len
    def preprocess(self,input_file,vocab_file,tensor_file):
        with open(input_file,"r") as f:
            data=f.read()
        data=self.clean_data(data)
        #print(data)
        ##
        self.vocab,self.words,self.vocab_size=self.get_vocab(data)
        with open(vocab_file,'wb') as f:
            pickle.dump(self.words,f)
        self.tensor=np.array(list(map(self.vocab.get,data)))
        np.save(tensor_file,self.tensor)
