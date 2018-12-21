#This file contains the Chatbot object class

import nltk
import random
import string
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
        self.tweets_history = list()
        self.likelihood_table = self.initiate_personal_dictionary()
        self.lexicon = self.initiate_lexicon()
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
    #TODO: Expand this to consider features, relevancy, etc... idk
    def choose_words(self, stack):
        temp_stack = []
        for terminal in stack:
            #word = random.choice(general_lexicon[terminal])
            word = random.choice(self.lexicon[terminal])
            temp_stack.append(word)

        print(stack) #TEST

        return temp_stack
    ###

    ###
    #Retrieves bot's personal likelihood dictionary.
    def initiate_personal_dictionary(self):
        table = bot_likelihoods.retrieve_likelihood_table()
        temp = dict()
        for pos in table:
            temp[pos] = list()
            for word in table[pos]:
                temp[pos].append(word)
        return temp
    ###

    ###
    #Initiate personal lexicon
    def initiate_lexicon(self):
        lex = dict()
        lex["NOUN"] = self.likelihood_table["NN"] + self.likelihood_table["NNP"] + self.likelihood_table["NNPS"] + self.likelihood_table["NNS"] + self.likelihood_table["WP"] + self.likelihood_table["PRP"]
        lex["DETERMINER"] = self.likelihood_table["PDT"] + self.likelihood_table["DT"] + self.likelihood_table["WDT"]
        lex["PRP$"] = self.likelihood_table["PRP$"]
        lex["POS"] = self.likelihood_table["POS"]
        lex["ADJECTIVE"] = self.likelihood_table["JJ"] + self.likelihood_table["JJR"] + big_dictionary["JJS"]
        lex["CD"] = self.likelihood_table["CD"]
        lex["VERB"] = self.likelihood_table["VB"] + self.likelihood_table["VBD"] + self.likelihood_table["VBG"] + self.likelihood_table["VBN"] + self.likelihood_table["VBP"] + self.likelihood_table["VBZ"]
        lex["ADVERB"] = self.likelihood_table["RB"] + self.likelihood_table["RBR"] + self.likelihood_table["RBS"]
        lex["MODAL"] = self.likelihood_table["MD"]
        lex["IN"] = self.likelihood_table["IN"]
        return lex
    ###

    ###
    #TODO: Cosine similarity with past tweets
    def compare_with_past_tweets(self, generated_tweet):
        #Lemmatize generated tweet and compare cosine similarity with past tweets
        for tweet in self.tweets_history:
            self.clean_tweet(tweet)
            self.compare_tweets(generated_tweet, tweet)
    ###
    #Cleans tweets. Returns a list of tokens.
    def clean_tweet(self, tweet):
        tweet = nltk.word_tokenize(tweet)
        for token in list(tweet):
            if token.lower() in closed_class_stop_words:
                tweet.remove(token)
            if token in string.punctuation:
                tweet.remove(token)
        return tweet
    ###

    ###
    #Compares two tweets
    def compare_tweets(self, tweet1, tweet2):
        pass
    ###

    ###
    #Test function
    def tester(self):
        for pos in self.likelihood_table:
            print(self.likelihood_table[pos])
        pass
    ###
#END CHATBOT CLASS
###