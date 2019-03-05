import sys

isAB = False
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
cLine = list()

#Defines features
def featuresAllTest(word, pWord, pWord2, nWord, nWord2):
	try: 
		pos = word[1]
	except:
		return ""
	featureWord = word[0] + "\t" + "POS=" + pos + "\t" 
	
	try:
		p_pos = pWord[1]
	except: 
		p_pos = "sentence_break"
	finally:
		featureWord += "previous_Word=" + pWord[0] + "\t" + "previous_POS=" + p_pos + "\t"
	
	try:
		p2_pos = pWord2[1]
	except: 
		p2_pos = "sentence_break"
	finally:
		featureWord += "previous2_Word=" + pWord2[0] + "\t" + "previous2_POS=" + p2_pos + "\t"

	try: 
		n_pos = nWord[1]
	except:
		n_pos = "sentence_break"
	finally:
		featureWord += "next_Word=" + nWord[0] + "\t" + "next_POS=" + n_pos + "\t"

	try: 
		n2_pos = nWord2[1]
	except:
		n2_pos = "sentence_break"
	finally:
		featureWord += "next2_Word=" + nWord2[0] + "\t" + "next2_POS=" + n2_pos + "\t"

	#Check for Proper Nouns
	if((pos == ("NNP" or "NNPS")) or (p_pos != "sentence_break" and word[0] != "I")):
		if(word[0].isupper()):
			featureWord += "PROPER_NOUN\t"

	#Check for Proper Noun Groups 
	if((p_pos == ("NNP" or "NNPS")) or (n_pos == ("NNP" or "NNPS"))):
		if(pos == ("NNP" or "NNPS")):
			featureWord += "PROPER_NOUN_GROUP\t"

	#Check for Noun Groups
	if(pos == ("DT" or "JJ" or "JJS" or "JJR" or "CD")):
		if(n_pos == ("JJ" or "JJS" or "JJR" or "NN" or "NNS" or "NNP" or "NPPS" or "CD" )):
			featureWord += "NOUN_GROUP\t"

	#Check for Money
	if(word[0] == "$"):
		featureWord += "MONEY\t"
	elif(pWord == "$"):
		featureWord += "MONEY\t"

	if("." in word[0]):
		for char in word[0]:
			if(char.isupper() or char == "."):
				isAB = True
			else:
				isAB = False
				break
		if(isAB):
			featureWord += "ABBREVIATION\t"

	if((p_pos == "IN") and (pos == ("NNP" or "NNPS"))):
		featureWord += "LOC\t"
	if(word[0] in months):
		featureWord += "DATE\t"
	if(pos == "CD"):
		if((pWord in months) or (nWord in months)):
			featureWord += "DATE\t"
	
	if(pos == ("NNS" or "NNPS")):
		featureWord += "PLURAL\t"
	
	if(pos == ("VBN" or "VBD")):
		featureWord += "PAST\t"
	elif(pos == ("VBP" or "VBG" or "VBZ")):
		featureWord += "PRESENT\t"
	elif(pos == "MD"):
		featureWord += "FUTURE\t"
	
	if(pos == "UH"):
		featureWord += "SLANG\t"
	if(pos == "."):
		featureWord += "PUNCTUATION\t"
	if(pos == "POS" or n_pos == "POS"):
		featureWord += "POSSESSIVE\t"
	
	return featureWord

def featuresN2Test(word, nWord, nWord2):
	try: 
		pos = word[1]
	except:
		return ""
	featureWord = word[0] + "\t" + "POS=" + pos + "\t" 
	
	try:
		n_pos = nWord[1]
	except: 
		n_pos = "sentence_break"
	finally:
		featureWord += "next_Word=" + nWord[0] + "\t" + "next_POS=" + n_pos + "\t"
	
	try:
		n2_pos = nWord2[1]
	except: 
		n2_pos = "sentence_break"
	finally:
		featureWord += "next2_Word=" + nWord2[0] + "\t" + "next2_POS=" + n2_pos + "\t"

	#Check for Proper Nouns
	if(pos == ("NNP" or "NNPS")):
		if(word[0].isupper()):
			featureWord += "PROPER_NOUN\t"

	#Check for Proper Noun Groups 
	if((n_pos == ("NNP" or "NNPS"))):
		if(pos == ("NNP" or "NNPS")):
			featureWord += "PROPER_NOUN_GROUP\t"

	#Check for Noun Groups
	if(pos == ("DT" or "JJ" or "JJS" or "JJR" or "CD")):
		if(n_pos == ("JJ" or "JJS" or "JJR" or "NN" or "NNS" or "NNP" or "NPPS" or "CD")):
			featureWord += "NOUN_GROUP\t"

	#Check for Money
	if(word[0] == "$"):
		featureWord += "MONEY\t"

	if("." in word[0]):
		for char in word[0]:
			if(char.isupper() or char == "."):
				isAB = True
			else:
				isAB = False
				break
		if(isAB):
			featureWord += "ABBREVIATION\t"

	if(word[0] in months):
		featureWord += "DATE\t"
	if(pos == "CD"):
		if(nWord in months):
			featureWord += "DATE\t"
	
	if(pos == ("NNS" or "NNPS")):
		featureWord += "PLURAL\t"
	
	if(pos == ("VBN" or "VBD")):
		featureWord += "PAST\t"
	elif(pos == ("VBP" or "VBG" or "VBZ")):
		featureWord += "PRESENT\t"
	elif(pos == "MD"):
		featureWord += "FUTURE\t"

	if(pos == "UH"):
		featureWord += "SLANG\t"
	if(pos == "."):
		featureWord += "PUNCTUATION\t"
	if(pos == "POS" or n_pos == "POS"):
		featureWord += "POSSESSIVE\t"

	return featureWord

def featuresNTest(word, nWord):
	try: 
		pos = word[1]
	except:
		return ""
	featureWord = word[0] + "\t" + "POS=" + pos + "\t" 
	
	try:
		n_pos = nWord[1]
	except: 
		n_pos = "sentence_break"
	finally:
		featureWord += "next_Word=" + nWord[0] + "\t" + "next_POS=" + n_pos + "\t"

	#Check for Proper Nouns
	if(pos == ("NNP" or "NNPS")):
		if(word[0].isupper()):
			featureWord += "PROPER_NOUN\t"
	
	#Check for Proper Noun Groups 
	if(n_pos == ("NNP" or "NNPS")):
		if(pos == ("NNP" or "NNPS")):
			featureWord += "PROPER_NOUN_GROUP\t"

	#Check for Noun Groups
	if(pos == ("DT" or "JJ" or "JJS" or "JJR" or "CD")):
		if(n_pos == ("JJ" or "JJS" or "JJR" or "NN" or "NNS" or "NNP" or "NPPS" or "CD" )):
			featureWord += "NOUN_GROUP\t"

	#Check for Money
	if(word[0] == "$"):
		featureWord += "MONEY\t"

	if("." in word[0]):
		for char in word[0]:
			if(char.isupper() or char == "."):
				isAB = True
			else:
				isAB = False
				break
		if(isAB):
			featureWord += "ABBREVIATION\t"

	if(word[0] in months):
		featureWord += "DATE\t"
	if(pos == "CD"):
		if (nWord in months):
			featureWord += "DATE\t"
	
	if(pos == ("NNS" or "NNPS")):
		featureWord += "PLURAL\t"
	
	if(pos == ("VBN" or "VBD")):
		featureWord += "PAST\t"
	elif(pos == ("VBP" or "VBG" or "VBZ")):
		featureWord += "PRESENT\t"
	elif(pos == "MD"):
		featureWord += "FUTURE\t"

	if(pos == "UH"):
		featureWord += "SLANG\t"
	if(pos == "."):
		featureWord += "PUNCTUATION\t"
	if(pos == "POS" or n_pos == "POS"):
		featureWord += "POSSESSIVE\t"

	return featureWord

def featuresP2Test(word, pWord, pWord2):
	try: 
		pos = word[1]
	except:
		return ""
	featureWord = word[0] + "\t" + "POS=" + pos + "\t" 
	
	try:
		p_pos = pWord[1]
	except: 
		p_pos = "sentence_break"
	finally:
		featureWord += "previous_Word=" + pWord[0] + "\t" + "previous_POS=" + p_pos + "\t"
	
	try:
		p2_pos = pWord2[1]
	except: 
		p2_pos = "sentence_break"
	finally:
		featureWord += "previous2_Word=" + pWord2[0] + "\t" + "previous2_POS=" + p2_pos + "\t"

	#Check for Proper Nouns
	if((pos == ("NNP" or "NNPS")) or (p_pos != "sentence_break" and word[0] != "I")):
		if(word[0].isupper()):
			featureWord += "PROPER_NOUN\t"
	
	#Check for Proper Noun Groups 
	if(p_pos == ("NNP" or "NNPS")):
		if(pos == ("NNP" or "NNPS")):
			featureWord += "PROPER_NOUN_GROUP\t"

	#Check for Money
	if(word[0] == "$"):
		featureWord += "MONEY\t"
	elif(pWord == "$"):
		featureWord += "MONEY\t"

	if("." in word[0]):
		for char in word[0]:
			if(char.isupper() or char == "."):
				isAB = True
			else:
				isAB = False
				break
		if(isAB):
			featureWord += "ABBREVIATION\t"

	if((p_pos == "IN") and (pos == ("NNP" or "NNPS"))):
		featureWord += "LOC\t"
	if(word[0] in months):
		featureWord += "DATE\t"
	if(pos == "CD"):
		if(pWord in months):
			featureWord += "DATE\t"
	
	if(pos == ("NNS" or "NNPS")):
		featureWord += "PLURAL\t"
	
	if(pos == ("VBN" or "VBD")):
		featureWord += "PAST\t"
	elif(pos == ("VBP" or "VBG" or "VBZ")):
		featureWord += "PRESENT\t"
	elif(pos == "MD"):
		featureWord += "FUTURE\t"

	if(pos == "UH"):
		featureWord += "SLANG\t"
	if(pos == "."):
		featureWord += "PUNCTUATION\t"
	if(pos == "POS"):
		featureWord += "POSSESSIVE\t"

	return featureWord

def featuresPTest(word, pWord):
	try: 
		pos = word[1]
	except:
		return ""
	featureWord = word[0] + "\t" + "POS=" + pos + "\t" 
	
	try:
		p_pos = pWord[1]
	except: 
		p_pos = "sentence_break"
	finally:
		featureWord += "previous_Word=" + pWord[0] + "\t" + "previous_POS=" + p_pos + "\t"
	
	#Check for Proper Nouns
	if((pos == ("NNP" or "NNPS")) or (p_pos != "sentence_break" and word[0] != "I")):
		if(word[0].isupper()):
			featureWord += "PROPER_NOUN\t"
	
	#Check for Proper Noun Groups 
	if(p_pos == ("NNP" or "NNPS")):
		if(pos == ("NNP" or "NNPS")):
			featureWord += "PROPER_NOUN_GROUP\t"

	#Check for Money
	if(word[0] == "$"):
		featureWord += "MONEY\t"
	elif(pWord == "$"):
		featureWord += "MONEY\t"

	if("." in word[0]):
		for char in word[0]:
			if(char.isupper() or char == "."):
				isAB = True
			else:
				isAB = False
				break
		if(isAB):
			featureWord += "ABBREVIATION\t"

	if((p_pos == "IN") and (pos == ("NNP" or "NNPS"))):
		featureWord += "LOC\t"
	if(word[0] in months):
		featureWord += "DATE\t"
	if pos == "CD":
		if(pWord in months):
			featureWord += "DATE\t"
	
	if(pos == ("NNS" or "NNPS")):
		featureWord += "PLURAL\t"
	
	if(pos == ("VBN" or "VBD")):
		featureWord += "PAST\t"
	elif(pos == ("VBP" or "VBG" or "VBZ")):
		featureWord += "PRESENT\t"
	elif(pos == "MD"):
		featureWord += "FUTURE\t"

	if(pos == "UH"):
		featureWord += "SLANG\t"
	if(pos == "."):
		featureWord += "PUNCTUATION\t"
	if(pos == "POS"):
		featureWord += "POSSESSIVE\t"

	return featureWord

def features1Test(word, pWord, nWord):
	try: 
		pos = word[1]
	except:
		return ""
	featureWord = word[0] + "\t" + "POS=" + pos + "\t" 
	
	try:
		p_pos = pWord[1]
	except: 
		p_pos = "sentence_break"
	finally:
		featureWord += "previous_word=" + pWord[0] + "\t" + "previous_POS=" + p_pos + "\t"
	
	try: 
		n_pos = nWord[1]
	except:
		n_pos = "sentence_break"
	finally:
		featureWord += "next_Word=" + nWord[0] + "\t" + "next_POS=" + n_pos + "\t"

	#Check for Proper Nouns
	if((pos == ("NNP" or "NNPS")) or (p_pos != "sentence_break" and word[0] != "I")):
		if(word[0].isupper()):
			featureWord += "PROPER_NOUN\t"
	
	#Check for Proper Noun Groups 
	if((p_pos == ("NNP" or "NNPS")) or (n_pos == ("NNP" or "NNPS"))):
		if(pos == ("NNP" or "NNPS")):
			featureWord += "PROPER_NOUN_GROUP\t"

	#Check for Noun Groups
	if(pos == ("DT" or "JJ" or "JJS" or "JJR" or "CD")):
		if(n_pos == ("JJ" or "JJS" or "JJR" or "NN" or "NNS" or "NNP" or "NPPS" or "CD" )):
			featureWord += "NOUN_GROUP\t"

	#Check for Money
	if(word[0] == "$"):
		featureWord += "MONEY\t"
	elif(pWord == "$"):
		featureWord += "MONEY\t"

	if("." in word[0]):
		for char in word[0]:
			if(char.isupper() or char == "."):
				isAB = True
			else:
				isAB = False
				break
		if(isAB):
			featureWord += "ABBREVIATION\t"

	if((p_pos == "IN") and (pos == ("NNP" or "NNPS"))):
		featureWord += "LOC\t"

	if(word[0] in months):
		featureWord += "DATE\t"
	if(pos == "CD"):
		if ((pWord in months) or (nWord in months)):
			featureWord += "DATE\t"
	
	if(pos == ("NNS" or "NNPS")):
		featureWord += "PLURAL\t"
	
	if(pos == ("VBN" or "VBD")):
		featureWord += "PAST\t"
	elif(pos == ("VBP" or "VBG" or "VBZ")):
		featureWord += "PRESENT\t"
	elif(pos == "MD"):
		featureWord += "FUTURE\t"

	if(pos == "UH"):
		featureWord += "SLANG\t"
	if(pos == "."):
		featureWord += "PUNCTUATION\t"
	if(pos == "POS" or n_pos == "POS"):
		featureWord += "POSSESSIVE\t"

	return featureWord

def features1NTest(word, pWord, nWord, nWord2):
	try: 
		pos = word[1]
	except:
		return ""
	featureWord = word[0] + "\t" + "POS=" + pos + "\t" 
	
	try:
		p_pos = pWord[1]
	except: 
		p_pos = "sentence_break"
	finally:
		featureWord += "previous_Word=" + pWord[0] + "\t" + "previous_POS=" + p_pos + "\t"
	
	try: 
		n_pos = nWord[1]
	except:
		n_pos = "sentence_break"
	finally:
		featureWord += "next_Word=" + nWord[0] + "\t" + "next_POS=" + n_pos + "\t"

	try: 
		n2_pos = nWord2[1]
	except:
		n2_pos = "sentence_break"
	finally:
		featureWord += "next2_Word=" + nWord2[0] + "\t" + "next2_POS=" + n2_pos + "\t"

	#Check for Proper Nouns
	if((pos == ("NNP" or "NNPS")) or (p_pos != "sentence_break" and word[0] != "I")):
		if(word[0].isupper()):
			featureWord += "PROPER_NOUN\t"
	
	#Check for Proper Noun Groups 
	if((p_pos == ("NNP" or "NNPS")) or (n_pos == ("NNP" or "NNPS"))):
		if(pos == ("NNP" or "NNPS")):
			featureWord += "PROPER_NOUN_GROUP\t"

	#Check for Noun Groups
	if(pos == ("DT" or "JJ" or "JJS" or "JJR" or "CD")):
		if(n_pos == ("JJ" or "JJS" or "JJR" or "NN" or "NNS" or "NNP" or "NPPS" or "CD" )):
			featureWord += "NOUN_GROUP\t"

	#Check for Money
	if(word[0] == "$"):
		featureWord += "MONEY\t"
	elif(pWord == "$"):
		featureWord += "MONEY\t"

	if("." in word[0]):
		for char in word[0]:
			if(char.isupper() or char == "."):
				isAB = True
			else:
				isAB = False
				break
		if(isAB):
			featureWord += "ABBREVIATION\t"

	if((p_pos == "IN") and (pos == ("NNP" or "NNPS"))):
		featureWord += "LOC\t"
	if(word[0] in months):
		featureWord += "DATE\t"
	if(pos == "CD"):
		if((pWord in months) or (nWord in months)):
			featureWord += "DATE\t"

	if(pos == ("NNS" or "NNPS")):
		featureWord += "PLURAL\t"
	
	if(pos == ("VBN" or "VBD")):
		featureWord += "PAST\t"
	elif(pos == ("VBP" or "VBG" or "VBZ")):
		featureWord += "PRESENT\t"
	elif(pos == "MD"):
		featureWord += "FUTURE\t"

	if(pos == "UH"):
		featureWord += "SLANG\t"
	if(pos == "."):
		featureWord += "PUNCTUATION\t"
	if(pos == "POS" or n_pos == "POS"):
		featureWord += "POSSESSIVE\t"

	return featureWord

def features1PTest(word, pWord, pWord2, nWord):
	try: 
		pos = word[1]
	except:
		return ""
	featureWord = word[0] + "\t" + "POS=" + pos + "\t" 
	
	try:
		p_pos = pWord[1]
	except: 
		p_pos = "sentence_break"
	finally:
		featureWord += "previous_Word=" + pWord[0] + "\t" + "previous_POS=" + p_pos + "\t"
	
	try:
		p2_pos = pWord2[1]
	except: 
		p2_pos = "sentence_break"
	finally:
		featureWord += "previous2_Word=" + pWord2[0] + "\t" + "previous2_POS=" + p2_pos + "\t"

	try: 
		n_pos = nWord[1]
	except:
		n_pos = "sentence_break"
	finally:
		featureWord += "next_Word=" + nWord[0] + "\t" + "next_POS=" + n_pos + "\t"

	#Check for Proper Nouns
	if((pos == ("NNP" or "NNPS")) or (p_pos != "sentence_break" and word[0] != "I")):
		if(word[0].isupper()):
			featureWord += "PROPER_NOUN\t"
	
	#Check for Proper Noun Groups 
	if((p_pos == ("NNP" or "NNPS")) or (n_pos == ("NNP" or "NNPS"))):
		if(pos == ("NNP" or "NNPS")):
			featureWord += "PROPER_NOUN_GROUP\t"

	#Check for Noun Groups
	if(pos == ("DT" or "JJ" or "JJS" or "JJR" or "CD")):
		if(n_pos == ("JJ" or "JJS" or "JJR" or "NN" or "NNS" or "NNP" or "NPPS" or "CD")):
			featureWord += "NOUN_GROUP\t"

	#Check for Money
	if(word[0] == "$"):
		featureWord += "MONEY\t"
	elif(pWord == "$"):
		featureWord += "MONEY\t"

	if("." in word[0]):
		for char in word[0]:
			if(char.isupper() or char == "."):
				isAB = True
			else:
				isAB = False
				break
		if(isAB):
			featureWord += "ABBREVIATION\t"

	if((p_pos == "IN") and (pos == ("NNP" or "NNPS"))):
		featureWord += "LOC\t"
	if(word[0] in months):
		featureWord += "DATE\t"
	if(pos == "CD"):
		if((pWord in months) or (nWord in months)):
			featureWord += "DATE\t"
	
	if(pos == ("NNS" or "NNPS")):
		featureWord += "PLURAL\t"
	
	if(pos == ("VBN" or "VBD")):
		featureWord += "PAST\t"
	elif(pos == ("VBP" or "VBG" or "VBZ")):
		featureWord += "PRESENT\t"
	elif(pos == "MD"):
		featureWord += "FUTURE\t"

	if(pos == "UH"):
		featureWord += "SLANG\t"
	if(pos == "."):
		featureWord += "PUNCTUATION\t"
	if(pos == "POS" or n_pos == "POS"):
		featureWord += "POSSESSIVE\t"
		
	return featureWord

def buildFile(inF, out):
	del cLine[:]
	with open(inF, "r") as inFile:
		for line in inFile:
			if line == '\n': 
				content = "\n"
				cLine.append(content)
			else:
				content = line.rstrip('\n').split('_')
				cLine.append(content)
	with open(out, "w") as outFile:
		for i in range(len(cLine)):
			try:
				if(cLine[i-1] == "\n"):
					pWord = "break"
				else:
					pWord = cLine[i-1]
			except:
				pWord = None
			try:
				if(cLine[i-2] == "\n"):
					pWord2 = "break"
				else:
					pWord2 = cLine[i-2]
			except:
				pWord2 = None
			try:
				if(cLine[i+1] == "\n"):
					nWord = "break"
				else:
					nWord = cLine[i+1]
			except:
				nWord = None
			try:
				if(cLine[i+2] == "\n"):
					nWord2 = "break"
				else:
					nWord2 = cLine[i+2]
			except:
				nWord2 = None
			word = cLine[i]
			if(word == "\n"):
				outFile.write('\n\n')
				continue
			elif(i <= 1): #First 2, do not have previous positions
				word = featuresN2Test(word, nWord, nWord2)
				outFile.write(word + '\n')					
			elif(i>1 and i < (len(cLine)-2)):
				if(cLine[i-2] == "\n"): #Second previous == new line
					if(cLine[i+2] == "\n"): #Second next == new line
						word = features1Test(word, pWord, nWord)
						outFile.write(word + '\n')	
					elif(cLine[i+1] == "\n"): #Next == new line
						word = featuresPTest(word, pWord)
						outFile.write(word + '\n')	
					else: #Otherwise use both next words
						word = features1NTest(word, pWord, nWord, nWord2)
						outFile.write(word + '\n')	
				elif(cLine[i-1] == "\n"): #Previous == new line
					if(cLine[i+2] == "\n"): #Second next == new line
						word = featuresNTest(word, nWord)
						outFile.write(word + '\n')	
					else:
						word = featuresN2Test(word, nWord, nWord2)
						outFile.write(word + '\n')
					#elif(cLine[i+1] == ""): --single word, too short to consider? 
					#	word = featuresTrain1(word, isTrain)
				elif(cLine[i+2] == "\n"): #Second next == new line
					word = features1PTest(word, pWord, pWord2, nWord)
					outFile.write(word + '\n')
				elif(cLine[i+1] == "\n"): #Next == new line
					word = featuresP2Test(word, pWord, pWord2)
					outFile.write(word + '\t')				
				else:
					word = featuresAllTest(word, pWord, pWord2, nWord, nWord2)
					outFile.write(word + '\n')	
			elif(i == (len(cLine)-2)): #For second to last - does not have next position
				word = features1PTest(word, pWord, pWord2, nWord)
				outFile.write(word + '\n')	
			else: #Last - does not have next positions
				word = featuresP2Test(word, pWord, nWord2)
				outFile.write(word + '\n')	


"""def main():
	buildFile(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
	main()
"""

def main(arg1, arg2):
    buildFile(arg1, arg2)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])