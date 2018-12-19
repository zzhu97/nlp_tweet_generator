#This file contains the Chatbot object class

import nltk
import random
import global_vars

#Imports general dictionaries from import_dictionaries.py 
main_likelihood = global_vars.main_likelihood
main_transitions = global_vars.main_transitions
big_dictionary = global_vars.big_dictionary
syntax_rules = global_vars.syntax_rules
expansion_table = global_vars.expansion_table
general_lexicon = global_vars.general_lexicon
nonterminals = global_vars.nonterminals
terminals = global_vars.terminals
collection_words = global_vars.collection_words #Collection of words used for synonym matching

class Chatbot:
    #lemmatizer = nltk.stem.WordNetLemmatizer() #Lemmatizer that changes words to stem of word. Accepts string

    ###
    #Initiate the chatbot object
    def __init__(self, name):
        self.name = name
        self.tweets_history = list() #Will be a dictionary of dictionaries of past tweets (organized by topic)

        #TODO: bot dictionary here
    ###

    ###
    #Generate a response based on topic
    #Tweet is a sentence
    def generate_response(self, subject):
        stack = self.expand_stack("S")
        stack = self.choose_words(stack)
        print(stack)
    ###

    def expand_stack(self, sym):
        temp_stack = []
        stack = [sym]
        expand_flag = True

        while (expand_flag == True): #NP, VP
            temp_stack = []
            expand_flag = False
            for element in stack:
                if element in global_vars.nonterminals:
                    expand_flag = True
                    element = random.choice(global_vars.expansion_table[element])
                else:
                    element = [element]
                temp_stack = temp_stack + element
            stack = temp_stack
        return stack

    def choose_words(self, stack):
        #TEST
        temp_stack = []
        for terminal in stack:
            word = random.choice(global_vars.general_lexicon[terminal])
            temp_stack.append(word)

        print(stack) #TEST
        
        return temp_stack

    def compare_with_past_tweets(self, generated_tweet):
        #Lemmatize generated tweet and compare cosine similarity with past tweets
        pass