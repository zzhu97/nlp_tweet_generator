#This module holds global variables.

import import_dictionaries
import nltk

global num_of_bots #number of tweetbots
global big_dictionary
global main_likelihood
global main_transitions
global wordnet_words

num_of_bots = 0
main_likelihood = import_dictionaries.main_likelihood_dict
main_transitions = import_dictionaries.main_transitions_dict
big_dictionary = import_dictionaries.big_dictionary_dict
collection_words = nltk.corpus.wordnet #Collection of words used for synonym matching

###
#Rules for sentence generation and nonterminal breakdown
#Nonterminal is [0] index, and possible breakdowns are in [1] index.
global syntax_rules, syntax_rules2
syntax_rules2 = [ ["S", ["NP", "VP"]], \
                ["NP", ["DetP", "AdjP", "NOUN"], ["DetP", "NOUN"], ["PossP", "AdjP", "NOUN"], ["PossP", "NOUN"], ["AdjP", "NOUN"], ["NOUN"]], \
                ["DetP", ["DETERMINER"]], \
                ["PossP", ["PRP$"], ["NOUN", "POS"]], \
                ["AdjP", ["ADJECTIVE", "AdjP"], ["ADJECTIVE"], ["CD"], ["CD", "AdjP"], ["CD"], ["ADJECTIVE"]], \
                #Predicate
                ["VP", ["VERB"], ["VERB", "NP"], ["ADVERB", "VERB"], ["MODAL", "VerbP"], ["VERB", "ADVERB"], ["VERB", "PrepP"]], \
                ["PrepP", ["IN", "NP"]], \
                ["VerbP", ["VERB"], ["VERB", "NP"], ["ADVERB", "VERB"], ["VERB", "ADVERB"], ["VERB", "PrepP"]], \
                ]
###

###
#List of terminals and nonterminals
global nonterminals
global terminals
nonterminals = ["S", "NP", "VP", "DetP", "AdjP", "PossP", "VerbP", "PrepP"]
terminals = ["NOUN", "DETERMINER", "PRP$", "POS", "ADJECTIVE", "CD", "VERB", "ADVERB", "MODAL", "IN"]
###

