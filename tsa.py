"""
Jason Yin and Ahmad Alsubaie
Twitter sentiment analysis, python code, cs499nlp
"""
import re #regular expression
import tweepy #python client for official twitter api, install with 'pip install tweepy'
import textblob #process text library, use 'pip install textblob' and 'python -m textblob.download_corpora'
from textblobk import Textblob
from tweepy import OAuthHandler #authentication


