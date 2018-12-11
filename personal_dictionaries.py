#Creates dictionaries for chatbots. 
#FORMAT: dictionary[POS] = {POS1:dict of words+features, POS2:dict of words+features}
    #POS1[sample_word_1] = list_of_features

    #Get probability of POS used from probabilities, then select word from here
    #For features that match with tweet, add a counter. Choose randomly between highest valued words to put in sentence.
