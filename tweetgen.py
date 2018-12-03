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
import math
from stop_list import closed_class_stop_words #List of stop words for cosine similarity calculation
#import numpy as np
#import re #if we need regex for whatever reason











#TWEET GENERATION ALGORITHM
"""RULES: 

#SELF LEARNING: Save celebrity NN/NNP preferences and prefer those over other common nouns.

"""



"""
### TEST CODE BLOCK FROM medium.com ###
sentence_tokenized = ["This", "is", "a", "sentence", "."]
lemmer = nltk.stem.WordNetLemmatizer(); #WordNet is a semantically-oriented dictionary of English included in NLTK.
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

f = open('test.txt', 'r', errors = 'ignore')
raw = f.read()
raw = raw.lower().replace('\n', ' ')

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw) 

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

flag=True
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("ROBO: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("ROBO: "+greeting(user_response))
            else:
                print("ROBO: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("ROBO: Bye! take care..")


### TEST CODE BLOCK FROM medium.com ###
"""