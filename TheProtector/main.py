from modules.googleNatrualLanguageProcessing import  get_sentiment

Twitter_post = input("Twitter Post: ")
sentiment = get_sentiment(Twitter_post)


print("Score: {} Magnitude {}".format(sentiment.score,sentiment.magnitude))
