import nltk
import re

word = "\"Reallyness's."
word = re.sub('[^0-9a-zA-Z]+', '', word)

print(word)