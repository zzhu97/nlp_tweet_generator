#This is run every time build_dictionaries is run.
#Retrieves likelihood, transitions, and big dictionary using Pickle library

import pickle

"""with open("dictionaries.pkl", "rb") as f:
    try:
        main_likelihood_dict = pickle.load(f) 
        main_transitions_dict = pickle.load(f)
    except:
        print("Could not import dictionaries.pkl. Maybe empty? Empty dictionaries created instead")
        main_likelihood_dict = dict()
        main_transitions_dict = dict()
"""


"""with open("features.pkl", "rb") as f:
    try:
        list_of_features = pickle.load(f)
    except:
        print("features.pkl is empty. Empty list created.")
        list_of_features = list()
"""