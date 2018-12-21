import sys
import math
import pickle
import global_vars

#Import dictionaries from import_dictionaries.py using Pickle
main_likelihood = global_vars.main_likelihood
main_transitions = global_vars.main_transitions
big_dictionary = global_vars.big_dictionary

###
#Build general likelihood dictionary
def build_likelihood(fileIn):
    with open(fileIn, "r") as f:
        for line in f:
            if line == '\n': #skip sentence breaks
                continue
            content = line.rstrip('\n').split('\t')
            word = content[0]
            pos = content[1]
            if word not in main_likelihood:
                main_likelihood[word] = dict()
            if pos in main_likelihood[word]:
                main_likelihood[word][pos] += 1
                #wordcount[word] += 1
            else:
                main_likelihood[word][pos] = 1
                #wordcount[word] = 1
    #Calculate likelihood percentages
    for word in main_likelihood:
        count = 0
        for token in main_likelihood.get(word):
            count += main_likelihood.get(word).get(token)
        for token in main_likelihood.get(word):
            main_likelihood[word][token] = (main_likelihood[word][token] / count)
###

###
#Build general probabilities dictionary
def build_transitions(fileIn):
    with open(fileIn, "r") as f:
        #temp will be the previous token
        temp = f.readline().rstrip('\n').split('\t')[1] #First token in file
        main_transitions["SENTENCE_BREAK"] = dict()
        main_transitions[temp] = dict()
        for line in f:
            content = line.split('\t')
            try:
                pos = content[1].rstrip('\n') #Current token
                #Current POS is a newline (Sentence break)
            except:
                if "SENTENCE_BREAK" not in main_transitions[temp]:
                    main_transitions[temp]["SENTENCE_BREAK"] = 1
                else:
                    main_transitions[temp]["SENTENCE_BREAK"] += 1
                temp = "SENTENCE_BREAK"
            else:
                if pos not in main_transitions:
                    main_transitions[pos] = dict()
                if pos in main_transitions[temp]:
                    main_transitions[temp][pos] += 1
                else:
                    main_transitions[temp][pos] = 1
                temp = pos
    #Calculate percentages (in decimal form)
    for pos in main_transitions:
        count = 0 #Total number of choices for prior POS to next POS
        for token in main_transitions.get(pos):
            count += main_transitions.get(pos).get(token)
        for token in main_transitions.get(pos):
            main_transitions[pos][token] = (main_transitions[pos][token] / count)
###

###
#Builds general big dictionary of words sorted by POS
def build_big_dictionary(pkl_file):
    for word in main_likelihood:
        for pos in main_likelihood[word]:
            if pos not in big_dictionary:
                big_dictionary[pos] = list()
            big_dictionary[pos].append(word)

###
#Saves dictionaries to file using pickle (.pkl extension)
def write_dictionaries(pkl_file, likelihood, transitions):
    #Switch up order if needed. Top to bottom priority
    with open(pkl_file, "wb") as fOut:
        pickle.dump(likelihood, fOut, -1)
        pickle.dump(transitions, fOut, -1) 
###

###Saves big dictionary to file using pickle
def write_big_dictionary(pkl_file, bigdict):
    with open(pkl_file, "wb") as fOut:
        pickle.dump(big_dictionary, fOut, -1)
###

###Updates big dictionary with new word
def update_big_dictionary(smaller_dict):
    #Smaller_dict should be a dictionary of same format: pos --> list of words
    for pos in smaller_dict:
        if pos not in big_dictionary:
            big_dictionary[pos] = list()
            big_dictionary[pos].append(smaller_dict[pos])
        else:
            list_of_words = smaller_dict[pos]
            original_list_of_words = big_dictionary[pos]
            for word in list_of_words:
                if word not in original_list_of_words:
                    big_dictionary[pos].append(word)
    with open("bigdict.pkl", "wb") as f:
        pass
    write_big_dictionary("bigdict.pkl", big_dictionary)
###


###
#Main function here. Builds likelihood, transitions, and big_dictionary from scratch from a corpus
def main():
    if (sys.argv[2] == "scratch"):
        print("Writing dictionaries - Starting from scratch.")
        with open("dictionaries.pkl", "wb") as f: #Erases dicts from pkl file
            pass
        with open("bigdict.pkl", "wb") as f:
            pass
        build_likelihood(sys.argv[1])
        build_transitions(sys.argv[1])
        build_big_dictionary("bigdict.pkl")
        write_dictionaries("dictionaries.pkl", main_likelihood, main_transitions)
        write_big_dictionary("bigdict.pkl", big_dictionary)
    elif (sys.argv[2] == "update"):
        pass
    else:
        print("Incorrect format for build_dictionaries.py.\nFormat is python3 build_dictionaries.py corpus scratch/update")
###

if __name__ == "__main__":
    main()