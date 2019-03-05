# Josh Seol, Sai Singireddy, Zhong Zhu
# NLP - Adam Myers
# Automated Tweet Generator

import sys
import global_vars
import Chatbot_class_2

#Format for cmd line is python3 tweetgen.py #chatbots, where #chatbots is number of tweetbots we want
def main():
    if len(sys.argv) < 2:
        print("Input format is: python3 tweetgen.py corpus")
    else:
        chatbot1 = Chatbot_class_2.Chatbot("test1", sys.argv[1])
        chatbot1.tester()

#Driver function for tweetgen.py
if __name__ == "__main__":
    main()