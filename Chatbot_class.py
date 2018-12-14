#Notes: Prioritize hashtags! If bot previously has used hashtag, good. If not, say something different?
#Notes: Save previous tweets in a file for NLTK shit

import nltk
import random
import import_dictionaries

#Imports general dictionaries from import_dictionaries.py 
likelihood = import_dictionaries.likelihood_dict
transitions = import_dictionaries.transitions_dict
wordcount = import_dictionaries.wordcount_dict
collection_words = nltk.corpus.wordnet #Collection of words used for synonym matching

class Chatbot:
    lemmatizer = nltk.stem.WordNetLemmatizer() #Lemmatizer that changes words to stem of word. Accepts string

    ###INITIATE CHATBOT
    def __init__(self, name):
        self.name = name
        #self.bot_dictionary = dict()
        self.tweets_history = list() #Will be a dictionary of dictionaries of past tweets (organized by topic)

        self.bot_dictionary = likelihood #TEMP
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
            for nextPOS in transitions[prevPOS]:
                if transitions[prevPOS][nextPOS] < 0.1:
                    continue
                elif nextPOS == "SENTENCE_BREAK": #Skip newlines for now
                    continue
                possiblePOS.append(nextPOS)
            if not possiblePOS: #If all POSes have <10% chance
                for nextPOS in transitions[prevPOS]:
                    if nextPOS == "SENTENCE_BREAK": #Skip newlines for now
                        continue
                    possiblePOS.append(nextPOS)

            currentPOS = random.choice(possiblePOS)

            for token in self.bot_dictionary:
                #possibleWord.append(token)
                if currentPOS in self.bot_dictionary[token]:
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