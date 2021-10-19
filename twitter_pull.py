import tweepy
import twitter_config



def main():
    #set up twitter
    auth = tweepy.OAuthHandler(twitter_config.API_KEY, twitter_config.SECRET_KEY)
    auth.set_access_token(twitter_config.ACCESS_TOKEN, twitter_config.ACCESS_SECRET)
    api = tweepy.API(auth)

    return 0

if __name__ == "__main__":
    main()