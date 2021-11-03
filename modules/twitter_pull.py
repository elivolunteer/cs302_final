import json
import pprint
import tweepy
import twitter_config #ask eli for api keys

def gen_tweets(query):
    #set up twitter
    auth = tweepy.OAuthHandler(twitter_config.API_KEY, twitter_config.SECRET_KEY)
    auth.set_access_token(twitter_config.ACCESS_TOKEN, twitter_config.ACCESS_SECRET)
    api = tweepy.API(auth)

    #data collection
    response = api.search_30_day(label="research", query=query)
    tweets_dict = {}
    for source in response:
        tweets_dict[source._json['id_str']] = source._json['text']

    #data dump
    with open('../data/tweets.json', 'w') as f:
        json.dump(tweets_dict, f, indent=4)

    return 0
