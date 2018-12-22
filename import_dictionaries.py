#This is run every time build_dictionaries is run.
#Retrieves likelihood, transitions, and big dictionary using Pickle library

import pickle

with open("dictionaries.pkl", "rb") as f:
    try:
        main_likelihood_dict = pickle.load(f) 
        main_transitions_dict = pickle.load(f)
    except:
        print("Could not import dictionaries.pkl. Maybe empty? Empty dictionaries created instead")
        main_likelihood_dict = dict()
        main_transitions_dict = dict()

with open("bigdict.pkl", "rb") as f:
    try:
        big_dictionary_dict = pickle.load(f)
    except:
        print("Could not import big dictionary file. Empty dict created")
        big_dictionary_dict = dict()

with open("bot_likelihoods.pkl", "rb") as f:
    try:
        list_of_likelihood_tables = pickle.load(f)
    except:
        print("bot_likelihoods.pkl is empty. Empty list created.")
        list_of_likelihood_tables = list()

with open("features.pkl", "rb") as f:
    try:
        list_of_features = pickle.load(f)
    except:
        print("features.pkl is empty. Empty list created.")
        list_of_features = list()