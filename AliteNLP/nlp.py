import pandas as pd
import string
import re
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('brown')
# nltk.download('punkt')

wn = nltk.WordNetLemmatizer()
ps = nltk.PorterStemmer()

stopword = stopwords.words('english')

filepath = './trainingdatafiles/data.txt'
file = open(filepath, "r").read()
# print(file);

no_dup_nouns = list()
blob = TextBlob(file)

for phrase in blob.noun_phrases:
    if phrase not in no_dup_nouns:
        no_dup_nouns.append(phrase)
print('-------No Dup Noun Phrases ----------\n', len(no_dup_nouns), '\n', no_dup_nouns)

sentence = list()
for phrase in blob.sentences:
    if phrase not in sentence:
        sentence.append(phrase)
print('-------No Dup Sentences ----------\n', len(sentence), '\n', sentence)


no_punct = "".join([char for char in file if char not in string.punctuation]).lower()
tokens = re.split('\W+', no_punct)
no_stop_lemmatized = [wn.lemmatize(word) for word in tokens if word not in stopword]
print('Length of no_punct = {}'.format(len(no_punct)))
print('Length of tokens = {}'.format(len(tokens)))
print('Length of no_stop_lemmatized = {}'.format(len(no_stop_lemmatized)))

# print(no_stop_lemmatized)

no_duplicate = list()
for word in no_stop_lemmatized:
    if word not in no_duplicate:
        no_duplicate.append(word)

print('Length of no_duplicate = {}'.format(len(no_duplicate)))

# print(no_duplicate) 
