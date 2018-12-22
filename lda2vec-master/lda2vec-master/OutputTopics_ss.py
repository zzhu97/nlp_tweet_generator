from lda2vec import preprocess, Corpus
import matplotlib.pyplot as plt
import numpy as np
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

try:
    import seaborn
except:
    pass
import pyLDAvis
pyLDAvis.enable_notebook()
npz = np.load(open('topics.pyldavis.npz', 'r'))
dat = {k: v for (k, v) in npz.iteritems()}
dat['vocab'] = dat['vocab'].tolist()
top_n = 10
topic_to_topwords = {}
for j, topic_to_word in enumerate(dat['topic_term_dists']):
    top = np.argsort(topic_to_word)[::-1][:top_n]
    msg = 'Topic %i '  % j
    top_words = [dat['vocab'][i].strip()[:35] for i in top]
    msg += ' '.join(top_words)
    print msg
    topic_to_topwords[j] = top_words