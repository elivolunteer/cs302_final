
from google.cloud import language_v1
import os
# Set enviroment var to the path of the key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "modules\\theprotector-329416-d6760fe0283a.json"


def get_sentiment(text):
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

    return sentiment

