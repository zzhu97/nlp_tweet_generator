#This is run every time build_dictionaries is run.
#Retrieves likelihood, transitions, and wordcount from dictionaries.pkl using Pickle library

import pickle

with open("dictionaries.pkl", "rb") as f:
    try:
        main_likelihood_dict = pickle.load(f) 
        main_transitions_dict = pickle.load(f)
        #big_dictionary_dict = pickle.load(f)
    except:
        print("Could not import dictionaries.pkl. Maybe empty? Empty dictionaries created instead")
        main_likelihood_dict = dict()
        main_transitions_dict = dict()
        #big_dictionary_dict = dict()

with open("big_dictionary.pkl", "rb") as f:
    try:
        big_dictionary_dict = pickle.load(f)
    except:
        print("Could not import big dictionary file. Empty dict created")
        big_dictionary_dict = dict()

###Test code block below