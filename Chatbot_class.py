#This file contains the Chatbot object class

import nltk
import random
import import_dictionaries

#Imports general dictionaries from import_dictionaries.py 
main_likelihood = import_dictionaries.main_likelihood_dict
main_transitions = import_dictionaries.main_transitions_dict
big_dictionary = import_dictionaries.big_dictionary_dict
collection_words = nltk.corpus.wordnet #Collection of words used for synonym matching

class Chatbot:
    #lemmatizer = nltk.stem.WordNetLemmatizer() #Lemmatizer that changes words to stem of word. Accepts string

    ###INITIATE CHATBOT
    def __init__(self, name):
        self.name = name
        self.tweets_history = list() #Will be a dictionary of dictionaries of past tweets (organized by topic)

        #TODO: bot dictionary here
    ###END INITIATE CHATBOT


    ###Generate a response based on topic
    #Tweet is a sentence
    def generate_response(self, tweet):
        #Currently, the algorithm is RANDOM. We just want output.
        #Want to tag tokens in tweet
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
            for nextPOS in main_transitions[prevPOS]:
                if main_transitions[prevPOS][nextPOS] < 0.1:
                    continue
                elif nextPOS == "SENTENCE_BREAK": #Skip newlines for now
                    continue
                possiblePOS.append(nextPOS)
            if not possiblePOS: #If all POSes have <10% chance
                for nextPOS in main_transitions[prevPOS]:
                    if nextPOS == "SENTENCE_BREAK": #Skip newlines for now
                        continue
                    possiblePOS.append(nextPOS)

            currentPOS = random.choice(possiblePOS)

            for token in main_likelihood:
                #possibleWord.append(token)
                if currentPOS in main_likelihood[token]:
                    possibleWord.append(token)
            word = random.choice(possibleWord)

            sentence += word + " "
            prevPOS = currentPOS
            char_limit += 1
        print(sentence)

    def expand_stack(self):
        pass

    def choose_word(self):
        pass

    def compare_with_past_tweets(self, generated_tweet):
        #Lemmatize generated tweet and compare cosine similarity with past tweets
        pass