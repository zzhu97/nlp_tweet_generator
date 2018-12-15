# Josh Seol, Sai Singireddy, Zhong Zhu
# NLP - Adam Myers
# Automated Tweet Generator

import sys
import nltk
import random
import string
import math
from stop_list import closed_class_stop_words # List of stop words for cosine similarity calculation
import global_vars
import Chatbot_class
#import re #if we need regex for whatever reason


###Main function. Sys.argv[1] is number of tweetbots we want.
def main():
    global_vars.num_of_bots = sys.argv[1]
    chatbot1 = Chatbot_class.Chatbot("test_bot1") #TEST
    chatbot1.generate_response("test") #TEST

    for pos in Chatbot_class.big_dictionary:
        print(pos)

#Driver function for tweetgen.py
if __name__ == "__main__":
    main()