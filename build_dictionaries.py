#File used to build likelihood and probability tables. Takes properly formatted POS textfile and builds tables off that. Writes values to a textfile.
#Input format is: python3 corpus.pos (or corpus.txt, etc...)
#Can add "start" after args to build (reset) dictionaries from scratch

import sys

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
    f.close()

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
def write_dictionaries():
     with open("dictionaries.txt", "w") as f:
        f.write("LIKELIHOODS:\n")
        for word in likelihood:
            f.write("\t%s\n" % word)
            for pos in likelihood.get(word):
                f.write("\t\t%s,%.4f\n" % (pos, likelihood[word][pos]))
        f.write("\nTRANSITIONS:\n")
        for pos in transitions:
            f.write("\t%s\n" % pos)
            for nextPOS in transitions.get(pos):
                f.write("\t\t%s,%.4f\n" % (nextPOS, transitions[pos][nextPOS]))

def main():
    #If "start" is added as an arg after python3 build_dictionaries.py corpus.txt, build dicts from stratch

    print("%s %s %s\n" % (sys.argv[0], sys.argv[1], sys.argv[2]))
    build_likelihood(sys.argv[1])
    build_transitions(sys.argv[1])
    if (len(sys.argv) > 2):
        if (sys.argv[2].lower() == "start"):
            write_dictionaries()
        else:
            print("Garbage input for sys.argv[2]\n")
    else:
        pass

if __name__ == "__main__":
    main()