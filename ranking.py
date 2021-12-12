import numpy as np
import math
import re
import unidecode
import nltk

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
        self.postings = {"livro" : [(np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0])],
        "grande" : [(np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0])],
        "sobre" : [(np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0])],
        "guerras" : [(np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0])],
        "vive" : [(np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0])],
        "fechado" : [(np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0])],
        "fome" : [(np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0])],
        "pensa" : [(np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0])],
        "pensador" : [(np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0])],
        "terror" : [(np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0])],
        "ficcao" : [(np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0])],
        "romance" : [(np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0])],
        "infantil" : [(np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0])],
        "politica" : [(np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0]), (np.random.randint(0,20,1)[0], np.random.randint(1,20,1)[0])]}

    def score(self, query):
        query = tokenize(query)
        print(query)
        scores = np.zeros(20)

        terms_in_query = list(set(query.split(' ')))
        
        for s in terms_in_query:
            docs = self.postings[s]
            for d in docs:
                scores[d[0]] += d[1]*query.count(s)

        for i in range(0, len(scores)):
            scores[i] = scores[i]/np.random.randint(100, 500, 1)

        return scores
    
    def tf_idf(self, freq, term):
        N = 100
        if term in self.postings:
            return freq*math.log(N/freq, 2)
        else:
            return 0
    
    def score_tfidf(self, query):
        query = tokenize(query)
        scores = np.zeros(20)

        terms_in_query = list(set(query.split(' ')))
        
        for s in terms_in_query:
            docs = self.postings[s]
            for d in docs:
                scores[d[0]] += self.tf_idf(d[1], s)*self.tf_idf(query.count(s), s)

        for i in range(0, len(scores)):
            scores[i] = scores[i]/np.random.randint(100, 500, 1)

        return scores

r = Ranker()
print(r.score("política guerras politica"))