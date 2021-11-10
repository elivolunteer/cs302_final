
from google.cloud import language_v1
import os
# Set enviroment var to the path of the key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "modules/theprotector-329416-8d3ddc56c477.json"


def get_sentiment(text):
    try: 
        client = language_v1.LanguageServiceClient()
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
        return sentiment

    except:
        print(f"Tweet failed: {text}")
        return {"score":0.0,"magnitude":0.0}


def get_entity_sentiment(text):
    try:
        client = language_v1.LanguageServiceClient() #
        # following block added by Kyle
        # attempting entity sentiment analysis
        type_ = language_v1.Document.Type.PLAIN_TEXT
        language = "en"
        document = {"content": text, "type_": type_, "language": language}
        encoding_type = language_v1.EncodingType.UTF8
        response = client.analyze_entity_sentiment(request = {'document': document, 'encoding_type': encoding_type})
        # Loop through entitites returned from the API
        # for entity in response.entities:
        #     print(u"Representative name for the entity: {}".format(entity.name))
        #     entSentiment = entity.sentiment
        #     print(u"Entity sentiment score: {}".format(entSentiment.score))
        #     print(u"Entity sentiment magnitude: {}".format(entSentiment.magnitude))
        return response
    except:
        print(f"Entity failed: {text}")
        return {}