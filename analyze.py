from modules.googleNatrualLanguageProcessing import get_entity_sentiment, get_sentiment
import pickle
import sklearn as skl
from sklearn.ensemble import RandomForestRegressor

print("enter text: ")

txtIn = input()

# random forest result
rf_model = pickle.load(open("random_forest_protector.pkl", 'rb'))
vectorizer = pickle.load(open("vectorizer.pkl", 'rb'))
txtArr = [txtIn]
result = rf_model.predict(vectorizer.transform(txtArr))
print("random forest result: " + result)

# # google sentiment 
# sentiment = get_sentiment(txtIn)
# entsent = get_entity_sentiment(txtIn)
# for entity in entsent.entities:
#     entSentiment = entity.sentiment
#     # Entity[entity.name] = {"score":entSentiment.score,"magnitude":entSentiment.magnitude}
    
# print("google sentiment analysis: " + sentiment)