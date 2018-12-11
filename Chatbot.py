#Notes: Prioritize hashtags! If bot previously has used hashtag, good. If not, say something different?
#Notes: Save previous tweets in a file for NLTK shit

import os
import nltk
import random
import import_dictionaries
import re

#Imports general dictionaries from import_dictionaries.py 
likelihood = import_dictionaries.likelihood_dict
transitions = import_dictionaries.transitions_dict
wordcount = import_dictionaries.wordcount_dict

class Chatbot:
    ###INITIATE CHATBOT
    def __init__(self, name):
        self.name = name
        self.bot_dictionary = dict()
        self.tweets_history = list() #Will be a dictionary of dictionaries of past tweets (organized by topic)
    ###END INITIATE CHATBOT

    #Tokenize tweet, identify POSes and features.
    def tokenize_tweet(self, tweet):
        tweet_tokenized = nltk.word_tokenize(tweet)
        tweet_normalized = nltk.word_tokenize(tweet.lower())

        #Identify POSes per token here. Get subject from hashtags/nouns


        return tweet_tokenized
    ###END TOKENIZE TWEET FUNCTION

    ###Generate a response based on topic
    #Tweet is a sentence
    def generate_response(self, tweet):
        #Currently, the algorithm is RANDOM. We just want output.
        sentence = ""
        char_limit = 0 #Max is 150

        prevPOS = "SENTENCE_BREAK"
        while char_limit < 5: #5 is temporary value
            currentPOS = ""
            word = ""
            #currentPOS_max = 0
            possiblePOS = []
            possibleWord = []

            #Random word generator
            for nextPOS in transition_dict[prevPOS]:
                if transition_dict[prevPOS][nextPOS] < 0.1:
                    continue
                elif nextPOS == "SENTENCE_BREAK": #Skip newlines for now
                    continue
                possiblePOS.append(nextPOS)
            if not possiblePOS: #If all POSes have <10% chance
                for nextPOS in transition_dict[prevPOS]:
                    if nextPOS == "SENTENCE_BREAK": #Skip newlines for now
                        continue
                    possiblePOS.append(nextPOS)

            currentPOS = random.choice(possiblePOS)

            for token in self.dictionary[currentPOS]:
                possibleWord.append(token)
            word = random.choice(possibleWord)

            sentence += word + " "
            prevPOS = currentPOS
            char_limit += 1
        print(sentence)

    #Answer to a question given a subject (extract it from tweet)
    def generate_answer(self, topic):
        pass

    #Generate a question
    def generate_question(self, topic):
        pass

    #Generate a random tweet that this celebrity chatbot might realistically chat about
    def generate_chat(self, tweet):
        sentence = ""

    #Generate a statement about a topic
    def generate_statement(self, tweet):
        pass
