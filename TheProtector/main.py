from modules.googleNatrualLanguageProcessing import get_sentiment
from modules.twitter_pull import gen_tweets


def main():
    gen_tweets("Univeristy of Tennessee")

    Twitter_post = input("Twitter Post: ")
    sentiment = get_sentiment(Twitter_post)


    print("Score: {} Magnitude {}".format(sentiment.score,sentiment.magnitude))


if __name__ == '__main__':
    main()