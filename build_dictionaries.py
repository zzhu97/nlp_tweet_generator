import sys

#Hash table of POS and word frequencies based on POS
likelihood = dict() #{"VB": dict(), "VBP": dict(), "VBZ": dict(), "VBD": dict(), "VBG": dict(), "VBN": dict(), "NNP": dict(), "NNPS": dict(), "NN": dict(), "NNS": dict(), "JJ": dict(), "JJR": dict(), "JJS": dict(), "RB": dict(), "RBR": dict(), "RBS": dict(), "RP": dict(), "PRP": dict(), "PP$": dict(), "WP": dict(), "WP$": dict(), "WDT": dict(), "WRB": dict(), "CC": dict(), "CD": dict(), "DT": dict(), "PDT": dict(), "IN": dict(), "MD": dict(), "#": dict(), "$": dict(), ".": dict(), ",": dict(), ":": dict(), "(": dict(), ")": dict(), '"': dict(), "'": dict(), "''": dict(), "``": dict(), "FW": dict(), "SYM": dict(), "LS": dict(), "TO": dict(), "POS": dict(), "UH": dict(), "EX": dict(), "PRP$": dict(), "SENTENCE_BREAK": dict(), "OOV": dict(), }
#Hash table of POS and transitions to next POS
transitions = dict() #{"VB": dict(), "VBP": dict(), "VBZ": dict(), "VBD": dict(), "VBG": dict(), "VBN": dict(), "NNP": dict(), "NNPS": dict(), "NN": dict(), "NNS": dict(), "JJ": dict(), "JJR": dict(), "JJS": dict(), "RB": dict(), "RBR": dict(), "RBS": dict(), "RP": dict(), "PRP": dict(), "PP$": dict(), "WP": dict(), "WP$": dict(), "WDT": dict(), "WRB": dict(), "CC": dict(), "CD": dict(), "DT": dict(), "PDT": dict(), "IN": dict(), "MD": dict(), "#": dict(), "$": dict(), ".": dict(), ",": dict(), ":": dict(), "(": dict(), ")": dict(), '"': dict(), "'": dict(), "''": dict(), "``": dict(), "FW": dict(), "SYM": dict(), "LS": dict(), "TO": dict(), "POS": dict(), "UH": dict(), "EX": dict(), "PRP$": dict(), "SENTENCE_BREAK": dict(), "OOV": dict(), }

###Build likelihood dictionary word --> pos --> count
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