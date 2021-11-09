
from google.cloud import language_v1
import os
# Set enviroment var to the path of the key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "theprotector-329416-8d3ddc56c477.json"


def get_sentiment(text):
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

    return sentiment


def get_entity_sentiment(text):
    """" """
    return data