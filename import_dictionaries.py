#This is run every time build_dictionaries is run.
#Retrieves likelihood, transitions, and wordcount from dictionaries.pkl using Pickle library

import pickle

with open("dictionaries.pkl", "rb") as f:
    try:
        likelihood_dict = pickle.load(f) 
        transitions_dict = pickle.load(f)
        wordcount_dict = pickle.load(f)
    except:
        print("Could not import dictionaries.pkl. Maybe empty? Empty dictionaries created instead")
        likelihood_dict = dict()
        transitions_dict = dict()
        wordcount_dict = dict()