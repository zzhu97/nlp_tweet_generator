#This module holds global variables.

import import_dictionaries
import nltk

global big_dictionary
global syntax_rules
global terminals
global nonterminals
global expansion_table
global general_lexicon

#main_features = import_dictionaries.list_of_features

#TODO: saving dictionaries per bot



###
#Rules for sentence generation and nonterminal breakdown
#Nonterminal is [0] index, and possible breakdowns are in [1] index.
syntax_rules = [ ["S", ["NP", "VP"]], \
                ["NP", ["DetP", "AdjP", "NOUN"], ["DetP", "NOUN"], ["PossP", "AdjP", "NOUN"], ["PossP", "NOUN"], ["AdjP", "NOUN"], ["NOUN"]], \
                ["DetP", ["DETERMINER"]], \
                ["PossP", ["PRP$"], ["NOUN", "POS"], ["DETERMINER", "NOUN", "POS"]], \
                ["AdjP", ["ADJECTIVE"], ["CD"], ["ADJECTIVE"]], \
                #Predicate
                ["VP", ["VERB"], ["VERB", "NP"], ["ADVERB", "VERB"], ["MODAL", "VerbP"], ["VERB", "ADVERB"], ["VERB", "PrepP"]], \
                ["PrepP", ["IN", "NOUN"]], \
                ["VerbP", ["VERB"], ["VERB", "NP"], ["ADVERB", "VERB"], ["VERB", "ADVERB"], ["VERB", "PrepP"]], \
                ]
###

###
#List of terminals and nonterminals
nonterminals = ["S", "NP", "VP", "DetP", "AdjP", "PossP", "VerbP", "PrepP"]
terminals = ["NOUN", "DETERMINER", "PRP$", "POS", "ADJECTIVE", "CD", "VERB", "ADVERB", "MODAL", "IN"]
expansion_table = dict()

def fill_expansion_table():
    for rules in syntax_rules:
        expander = rules[0]
        expansion = rules[1:]
        expansion_table[expander] = expansion
###

###
#General lexicon list 
general_lexicon = dict()

def fill_lexicon_table():
    """general_lexicon["NOUN"] = big_dictionary["NN"] + big_dictionary["NNP"] + big_dictionary["NNPS"] + big_dictionary["NNS"] + big_dictionary["WP"] + big_dictionary["PRP"]
    general_lexicon["DETERMINER"] = big_dictionary["PDT"] + big_dictionary["DT"] + big_dictionary["WDT"]
    general_lexicon["PRP$"] = big_dictionary["PRP$"]
    general_lexicon["POS"] = big_dictionary["POS"]
    general_lexicon["ADJECTIVE"] = big_dictionary["JJ"] + big_dictionary["JJR"] + big_dictionary["JJS"]
    general_lexicon["CD"] = big_dictionary["CD"]
    general_lexicon["VERB"] = big_dictionary["VB"] + big_dictionary["VBD"] + big_dictionary["VBG"] + big_dictionary["VBN"] + big_dictionary["VBP"] + big_dictionary["VBZ"]
    general_lexicon["ADVERB"] = big_dictionary["RB"] + big_dictionary["RBR"] + big_dictionary["RBS"]
    general_lexicon["MODAL"] = big_dictionary["MD"]
    general_lexicon["IN"] = big_dictionary["IN"]"""
    general_lexicon["NOUN"] = dict()
    general_lexicon["DETERMINER"] = dict()
    general_lexicon["PRP$"] = dict()
    general_lexicon["POS"] = dict()
    general_lexicon["ADJECTIVE"] = dict()
    general_lexicon["CD"] = dict()
    general_lexicon["VERB"] = dict()
    general_lexicon["ADVERB"] = dict()
    general_lexicon["MODAL"] = dict()
    general_lexicon["IN"] = dict()

    return general_lexicon
###

###
#Driver code here
fill_expansion_table()
fill_lexicon_table()
###