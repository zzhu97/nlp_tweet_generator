#File used to build likelihood and probability tables. Takes properly formatted POS textfile and builds tables off that. Writes values to a textfile.
#Directly calling this program Input format is: python3 corpus.pos (or corpus.txt, etc...)
#   Can add "start" after args to build (reset) dictionaries from scratch. 
#   ONLY DO THIS when compiling everything for the first time, or if dictionaries are messed up.

#We can expand this to encompass multiple dicts for multiple celebrity bots

import sys
import os

#Hash table of POS and word frequencies based on POS
likelihood = dict() 

#Hash table of POS and transitions to next POS
transitions = dict() 

###Dictionary format: word pos count
#Function to build likelihood table
def build_likelihood(filepath):
    with open(filepath, "r") as f:
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
            else:
                likelihood[word][pos] = 1
    #Calculate likelihood percentages
    for word in likelihood:
        count = 0
        for token in likelihood.get(word):
            count += likelihood.get(word).get(token)
        for token in likelihood.get(word):
            likelihood[word][token] = (likelihood[word][token] / count)
    #f.close()

###Build prior probabilities table###
def build_transitions(filepath):
    with open(filepath, "r") as f:
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
            #print(token)
            transitions[pos][token] = (transitions[pos][token] / count)
    f.close()

#Add an OOV word to likelihood table
def add_likelihood(word, pos):
    likelihood[word] = dict()
    likelihood[word][pos] = 1
    for word in likelihood:
        count = 0
        for token in likelihood.get(word):
            count += likelihood.get(word).get(token)
        for token in likelihood.get(word):
            likelihood[word][token] = (likelihood[word][token] / count)

#Writes dictionaries to file
def rewrite_dictionaries():
    with open("likelihoods.txt", "w") as f:
        f.write("LIKELIHOODS:\n")
        for word in likelihood:
            f.write("\t%s\n" % word)
            for pos in likelihood.get(word):
                f.write("\t\t%s\t%.4f\n" % (pos, likelihood[word][pos]))
    with open("transitions.txt", "w") as f:
        f.write("TRANSITIONS:\n")
        for pos in transitions:
            f.write("\t%s\n" % pos)
            for nextPOS in transitions.get(pos):
                f.write("\t\t%s\t%.4f\n" % (nextPOS, transitions[pos][nextPOS]))

#Updates dictionaries (using a corpus), and then writes to file
#ONLY counts new POSes and new words - does not update current ones since WSJ is pretty comprehensive
#   This is temporary until we find a need to modify this algorithm
def update_dictionaries(new_corpus):
    #Corpus should be formatted as word\tPOS
    original_dict = likelihood
    original_transitions = transitions

    with open(new_corpus, "r") as f:
        #Add likelihoods first
        for line in f:
            if line == '\n':
                continue
            content = line.rstrip('\n').split('\t')
            word = content[0]
            pos = content[1]
            if word not in original_dict:
                if word not in likelihood:
                    likelihood[word] = dict()
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

#Retrieves current dictionary from likelihoods.txt and transitions.txt
def retrieve_current_dicts(likelihood_file, transitions_file):

    #Retrieves and rebuilds likelihood dictionary
    if (os.stat(likelihood_file).st_size == 0):
        print("likelihoods.txt is empty.\n")
    else:
        with open(likelihood_file, "r") as f:
            word = ""
            pos = ""
            chance = 0

            for line in f:
                content = line

                if ((line =='\n') or (content[0] == ("LIKELIHOODS:\n"))):
                    #If line is newline or start of file
                    continue

                content = line.lstrip("\t").rstrip('\n').split("\t")
                if len(content) == 1:
                    #Line is an identifier (new word, or a possible POS for word)
                    #Format: word
                    word = content[0]
                    likelihood[word] = dict()
                else:
                    #Format: pos chance
                    pos = content[0]
                    chance = float(content[1])
                    likelihood[word][pos] = chance

    #Retrieves and rebuilds transition dictionary
    if (os.stat(transitions_file).st_size == 0):
        print("transitions.txt is empty\n")
    else:
        with open(transitions_file, "r") as f:
            pos = ""
            nextPOS = ""
            chance = 0

            for line in f:
                content = line

                if ((line == '\n') or (content[0] == ("TRANSITIONS:\n"))):
                    #If line is newline or start of file
                    continue

                content = line.lstrip('\t').rstrip('\n').split("\t")
                if len(content) == 1:
                    #Line is a identifier (new POS)
                    #Format: pos
                    pos = content[0]
                    transitions[pos] = dict()
                else:
                    #Format: nextPOS chance
                    nextPOS = content[0]
                    chance = float(content[1])
                    transitions[pos][nextPOS] = chance

def main():
    #If "start" is added as an arg after python3 build_dictionaries.py corpus.txt, build dicts from stratch
        #ONLY DO THIS when compiling everything for the first time, or if dictionaries are messed up.

    if (len(sys.argv) > 2):
        if (sys.argv[2].lower() == "start"):
            #Rewrite dictionaries from scratch using corpus
            build_likelihood(sys.argv[1])
            build_transitions(sys.argv[1])
            rewrite_dictionaries()
        elif (sys.argv[2].lower() == "test"):
            #test
            retrieve_current_dicts("likelihoods.txt", "transitions.txt")
            build_likelihood(sys.argv[1])
            build_transitions(sys.argv[1])
        else:
            pass
    else:
        #Update current dictionaries using corpus (will not delete old dictionaries)
        #   This only adds new words and new POSes
        retrieve_current_dicts("likelihoods.txt", "transitions.txt")
        update_dictionaries(sys.argv[1])
        rewrite_dictionaries()

if __name__ == "__main__":
    main()