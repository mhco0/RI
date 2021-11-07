#!/usr/bin/env python
# coding: utf-8

# In[25]:


#imports
import pickle
from bs4 import BeautifulSoup
import json
import re
import unidecode


# In[23]:


#Remove stopwords
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
from nltk.corpus import stopwords


# In[3]:


# import bag of words
bow = pickle.load(open("bow.pkl", "rb"))


# In[6]:


# import random forest classifier
model = pickle.load(open("model.pkl", "rb"))


# In[11]:


#open file to predict
f = open('17')
data = json.load(f)


# In[15]:


#read html
html = data['content']


# In[19]:


#parse html
soup = BeautifulSoup(html)
text = []
for script in soup(["script", "style"]):
        script.extract()    # rip it out
text.append(soup.get_text())


# In[21]:


#change characters
text = [unidecode.unidecode(s) for s in text]


# In[22]:


#Substitute point and go to lower case
text = [re.sub('[^A-Za-z]', ' ', s) for s in text]
text = [s.lower() for s in text]


# In[26]:


#tokenize
data = []
for s in text:
    tokenized_text = word_tokenize(s)
    for word in tokenized_text:
        if word in stopwords.words('portuguese'):
            tokenized_text.remove(word)
        
    s_text = " ".join(tokenized_text)
    data.append(s_text)


# In[30]:


#apply bag of words
X = bow.transform(data).toarray()


# In[31]:


#predict
model.predict(X)


# In[ ]:




