#nltk tools
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import PlaintextCorpusReader

#tf-idf
from sklearn.feature_extraction.text import TfidfVectorizer

#other resources
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml
import os

#%matplotlib inline


#goes to corpus directory
#os.chdir('../../')


#goes to corpus directory
#os.chdir('../../')


#creates corpus
corpus_root = '<PATH_TO_texts/>'
corpus = PlaintextCorpusReader(corpus_root, '.*')


#gets stopwords
stopwords = nltk.corpus.stopwords.words('portuguese')


#gets diversity lexial mean and var
mean, var = lexical_diversity_stopwords(corpus)


#extracts texts from corpus
corpus_texts = []

for f in corpus.fileids():
    corpus_texts.append(corpus.raw(fileids=f))


#gets meaningfull words
meaningfull_words = tf_idf(corpus_texts, stopwords, top_n_words=10)


#prints words and score
print("Words", "Score")
for i in range(len(meaningfull_words)):
    print(meaningfull_words[i][0], "%.3f" % meaningfull_words[i][1])

print('\n')

#prints lexical diversity mean and var (for texts comparison)
print("Mean", "%.3f" % mean)
print("Variance", "%.3f" % var)
