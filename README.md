# NLP Tweet Generator

Josh Seol
Sai Singireddy
Zhong Zhu

This program will utilize various POS tagging and tokenizing methods to parse Twitter corpuses and generate random Tweets, eventually leading to an ecosystem of multiple Twitter bots tweeting with each other.

## Introduction
Much research has been conducted in the recent past to understand and exploit the data presented on Twitter (twitter.com). Our tweet analysis & generation program is an attempt to model how people will post on Twitter about various topics. Twitter is a social media platform based on three states of text -- question, statement, and answer -- and we aim to tap into this potential of analyzing then generating questions, statements, and answers to provide potential improvements in the field of automated short-text bots (e.g. help-center text-bots). 

We will focus on the accounts of popular Twitter influencers’ texts and attempt to mimic their ways of texting, such as vocabulary and rhetoric, by generating dictionaries of their vocabulary and using Part-of-Speech (POS) Tagging to implement likelihood and transition tables specific to each personality. Therefore, the generated tweets should resemble past tweets from the influencer based on the algorithms of our tweet generation. We will then attempt to use Topic Identification to understand the keywords of each generated Tweet and have other chatbots reply as on-topic as possible to a tweet/topic, while remaining coherent. We hope this demonstration will lead to advancements categorizing microblog posts to analyze large amounts of data from social media, especially in an era where platforms such as Twitter has become a source for breaking news and trending events.

## Instructions to generate all Tweets

$ ./generate_tweets

### To generate Tweet based on a corpora

$ python3 tweetgen.py <tagged input corpora>

#### Example

$ python3 tweetgen.py corpora/Tagged/djkhaled_tweets_tagged.txt

### To download Tweets of an account

$ python tweet_dumper.py <Twitter Account>

To start tag the tweets, move the file to twitie-tagger/corpora/untagged and follow the instructions on the README to run the twitie_tag.jar and it will produce a tagged corpus.
