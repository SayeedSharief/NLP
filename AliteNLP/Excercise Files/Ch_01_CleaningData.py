#!/usr/bin/env python
# coding: utf-8

# # NLP Basics: Implementing a pipeline to clean text

# ### Pre-processing text data
# 
# Cleaning up the text data is necessary to highlight attributes that you're going to want your machine learning system to pick up on. Cleaning (or pre-processing) the data typically consists of a number of steps:
# 1. **Remove punctuation**
# 2. **Tokenization**
# 3. **Remove stopwords**
# 4. Lemmatize/Stem
# 
# The first three steps are covered in this chapter as they're implemented in pretty much any text cleaning pipeline. Lemmatizing and stemming are covered in the next chapter as they're helpful but not critical.

# In[1]:


import pandas as pd
pd.set_option('display.max_colwidth', 100)

data = pd.read_csv("SMSSpamCollection.tsv", sep='\t', header=None)
data.columns = ['label', 'body_text']

data.head()


# In[2]:


# What does the cleaned version look like?
data_cleaned = pd.read_csv("SMSSpamCollection_cleaned.tsv", sep='\t')
data_cleaned.head()


# ### Remove punctuation

# In[3]:


import string
string.punctuation


# In[4]:


"I like NLP." == "I like NLP"


# In[5]:


def remove_punct(text):
    text_nopunct = "".join([char for char in text if char not in string.punctuation])
    return text_nopunct

data['body_text_clean'] = data['body_text'].apply(lambda x: remove_punct(x))

data.head()


# ### Tokenization

# In[6]:


import re

def tokenize(text):
    tokens = re.split('\W+', text)
    return tokens

data['body_text_tokenized'] = data['body_text_clean'].apply(lambda x: tokenize(x.lower()))

data.head()


# In[7]:


'NLP' == 'nlp'


# ### Remove stopwords

# In[19]:


import nltk

from nltk.corpus import stopwords

stopword = stopwords.words('english')

print(stopword)


# In[20]:


def remove_stopwords(tokenized_list):
    no_stop = [word for word in tokenized_list if word not in stopword]
    return no_stop

data['body_text_nostop'] = data['body_text_tokenized'].apply(lambda x : remove_stopwords(x))

data.head()


# In[ ]:




