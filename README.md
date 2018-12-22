# NLP Tweet Generator

Josh Seol
Sai Singireddy
Zhong Zhu

This program will utilize various POS tagging and tokenizing methods to parse Twitter corpuses and generate random Tweets, eventually leading to an ecosystem of multiple Twitter bots tweeting with each other.

PROBLEM STATEMENT:
Twitter is a form of mass media in which a lot of people can express their feelings about many topics on this platform. By analyzing certain celebrity tweets about certain topics, we can predict what people will say about certain topics. Hopefully, this can be expanded to demonstrate future topics of conversation about a subject before they come up.

## Instructions to generate all Tweets

$ ./generate_tweets

### To generate Tweet based on a corpora

$ python3 tweetgen.py <tagged input corpora>

#### Example

$ python3 tweetgen.py corpora/Tagged/djkhaled_tweets_tagged.txt

### To download Tweets of an account

$ python tweet_dumper.py <Twitter Account>

To start tag the tweets, move the file to twitie-tagger/corpora/untagged and follow the instructions on the README to run the twitie_tag.jar and it will produce a tagged corpus.
