import datetime
import json
import pprint
import tweepy
import twitter_config #ask eli for api keys

def gen_tweets(query):
    #set up twitter
    auth = tweepy.OAuthHandler(twitter_config.API_KEY, twitter_config.SECRET_KEY)
    auth.set_access_token(twitter_config.ACCESS_TOKEN, twitter_config.ACCESS_SECRET)
    api = tweepy.API(auth)

    #loop back in time and open and append to data files
    start_time = 20200000000
    end_time = 202012010000
    tweets_dict = {}

    for i in range(start_time, end_time, 3000000):
        #data collection
        response = api.search_full_archive(label="dataGen", query=query, fromDate=i, toDate=i+3000000, maxResults=100)
        for source in response:
            tweets_dict[source._json['id_str']] = source._json['text']

    #data dump
    with open('data/tweets.json', 'r+') as f:
        json.dump(tweets_dict, f, indent=4)

    return 0
