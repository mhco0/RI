import numpy as np
import math
import re
import unidecode
import nltk
import json

def tokenize(text):
        nltk.download('punkt')
        from nltk.tokenize import word_tokenize

        nltk.download('stopwords')
        from nltk.corpus import stopwords
        text = unidecode.unidecode(text)
        text = re.sub('[^A-Za-z]', ' ', text)
        text = text.lower()

        #print(text)
        tokenized_text = word_tokenize(text)
        for word in tokenized_text:
            if word in stopwords.words('portuguese'):
                tokenized_text.remove(word)
        
        s_text = " ".join(tokenized_text)
        
        return(s_text)

class Ranker():
    def __init__(self):
        self.postings = json.load(open('postings.json'))
        self.N = 100

    def score(self, q):
        query = ""
        for x in q:
            if x[0]!= 'words' and x[1] != '':
                query+=x[0]+'.'+x[1]+' ' 
            else:
                query+=x[1]
        
        query = tokenize(query)
        scores = np.zeros(self.N*2)

        terms_in_query = list(set(query.split(' ')))
        
        for s in terms_in_query:
            if s in self.postings:
                docs = self.postings[s]
                for d in docs:
                    scores[d[0]] += d[1]*query.count(s)

        for i in range(0, len(scores)):
            scores[i] = scores[i]/self.N

        return scores
    
    def tf_idf(self, freq, term):
        
        if term in self.postings:
            return freq*math.log(self.N/freq, 2)
        else:
            return 0
    
    def score_tfidf(self, q):
        query = ""
        for x in q:
            if x[0]!= 'words' and x[1] != '':
                query+=x[0]+'.'+x[1]+' ' 
            else:
                query+=x[1]
        
        query = tokenize(query)
        scores = np.zeros(self.N*2)

        terms_in_query = list(set(query.split(' ')))
        
        for s in terms_in_query:
            if s in self.postings:
                docs = self.postings[s]
                for d in docs:
                    scores[d[0]] += self.tf_idf(d[1], s)*self.tf_idf(query.count(s), s)

        for i in range(0, len(scores)):
            scores[i] = scores[i]/self.N

        return scores

r = Ranker()
qx = [('author', 'rooney'), ('publisher', ''), ('language', ''), ('isbn', ''), ('words', 'smash')]

s = r.score(qx)
s_sorted = sorted(range(len(s)), key=lambda k: s[k], reverse=True)

print(s_sorted[0:5])
