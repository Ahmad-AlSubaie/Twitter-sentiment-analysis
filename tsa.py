"""
Jason Yin and Ahmad Alsubaie
Twitter sentiment analysis, python code, cs499nlp
remember to do this to install libraries:
pip install textblob and pip install tweepy and pip install vaderSentiment
"""
import re #regular expression
import tweepy #python client for official twitter api, install with 'pip install tweepy'
import textblob #process text library, use 'pip install textblob' and 'python -m textblob.download_corpora'
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import nltk
import pycountry
import string
from textblob import TextBlob
from tweepy import OAuthHandler #authentication
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#authenticate
apiKey =""
apiSecret =""
accessToken =""
accessSecret =""

authen = tweepy.OAuthHandler(apiKey, apiSecret)
authen.set_access_token(accessToken, accessSecret)
api = tweepy.API(authen)

#searching Twitter
positive = 0
negative = 0
neutral = 0
searchword = input("Enter hashtag or keyword for search: ")
numTweets = int(input("How many tweets would you like to analyze?: "))
tweets = tweepy.Cursor(api.search,q=searchword,lang="en",result_type="mixed",include_entities=False).items(numTweets)
tweet_lis = []
pos_lis = []
neg_lis = []
neutral_lis = []
polarity = 0
filep = open("ExtractedTweets.txt",'w',encoding="utf-8")
def percent(numer,denom):
    return 100*float(numer)/float(denom)

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons, emotes
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map stuff/symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS phone stuff)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

for tweet in tweets:
    print(tweet.text) #prints tweet text
    filep.write(deEmojify(tweet.text)) #write to output file
    #basically up to this point all the stuff above is useful for processing tweets, saving to the txt file, and removing emojis and other special characters
    tweet_lis.append(tweet.text)

    anal = TextBlob(tweet.text)#analysis part
    polscore = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
    neut = polscore["neu"]
    pos = polscore["pos"]
    nega = polscore["neg"]
    c = polscore['compound']
    polarity = polarity + anal.sentiment.polarity

    if nega > pos:
        neg_lis.append(tweet.text)
        negative=negative+1
    elif pos > nega:
        pos_lis.append(tweet.text)
        positive=positive+1
    elif nega == pos:
        neutral_lis.append(tweet.text)
        neutral=neutral+1
positive = percent(positive,numTweets)
neutral = percent(neutral,numTweets)
negative = percent(negative,numTweets)
polarity = percent(polarity,numTweets)

#total, pos, neg, neutral
tweet_lis = pd.DataFrame(tweet_lis)
neg_lis = pd.DataFrame(neg_lis)
neutral_lis = pd.DataFrame(neutral_lis)
pos_lis = pd.DataFrame(pos_lis)

#printing
print("Total tweets: ",len(tweet_lis))
print("Positive tweets: ",len(pos_lis))
print("Neutral tweets: ",len(neutral_lis))
print("Negative tweets: ",len(neg_lis))

#Could make a chart
