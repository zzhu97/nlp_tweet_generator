#This file contains the likelihood tables of a word following another word (bigram model)
#for each tweetbot.

import pickle
import global_vars

global list_of_likelihood_tables #list of dictionaries
num_of_bots = global_vars.num_of_bots #number of bots --> number of dictionaries to import. If #bots>#dictionaries, use big_dictionary

list_of_likelihood_tables = list()

#TODO: Create a bot's likelihood (Markov model) dictionary, dump it in a .pkl file, then retrieve it and insert it into a list.
    #Update big_dictionary from global_vars with new POSes and such

###
#TODO: Create a bot's likelihood dictionary here and return it
#Possible format: dict: word --> dict(nextword, possibility)
def create_bot_likelihood(fileIn):
    pass
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
    pass
###

#Driver
if __name__ == "__main__":
    main()