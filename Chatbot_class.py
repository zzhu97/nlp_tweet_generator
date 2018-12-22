#This file contains the Chatbot object class

import nltk
import random
import string
import global_vars
import bot_likelihoods
import bot_features
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
        self.features = self.initiate_personal_features()
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
        print(stack) #TEST

        """temp_stack = []
        for terminal in stack:
            pos = random.choice(list(self.lexicon[terminal].keys()))
            word = random.choice(self.lexicon[terminal][pos])
            temp_stack.append(word)

        return temp_stack"""
        return_stack = []

        prev_pos = ""
        prev_word = ""
        next_terminal = ""
        next_pos = ""
        next_word = ""

        for terminal in stack:
            choices = []
            maximum = 0

            if (prev_pos == ("NN" or "NNP" or "WP" or "PRP" or "POS" or "PRP$") and terminal == "VERB"):
                pos = random.choice(["VBD", "VBZ"])
            elif (prev_pos == ("NNS" or "NNPS") and terminal == "VERB"):
                pos = random.choice(["VBD", "VBG", "VBN", "VBP"])
            else:
                pos = random.choice(list(self.lexicon[terminal].keys()))

            for word in self.lexicon[terminal][pos]:
                try:
                    feature_list = self.features[word]
                    score = 0
                    for feature in feature_list:
                        if feature == "previous_Word":
                            if prev_word in feature:
                                score += 1
                        elif feature == "previous_POS":
                            if prev_pos in feature:
                                score += 1
                        #TODO: Add more features here

                        if score > 0:
                            choices.append(word)
                except:
                    continue

            if not choices:
                winner = random.choice(self.lexicon[terminal][pos])
            else:
                winner = random.choice(choices)

            prev_word = winner
            prev_pos = pos
            return_stack.append(winner)

        return return_stack
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
    #Retrieve's bot's personal features dictionary
    def initiate_personal_features(self):
        return bot_features.retrieve_feature_table()
    ###

    ###
    #Initiate personal lexicon
    def initiate_lexicon(self):
        lex = general_lexicon
        lex["NOUN"]["NN"] = self.likelihood_table["NN"]
        lex["NOUN"]["NNP"] = self.likelihood_table["NNP"]
        lex["NOUN"]["NNPS"] = self.likelihood_table["NNPS"]
        lex["NOUN"]["NNS"] = self.likelihood_table["NNS"]
        lex["NOUN"]["WP"] = self.likelihood_table["WP"]
        lex["NOUN"]["PRP"] = self.likelihood_table["PRP"]
        lex["DETERMINER"]["PDT"] = self.likelihood_table["PDT"]
        lex["DETERMINER"]["WDT"] = self.likelihood_table["WDT"]
        lex["DETERMINER"]["DT"] = self.likelihood_table["DT"]
        lex["PRP$"]["PRP$"] = self.likelihood_table["PRP$"]
        lex["POS"]["POS"] = self.likelihood_table["POS"]
        lex["ADJECTIVE"]["JJ"] = self.likelihood_table["JJ"]
        lex["ADJECTIVE"]["JJR"] = self.likelihood_table["JJR"]
        lex["ADJECTIVE"]["JJS"] = self.likelihood_table["JJS"]
        lex["CD"]["CD"] = self.likelihood_table["CD"]
        lex["VERB"]["VB"] = self.likelihood_table["VB"]
        lex["VERB"]["VBD"] = self.likelihood_table["VBD"]
        lex["VERB"]["VBG"] = self.likelihood_table["VBG"]
        lex["VERB"]["VBN"] = self.likelihood_table["VBN"]
        lex["VERB"]["VBP"] = self.likelihood_table["VBP"]
        lex["VERB"]["VBZ"] = self.likelihood_table["VBZ"]
        lex["ADVERB"]["RB"] = self.likelihood_table["RB"]
        lex["ADVERB"]["RBR"] = self.likelihood_table["RBR"]
        lex["ADVERB"]["RBS"] = self.likelihood_table["RBS"]
        lex["MODAL"]["MD"] = self.likelihood_table["MD"]
        lex["IN"]["IN"] = self.likelihood_table["IN"]

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
        pass
    ###
#END CHATBOT CLASS
###