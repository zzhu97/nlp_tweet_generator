import nltk
import random
import string
import re
import global_vars
from numpy.random import choice

#Chatbot class
class Chatbot:
    def __init__(self, name, corpus_tagged):
        self.name = name
        self.endwords = list() #Format: List of tuples of format [word, pos]
        self.startwords = list()
        self.likelihood_table, self.transitions_table, self.words_by_pos = self.initiate_personal_dictionary(corpus_tagged)
        self.startwords = self.clean_start_words() #Format: List of tuples of format [word, pos]

    #Generates a tweet. 
    def generate_tweet(self):
        table = self.likelihood_table
        stack = ""
        expand = True

        start = (random.choice(self.startwords))
        current_pos = start[1]
        current_word = start[0]

        #TEST
        #print(current_word, "--> ", current_pos)

        stack += (current_word) + " "
        while (expand == True and len(stack) < 140):
            winner_word = ""
            winner_pos = ""
            winner = float(0)
            candidate = float(0)
            choices = list()

            for next_pos in self.transitions_table[current_pos]:
                pos_prob = self.transitions_table[current_pos][next_pos]
                for word in self.words_by_pos[next_pos]:
                    try:
                        candidate = pos_prob * self.likelihood_table[current_word][word]
                        #print(word, ": ", candidate)
                    except:
                        candidate = 0
                    else:
                        if candidate > winner:
                            if winner_word in self.endwords:
                                #Attempt to end the tweet if a endword is encountered.
                                if len(stack) > 70:
                                    winner_word += "."
                                    expand = False
                                else:
                                    pass
                            winner = candidate
                            winner_word = word
                            winner_pos = next_pos
                            choices.insert(0, [winner_word, winner_pos])
            if winner == 0:
                selection = random.choice(self.endwords)
                winner_word = selection[0]
                winner_pos = selection[1]
                expand = False
                stack += winner_word + "."
                break

            #Take the highest scored possible words and randomly pick
            choices = choices[:5]
            winner_tuple = random.choice(choices)
            winner_word = winner_tuple[0]
            winner_pos = winner_tuple[1]

            stack += winner_word + " "

            current_word = winner_word
            current_pos = winner_pos
        print(stack)
    
    def initiate_personal_dictionary(self, fileIn):
        table = dict()
        pos_table = dict()
        words_by_pos = dict()
        prev_word = ""
        prev_pos = "SENT_BREAK"
        word = ""
        pos = ""
        sentence_end_flag = False

        with open(fileIn, "r") as trainingFile:
            pos_table["SENT_BREAK"] = dict()
            for line in trainingFile:
                prev_pos = "SENT_BREAK"
                prev_word = ""
                if line == "\n":
                    continue
                else:
                    line = line.rstrip('\n').split(" ")

                    for element in line:
                        element = element.replace('"', '').split("_")
                        sentence_end_flag = False
                        word = element[0]
                        pos = element[1]

                        if all(j in string.punctuation for j in word):
                            continue

                        try:
                            if word in words_by_pos[pos]:
                                pass
                            else:
                                words_by_pos[pos].append(word)
                        except:
                            words_by_pos[pos] = list()

                        if prev_pos == "SENT_BREAK":
                            self.add_start_word([word, pos])

                        #If a word ends with punctuation, treat it as an endword
                        if re.match('[.:;-?!]', word[-1]) is not None:
                            word = word[:-1]
                            self.add_stop_word([word, pos])
                            sentence_end_flag = True
                            pos = "SENT_BREAK"
                        #Parse commas from words
                        if word[-1] == ",":
                            word = word[:-1]
                        if (pos == "URL"):
                            pos = "URL"
                        if (word[:4] == "http"):
                            pos = "URL"
                        #Normalize non-proper words
                        if (pos != "NNP" and pos != "NNPS"):
                            word = word.lower()

                        #print(prev_word, "--> ", word)
                        #print(prev_pos, "-->", pos)

                        #Update Likelihood
                        if prev_word not in table:
                            table[prev_word] = dict()
                        if word not in table[prev_word]:
                            table[prev_word][word] = 1
                        else:
                            table[prev_word][word] += 1
                        #Update transitions
                        if prev_pos not in pos_table:
                            pos_table[prev_pos] = dict()
                        if pos not in pos_table[prev_pos]:
                            pos_table[prev_pos][pos] = 1
                        else:
                            pos_table[prev_pos][pos] += 1

                        prev_word = word
                        if (sentence_end_flag == False):
                            prev_pos = pos
                        else:
                            prev_pos = "SENT_BREAK"

        for previous_word in table:
            count = 0
            for word in table[previous_word]:
                count += table[previous_word][word]
            for word in table[previous_word]:
                oldcount = float(table[previous_word][word])
                table[previous_word][word] = float(oldcount) / float(count)
        for previous_pos in pos_table:
            count = 0
            for pos in pos_table[previous_pos]:
                count += pos_table[previous_pos][pos]
            for pos in pos_table[previous_pos]:
                oldcount = float(pos_table[previous_pos][pos])
                pos_table[previous_pos][pos] = float(oldcount) / float(count)

        words_by_pos["SENT_BREAK"] = list()

        return table, pos_table, words_by_pos

    def add_stop_word(self, mini_tuple): #word, pos
        self.endwords.append(mini_tuple)

    def add_start_word(self, mini_tuple):
        self.startwords.append(mini_tuple)

    #Prevents URLs from starting sentences.
    def clean_start_words(self):
        temp = list(self.startwords)
        for token in temp:
            if token[0][:4] == "http":
                temp.remove(token)
        return temp

    def tester(self):
        self.generate_tweet()
        #for word in self.endwords:
        #    print(word)
        pass

        