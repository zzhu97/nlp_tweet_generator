#This file contains the Chatbot object class

import nltk
import random
import global_vars
import bot_likelihoods
from stop_list import closed_class_stop_words # List of stop words for cosine similarity calculation

big_dictionary = global_vars.big_dictionary
syntax_rules = global_vars.syntax_rules
expansion_table = global_vars.expansion_table
general_lexicon = global_vars.general_lexicon
nonterminals = global_vars.nonterminals
terminals = global_vars.terminals
collection_words = global_vars.collection_words #Collection of words used for synonym matching

###
#CHATBOT CLASS
class Chatbot:
    ###
    #Initiate the chatbot object
    def __init__(self, name):
        self.name = name
        self.tweets_history = list() #Will be a dictionary of dictionaries of past tweets (organized by topic)

        #TODO: bot dictionary here
        """
        self.likelihood_table = bot_likelihoods.retrieve_likelihood_table()
        
        """
    ###

    ###
    #Generate a response based on subject
    def generate_response(self, subject):
        stack = self.expand_stack("S")
        stack = self.choose_words(stack)
        print(stack)
    ###

    ###
    #Expands sentence stack
    def expand_stack(self, sym):
        temp_stack = []
        stack = [sym]
        expand_flag = True

        while (expand_flag == True): #NP, VP
            temp_stack = []
            expand_flag = False
            for element in stack:
                if element in nonterminals:
                    expand_flag = True
                    element = random.choice(expansion_table[element])
                else:
                    element = [element]
                temp_stack = temp_stack + element
            stack = temp_stack
        return stack
    ###

    ###
    #Replaces terminals with words
    def choose_words(self, stack):
        temp_stack = []
        for terminal in stack:
            word = random.choice(general_lexicon[terminal])
            temp_stack.append(word)

        print(stack) #TEST

        return temp_stack
    ###

    ###
    #TODO: Cosine similarity with past tweets
    def compare_with_past_tweets(self, generated_tweet):
        #Lemmatize generated tweet and compare cosine similarity with past tweets
        pass
    ###
#END CHATBOT CLASS
###