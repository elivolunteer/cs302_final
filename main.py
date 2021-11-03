from modules.googleNatrualLanguageProcessing import get_sentiment
# from modules.twitter_pull import gen_tweets
import modules.ReadWrite as rw

def main():
    # gen_tweets("Univeristy of Tennessee")

    twitter_data = rw.get_data("data/tweets.json")
    ids = {}
    data = {}

    for id in twitter_data:
        print(id)
        sentiment = get_sentiment(rw.get_value_by_id(twitter_data,id))
        # print("Score: {} Magnitude {}".format(sentiment.score,sentiment.magnitude))
        ids = {"score":sentiment.score,"magnitude":sentiment.magnitude}
        data[id] =  ids
    rw.store_data("data/sentiment_data.json",data)



if __name__ == '__main__':
    main()