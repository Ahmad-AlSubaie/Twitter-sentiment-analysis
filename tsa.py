"""
Jason Yin and Ahmad Alsubaie
Twitter sentiment analysis, python code, cs499nlp
remember to do this to install libraries:
pip install textblob and pip install tweepy
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
from textblobk import Textblob
from tweepy import OAuthHandler #authentication

#authenticate
apiKey = ""
apiSecret = ""
accessToken = ""
accessSecret = ""

authen = tweepy.OAuthHandler(apiKey, apiSecret)
authen.set_access_token(accessToken, accessSecret)
api = tweepy.API(authen)

#searching Twitter
positive = 0
negative = 0
neutral = 0
searchword = input("Enter hashtag or keyword for search: ")
numTweets = int(input("How many tweets would you like to analyze?: "))
tweets = tweepy.Cursor(api.search,q=keyword).items(numTweets)
tweet_lis = []
pos_lis = []
neg_lis = []
neutral_lis = []
for tweet in tweets:
    print(tweet.text) #prints tweet text
    tweet_lis.append(tweet.text)
