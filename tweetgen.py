# Josh Seol, Sai Singireddy, Zhong Zhu
# NLP - Adam Myers
# Automated Tweet Generator

import sys
import global_vars
import Chatbot_class

#Format for cmd line is python3 tweetgen.py #chatbots, where #chatbots is number of tweetbots we want
def main():
    global_vars.num_of_bots = sys.argv[1]
    chatbot1 = Chatbot_class.Chatbot("test_bot1") #TEST
    chatbot1.generate_response("test") #TEST
    chatbot1.tester()

#Driver function for tweetgen.py
if __name__ == "__main__":
    main()