import os
import subprocess
import tweepy


#authenticate


authen = tweepy.OAuthHandler(apiKey, apiSecret)
authen.set_access_token(accessToken, accessSecret)
api = tweepy.API(authen)

def tweet_search(keyword, num):
    return tweepy.Cursor(api.search, q=keyword).items(num)


def write_tweets_to_file(tweets, filename):
    with open("./tweets/"+ filename, "w", encoding="utf-8") as tweetFile:
        for tweet in tweets:
            tweetFile.write(tweet.text)
    with open("tweets.doclist", 'a', encoding="utf-8") as doc:
        doc.write("./tweets/" + filename)


def count_strong_pos(filename):
    with open("./tweets/"+ filename + "_auto_anns/subjclueslen1polar", "r",  encoding="utf-8") as opinFile:
        text = opinFile.read()
        return text.count("strongpos")


def count_strong_neg(filename):
    with open("./tweets/"+ filename + "_auto_anns/subjclueslen1polar", "r",  encoding="utf-8") as opinFile:
        text = opinFile.read()
        return text.count("strongneg")


def count_weak_neg(filename):
    with open("./tweets/"+ filename + "_auto_anns/subjclueslen1polar", "r",  encoding="utf-8") as opinFile:
        text = opinFile.read()
        return text.count("weakneg")


def count_weak_pos(filename):
    with open("./tweets/"+ filename + "_auto_anns/subjclueslen1polar", "r",  encoding="utf-8") as opinFile:
        text = opinFile.read()
        return text.count("weakpos")


def count_neutral(filename):
    with open("./tweets/"+ filename + "_auto_anns/subjclueslen1polar", "r",  encoding="utf-8") as opinFile:
        text = opinFile.read()
        return text.count("neutral")


def count_all(filename):
    out = {'neutral': count_neutral(filename), 'weak_pos': count_weak_pos(filename),
           'weak_neg': count_weak_neg(filename), 'strong_neg': count_strong_neg(filename),
           'strong_pos': count_strong_pos(filename)}
    return out

def run_opinion_finder(doclist = "tweets.doclist"):
    os.system('cmd /k java -classpath opinionfinderv2.0\\lib\\weka.jar;opinionfinderv2.0\\lib\\stanford-postagger.jar;opinionfinderv2.0\\opinionfinder.jar opin.main.RunOpinionFinder '+ doclist +' -d')


tw = tweepy.Cursor(api.search, q="2020").items(200)
write_tweets_to_file(tw, "testtweets")
run_opinion_finder()
print(count_all('testtweets'))
