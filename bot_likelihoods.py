#This file contains the likelihood tables of a word following another word (bigram model)
#for each tweetbot.

import pickle
import global_vars
import sys
from collections import defaultdict

global list_of_likelihood_tables #list of dictionaries
num_of_bots = global_vars.num_of_bots #number of bots --> number of dictionaries to import. If #bots>#dictionaries, use big_dictionary

list_of_likelihood_tables = list()

# nested defaultdict of likelihoodTable[POS][word] = number of occurences
likelihoodTable = defaultdict(lambda: defaultdict(lambda: 0))

# nested defaultdict of priorTable[prior word's POS][current word POS] = number of occurences
priorTable = defaultdict(lambda: defaultdict(lambda: 0))

# Constants for beginning and ending states
BEGIN_SENT = "BEGIN_SENT"
END_SENT = "END_SENT"


#TODO: Create a bot's likelihood (Markov model) dictionary, dump it in a .pkl file, then retrieve it and insert it into a list.
    #Update big_dictionary from global_vars with new POSes and such

###
#TODO: Create a bot's likelihood dictionary here and return it
# Input File: fileIn = tagged version of celebrity's tweets (format of WORD_POS)
# likelihoodTable[word][POS] = number of occurences as that POS

def create_bot_dictionaries(fileIn):
    trainingFile = open(fileIn, 'r') # training corpus

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
                print("Skipping: ", word[rightIndex-1:rightIndex])
                posString = word[rightIndex+1:]
                wordString = word[:rightIndex-1]
                print("POS: ", posString, "Word: ", wordString)
                likelihoodTable[posString][wordString] += 1

                priorTable[priorPOS][posString] += 1

            else:
                posString = word[rightIndex+1:]
                wordString = word[:rightIndex]
                print("POS: ", posString, "Word: ", wordString)
                likelihoodTable[posString][wordString] += 1

                priorTable[priorPOS][posString] += 1

###

###
# Pops first dictionary from list_of_likelihood_tables
def retrieve_likelihood_table():
    return list_of_likelihood_tables.pop(0)
###

###
#Main function
def main():
    #Use sys args to determine number of dictionaries to create
    #Import from x number of files for x number of bots
    """
    import likelihood tables and put into list
    add new likelihood and put into list
    export into .pkl file to update

    """
    create_bot_dictionaries(sys.argv[1])
###

#Driver
if __name__ == "__main__":
    main()