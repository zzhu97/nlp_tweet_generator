import sys
import os
import math
import pickle
import import_dictionaries

#Import dictionaries from import_dictionaries.py using Pickle
likelihood = import_dictionaries.likelihood_dict
transitions = import_dictionaries.transitions_dict
wordcount = import_dictionaries.wordcount_dict

###BUILDS LIKELIHOOD DICTIONARY
def build_likelihood(fileIn):
    with open(fileIn, "r") as f:
        for line in f:
            if line == '\n': #skip sentence breaks
                continue
            content = line.rstrip('\n').split('\t')
            word = content[0]
            pos = content[1]
            if word not in likelihood:
                likelihood[word] = dict()
            if pos in likelihood[word]:
                likelihood[word][pos] += 1
                wordcount[word] += 1
            else:
                likelihood[word][pos] = 1
                wordcount[word] = 1
    #Calculate likelihood percentages
    for word in likelihood:
        count = 0
        for token in likelihood.get(word):
            count += likelihood.get(word).get(token)
        for token in likelihood.get(word):
            likelihood[word][token] = (likelihood[word][token] / count)

###Build probabilities dictionary
def build_transitions(fileIn):
    with open(fileIn, "r") as f:
        #temp will be the previous token
        temp = f.readline().rstrip('\n').split('\t')[1] #First token in file
        transitions["SENTENCE_BREAK"] = dict()
        transitions[temp] = dict()
        for line in f:
            content = line.split('\t')
            try:
                pos = content[1].rstrip('\n') #Current token
                #Current POS is a newline (Sentence break)
            except:
                if "SENTENCE_BREAK" not in transitions[temp]:
                    transitions[temp]["SENTENCE_BREAK"] = 1
                else:
                    transitions[temp]["SENTENCE_BREAK"] += 1
                temp = "SENTENCE_BREAK"
            else:
                if pos not in transitions:
                    transitions[pos] = dict()
                if pos in transitions[temp]:
                    transitions[temp][pos] += 1
                else:
                    transitions[temp][pos] = 1
                temp = pos
    #Calculate percentages (in decimal form)
    for pos in transitions:
        count = 0 #Total number of choices for prior POS to next POS
        for token in transitions.get(pos):
            count += transitions.get(pos).get(token)
        for token in transitions.get(pos):
            transitions[pos][token] = (transitions[pos][token] / count)

###Saves dictionaries to file using pickle (.pkl extension)
def write_dictionaries(pkl_file):
    #Order is: likelihoods, transitions, (wordcount)?
    with open(pkl_file, "wb") as fOut:
        pickle.dump(likelihood, fOut, -1)
        pickle.dump(transitions, fOut, -1)
        pickle.dump(wordcount, fOut, -1)

###Updates dictionaries with a corpus, then saves it to .pkl file
###Only counts new POSes and new words
def update_dictionaries(new_corpus):
    #Corpus should be formatted as word\tPOS
    original_dict = likelihood
    original_transitions = transitions

    with open(new_corpus, "r") as f:
        #Add likelihoods and wordcounts first
        for line in f:
            if line == '\n':
                continue
            content = line.rstrip('\n').split('\t')
            word = content[0]
            pos = content[1]
            if word not in original_dict:
                if word not in likelihood:
                    likelihood[word] = dict()
                    wordcount[word] = 1 #Updates wordcount
                else:
                    wordcount[word] += 1 #Updates wordcount
                if pos in likelihood[word]:
                    likelihood[word][pos] += 1
                else:
                    likelihood[word][pos] = 1
    #Calculate likelihood percentages
    for word in likelihood:
        if word not in original_dict:
            count = 0
            for token in likelihood.get(word):
                count += likelihood.get(word.get(token))
            for token in likelihood.get(word):
                likelihood[word][token] = (likelihood[word][token] / count)
    with open(new_corpus, "r") as f:
        #Add transitions
        #prev will be the previous token
        prev = f.readline().rstrip('\n').split('\t')[1] #First token in file
        if prev not in original_transitions:
            transitions[prev] = dict()

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
                    if pos not in transitions:
                        transitions[pos] = dict()
                        transitions[prev][pos] = 1
                    else:
                        transitions[prev][pos] += 1
    #Calculate new POS probabilities
    for pos in transitions:
        if pos not in original_transitions:
            count = 0
            for token in transitions.get(pos):
                count += transitions.get(pos.get(token))
            for token in transitions.get(pos):
                transitions[pos][token] = (transitions[pos][token] / count)

###MAIN FUNCTION
def main():
    #If "start" is added as an arg after python3 build_dictionaries.py corpus.txt, build dicts from stratch
        #ONLY DO THIS when compiling everything for the first time, or if dictionaries are messed up.

    if (len(sys.argv) > 2):
        if (sys.argv[2].lower() == "start"):
            #Rewrite dictionaries from scratch using corpus
            print("Writing dictionaries - Starting from scratch.")
            with open("dictionaries.pkl", "wb") as f: #Erases dicts from pkl file
                pass
            build_likelihood(sys.argv[1])
            build_transitions(sys.argv[1])
            write_dictionaries("dictionaries.pkl")
        else:
            pass
    else:
        #Update current dictionaries using corpus (will not delete old dictionaries)
        #This only adds new words and new POSes

        update_dictionaries(sys.argv[1])
        write_dictionaries("dictionaries.pkl")

if __name__ == "__main__":
    main()