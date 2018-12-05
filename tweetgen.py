# Josh Seol, Sai Singireddy, Zhong Zhu
# NLP - Adam Myers
# Automated Tweet Generator

import sys
import nltk
import random
import string
import math
import build_dictionaries # Import built dictionaries. 
from stop_list import closed_class_stop_words # List of stop words for cosine similarity calculation

#import numpy as np #garbage
#import re #if we need regex for whatever reason


###TWEET GENERATION ALGORITHM####
#RULES:
#   - 150 character max
#    
#
#SELF LEARNING: Save celebrity NN/NNP preferences and prefer those over other common nouns.
#
#
##CODE HERE
#################################

build_dictionaries.retrieve_current_dicts("likelihoods.txt", "transitions.txt") # Builds likelihood and transition dicts from text files
likelihood_dict = build_dictionaries.likelihood
transition_dict = build_dictionaries.transitions


class Chatbot:
    def __init__(self, name, likelihoods, transitions):
        self.name = name
        self.generation_dict = build_dictionaries.word_generation_dict(likelihoods, transitions) #Dict of format: pos>word>(word count)

    #Generate a response based on topic
    #Topic should be a word/phrase that has associated features
    def generate_response(self, topic):
        #Currently, the algorithm is RANDOM. We just want output.
        sentence = ""
        char_limit = 0 #Max is 150

        prevPOS = "SENTENCE_BREAK"
        while char_limit < 5:
            currentPOS = ""
            word = ""
            #currentPOS_max = 0
            possiblePOS = []
            possibleWord = []

            for pos in transition_dict[prevPOS]:
                possiblePOS.append(pos)
            currentPOS = random.choice(possiblePOS)

            for token in self.generation_dict[currentPOS]:
                possibleWord.append(token)
            word = random.choice(possibleWord)

            sentence += word + " "
            prevPOS = currentPOS
            char_limit += 1
        print(sentence)

def main():
    chatbot1 = Chatbot("test_bot1", likelihood_dict, transition_dict)
    chatbot1.generate_response("test")
    

if __name__ == "__main__":
    main()

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