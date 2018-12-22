#This file contains the likelihood tables of a word following another word (bigram model)
#for each tweetbot.

import pickle
import global_vars
import sys
import build_dictionaries
import import_dictionaries

global list_of_likelihood_tables #list of dictionaries

list_of_likelihood_tables = import_dictionaries.list_of_likelihood_tables

# Constants for beginning and ending states
BEGIN_SENT = "BEGIN_SENT"
END_SENT = "END_SENT"

# Input File: fileIn = tagged version of celebrity's tweets (format of WORD_POS)
# likelihoodTable[word][POS] = number of occurences as that POS

def create_bot_dictionaries(fileIn):
    trainingFile = open(fileIn, 'r') # training corpus
    likelihoodTable = dict()
    priorTable = dict()

    priorPOS = BEGIN_SENT

    # Split words in a line into tokens in tempLine
    for line in trainingFile:
        if line != "\n":
            tempLine = line.strip('\n')
            tempLine = tempLine.split(' ')
        else:
            tempLine = line

        for tempWord in tempLine:
            # Remove quotation marks
            word = tempWord.replace('"', '')
            rightIndex = word.rfind('_')

            # Parse out periods from tokens
            if(word[rightIndex-1:rightIndex] == '.'):
                #print("Skipping: ", word[rightIndex-1:rightIndex])
                posString = word[rightIndex+1:]
                wordString = word[:rightIndex-1]
                #print("POS: ", posString, "Word: ", wordString)
                if posString not in likelihoodTable:
                    likelihoodTable[posString] = dict()
                if wordString not in likelihoodTable[posString]:
                    likelihoodTable[posString][wordString] = 1
                else:
                    likelihoodTable[posString][wordString] += 1

                #priorTable[priorPOS][posString] += 1
                if priorPOS not in priorTable:
                    priorTable[priorPOS] = dict()
                if posString not in priorTable[priorPOS]:
                    priorTable[priorPOS][posString] = 1
                else:
                    priorTable[priorPOS][posString] += 1

            else:
                posString = word[rightIndex+1:]
                wordString = word[:rightIndex]
                #print("POS: ", posString, "Word: ", wordString)
                if posString not in likelihoodTable:
                    likelihoodTable[posString] = dict()
                if wordString not in likelihoodTable[posString]:
                    likelihoodTable[posString][wordString] = 1
                else:
                    likelihoodTable[posString][wordString] += 1

                #priorTable[priorPOS][posString] += 1
                if priorPOS not in priorTable:
                    priorTable[priorPOS] = dict()
                if posString not in priorTable[priorPOS]:
                    priorTable[priorPOS][posString] = 1
                else:
                    priorTable[priorPOS][posString] += 1

    for pos in global_vars.big_dictionary:
        if pos not in likelihoodTable:
            print(pos)
            likelihoodTable[pos] = global_vars.big_dictionary[pos]
    for pos in global_vars.big_dictionary:
        if pos not in priorTable:
            pass
            #TODO: if pos not in this corpora

    build_dictionaries.update_big_dictionary(likelihoodTable)
    list_of_likelihood_tables.append(likelihoodTable)
    #TODO: Implement prior probability
###

###
# Pops first dictionary from list_of_likelihood_tables
def retrieve_likelihood_table():
    return list_of_likelihood_tables.pop(0)
###

###
#Loads likelihood tables into pkl file for storage
def dump_likelihood_tables():
    with open("bot_likelihoods.pkl", "wb") as fOut:
        pass
    with open("bot_likelihoods.pkl", "wb") as fOut:
    #    for table in list_of_likelihood_tables:
    #        pickle.dump(table, fOut, -1)
        pickle.dump(list_of_likelihood_tables, fOut, -1)
###

###
#Main function
def main(arg1):
    with open("bot_likelihoods.pkl", "wb") as f:
        pass
    create_bot_dictionaries(arg1)
    dump_likelihood_tables()
###

#Driver
if __name__ == "__main__":
    main(sys.argv[1])