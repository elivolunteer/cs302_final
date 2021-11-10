from modules.googleNatrualLanguageProcessing import get_entity_sentiment, get_sentiment
# from modules.twitter_pull import gen_tweets
import modules.ReadWrite as rw
# from twitter_pull import gen_tweets


def main():
    #gen_tweets("CS students")

    twitter_data = rw.get_data("data/tweets.json")
    Entity = {}
    id_data = {}
    data = {}

    

    for id in twitter_data:
        print(id)
        sentiment = get_sentiment(rw.get_value_by_id(twitter_data,id))
        entsent = get_entity_sentiment(rw.get_value_by_id(twitter_data,id))
        for entity in entsent.entities:
            entSentiment = entity.sentiment
            Entity[entity.name] = {"score":entSentiment.score,"magnitude":entSentiment.magnitude}
        # print("Score: {} Magnitude {}".format(sentiment.score,sentiment.magnitude))
        id_data = {"Score":sentiment.score,"Magnitude":sentiment.magnitude,"Entity":Entity}
        data[id] = id_data
        

    rw.store_data("data/sentiment_data.json",data)



if __name__ == '__main__':
    main()