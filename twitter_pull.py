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
    start_date = datetime.date(2020, 8, 10)
    end_date = datetime.date(2021, 8, 10)
    delta = datetime.timedelta(days=30)
    tweets_dict = {}

    while start_date <= end_date:
        #data collection
        response = api.search_full_archive(label="dataGen", query=query, fromDate=start_date.strftime('%Y%m%d0000'), toDate=(start_date+delta).strftime('%Y%m%d0000'), maxResults=100)
        for source in response:
            if source.ang == "en":
                tweets_dict[source._json['id_str']] = source._json['text']
        start_date += delta

    #data dump
    with open('data/tweets.json', 'r+') as f:
        json.dump(tweets_dict, f, indent=4)

    return 0
