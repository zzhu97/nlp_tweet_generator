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

<<<<<<< HEAD
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
=======

>>>>>>> e7e8d5817a8d1da1c350bd79187135eb24cae77b

def main():
    pass

if __name__ == "__main__":
    main()

