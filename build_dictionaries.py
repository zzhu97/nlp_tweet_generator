import sys
import os
import math
import pickle
import import_dictionaries

#Import dictionaries from import_dictionaries.py using Pickle
main_likelihood = import_dictionaries.main_likelihood_dict
main_transitions = import_dictionaries.main_transitions_dict
big_dictionary = import_dictionaries.big_dictionary_dict

###BUILDS LIKELIHOOD DICTIONARY
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

###Build probabilities dictionary
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

###Builds big dictionary of words sorted by POS
def build_big_dictionary(pkl_file):
    for word in main_likelihood:
        for pos in main_likelihood[word]:
            if pos not in big_dictionary:
                big_dictionary[pos] = list()
            big_dictionary[pos].append(word)

###Saves dictionaries to file using pickle (.pkl extension)
def write_dictionaries(pkl_file, likelihood, transitions):
    #Switch up order if needed. Top to bottom priority
    with open(pkl_file, "wb") as fOut:
        pickle.dump(likelihood, fOut, -1)
        pickle.dump(transitions, fOut, -1) 

###Saves big dictionary to file using pickle
def write_big_dictionary(pkl_file, bigdict):
    with open(pkl_file, "wb") as fOut:
        pickle.dump(big_dictionary, fOut, -1)

###Updates dictionaries with a corpus, then saves it to .pkl file
###Only counts new POSes and new words
def update_dictionaries(new_corpus):
    #Corpus should be formatted as word\tPOS
    original_dict = main_likelihood
    original_transitions = main_transitions

    with open(new_corpus, "r") as f:
        #Add likelihoods and wordcounts first
        for line in f:
            if line == '\n':
                continue
            content = line.rstrip('\n').split('\t')
            word = content[0]
            pos = content[1]
            if word not in original_dict:
                if word not in main_likelihood:
                    main_likelihood[word] = dict()
                if pos in likelihood[word]:
                    main_likelihood[word][pos] += 1
                else:
                    main_likelihood[word][pos] = 1
    #Calculate likelihood percentages
    for word in main_likelihood:
        if word not in original_dict:
            count = 0
            for token in main_likelihood.get(word):
                count += main_likelihood.get(word.get(token))
            for token in main_likelihood.get(word):
                main_likelihood[word][token] = (main_likelihood[word][token] / count)
    with open(new_corpus, "r") as f:
        #Add transitions
        #prev will be the previous token
        prev = f.readline().rstrip('\n').split('\t')[1] #First token in file
        if prev not in original_transitions:
            main_transitions[prev] = dict()

        for line in f:
            content = line.split('\t')
            try:
                pos = content[1].rstrip('\n') #Current POS
            except:
                #Current POS is sentence break
                prev = "SENTENCE_BREAK"
            else:
                if pos not in original_transitions:
                    print("Prev: ", prev)
                    print("Pos: ", pos)
                    if pos not in main_transitions:
                        main_transitions[pos] = dict()
                        main_transitions[prev][pos] = 1
                    else:
                        main_transitions[prev][pos] += 1
    #Calculate new POS probabilities
    for pos in main_transitions:
        if pos not in original_transitions:
            count = 0
            for token in main_transitions.get(pos):
                count += main_transitions.get(pos.get(token))
            for token in main_transitions.get(pos):
                main_transitions[pos][token] = (main_transitions[pos][token] / count)

###Main function here.
def main():
    #If "start" is added as an arg after python3 build_dictionaries.py corpus.txt, build dicts from stratch
    #ONLY DO THIS when compiling everything for the first time, or if dictionaries are messed up.

    if (len(sys.argv) > 2):
        if (sys.argv[2].lower() == "start"):
            #Rewrite dictionaries from scratch using corpus
            print("Writing dictionaries - Starting from scratch.")
            with open("dictionaries.pkl", "wb") as f: #Erases dicts from pkl file
                pass
            with open("big_dictionary.pkl", "wb") as f:
                pass
            build_likelihood(sys.argv[1])
            build_transitions(sys.argv[1])
            build_big_dictionary("big_dictionary.pkl")
            write_dictionaries("dictionaries.pkl", main_likelihood, main_transitions)
            write_big_dictionary("big_dictionary.pkl", big_dictionary)
        else:
            pass
    else:
        #Update current dictionaries using corpus (will not delete old dictionaries)
        #This only adds new words and new POSes

        update_dictionaries(sys.argv[1])
        build_big_dictionary("big_dictionary.pkl")
        write_dictionaries("dictionaries.pkl", main_likelihood, main_transitions)
        write_big_dictionary("big_dictionary.pkl", big_dictionary)

if __name__ == "__main__":
    main()