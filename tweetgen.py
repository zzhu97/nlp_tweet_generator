# Josh Seol, Sai Singireddy, Zhong Zhu
# NLP - Adam Myers
# Automated Tweet Generator

import sys
import nltk
import random
import string
import math
from stop_list import closed_class_stop_words # List of stop words for cosine similarity calculation
import Chatbot_class

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



def main():
    chatbot1 = Chatbot_class.Chatbot("test_bot1") #TEST
    chatbot1.generate_response("test") #TEST

if __name__ == "__main__":
    main()