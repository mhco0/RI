from utils import Utils
from collections import Counter
import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import unidecode


class MutualInformation:

    @staticmethod
    def tokenize(text):
        # change characters
        text = unidecode.unidecode(text)

        # Substitute point and go to lower case

        text = re.sub('[^A-Za-z]', ' ', text)
        text = text.lower()

        # tokenize
        tokenized_text = word_tokenize(text)
        for word in tokenized_text:
            if word in stopwords.words('portuguese'):
                tokenized_text.remove(word)

        return tokenized_text

    @staticmethod
    def countUnigramBigram():
        corpus = Utils.readJsonFile('./static/list_corpus.json')
        unigram = Counter(corpus)
        bigram = Counter([(corpus[idx]+' '+corpus[idx+1])
                          for idx in range(len(corpus) - 1)])
        Utils.writeJsonFile('./static/unigram.json', dict(unigram))
        Utils.writeJsonFile('./static/bigram.json', dict(bigram))

    @staticmethod
    def calcMutualInformation(s: str):
        corpus = Utils.readJsonFile('./static/list_corpus.json')
        unigrams = Utils.readJsonFile('./static/unigram.json')
        bigrams = Utils.readJsonFile('./static/bigram.json')

        n = len(corpus)
        words = MutualInformation.tokenize(s)
        mutualInformations = {}
        for word in words:
            if word != '':
                for bigram, fxy in bigrams.items():
                    if word in bigram.split(' '):
                        fx = unigrams[word]
                        wordTwo = bigram.replace(word, '').strip()
                        if wordTwo in unigrams:
                            fy = unigrams[wordTwo]
                            ixy = math.log2((fxy / n)/((fx / n)*(fy/n)))
                            mutualInformations[bigram] = ixy

        return Counter(mutualInformations).most_common(3)
