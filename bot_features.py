#This file contains the feature lists per bot

import pickle
import global_vars
import sys
import import_dictionaries

global list_of_features

list_of_features = import_dictionaries.list_of_features

###
#Creates bot features
#Dict[Americans] = {Previous_POS : NNS, JJ}, {PLURAL : }
def create_bot_features(fileIn):
    features_table = dict()

    with open(fileIn, "r") as f:
        for line in f:
            if line == "\n":
                continue
            content = line.lstrip('"').rstrip("\t\n").split("\t")
            word = content[0].replace('"', "")
            features = content[1:]

            if word not in features_table:
                features_table[word] = dict()

            for token in features:
                if "=" in token:
                    token = token.split("=") #POS=UH
                    feature = token[0] #POS
                    definition = token[1].replace('"', "") #UH
                    if feature not in features_table[word]:
                        features_table[word][feature] = list()
                        if definition not in features_table[word][feature]:
                            features_table[word][feature].append(definition)
                    else:
                        if definition not in features_table[word][feature]:
                            features_table[word][feature].append(definition)
                else:
                    #Key is the feature (PLURAL, SLANG, etc...) Value is garbage.
                    if token not in features_table[word]:
                        features_table[word][token] = 1
    list_of_features.append(features_table)
###

###
#Pops first dictionary from list_of_features
def retrieve_feature_table():
    return list_of_features.pop(0)
###

###
#Saves feature tables into pkl file for storage
def dump_feature_tables():
    with open("features.pkl", "wb") as fOut:
        pass
    with open("features.pkl", "wb") as fOut:
        pickle.dump(list_of_features, fOut, -1)
###

###
#Main function
def main(arg1):
    #Note: Does not erase previous dictionaries.
    with open("features.pkl", "wb") as f:
        pass
    create_bot_features(arg1)
    dump_feature_tables()
###

if __name__ == "__main__":
    main(sys.argv[1])