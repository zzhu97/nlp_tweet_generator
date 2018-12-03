""" Josh, Sai, Zhong
    NLP - Adam Myers
    Automated Tweet Generator
"""

#How should we do this boiz
#For words, we should use feature structures, likelihood, and probability.

import sys
import nltk
import random
import string
import numpy as np
#import re #if we need regex for whatever reason

#Below imports for chatbot algorithm generation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity











#TWEET GENERATION ALGORITHM
"""RULES: 

#SELF LEARNING: Save celebrity NN/NNP preferences and prefer those over other common nouns.

"""

sentence_tokenized = ["This", "is", "a", "sentence", "."]
lemmer = nltk.stem.WordNetLemmatizer();

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

f = open('test.txt', 'r', errors = 'ignore')
raw = f.read()
raw = raw.lower().replace('\n', ' ')

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw) 

print(sent_tokens[:2], '\n')