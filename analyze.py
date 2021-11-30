from modules.googleNatrualLanguageProcessing import get_entity_sentiment, get_sentiment
import pickle
import sklearn as skl
from sklearn.ensemble import RandomForestRegressor

# get from user
print("enter text: ")

txtIn = input()

# initialize random forest and xg pickles
rf_model = pickle.load(open("random_forest_protector.pkl", 'rb'))
XG_model = pickle.load(open("XGBoost_protector.pkl", 'rb'))

# initialize vectorizers for both
vectorizerRF = pickle.load(open("RF_vectorizer.pkl", 'rb'))
vectorizerXG = pickle.load(open("XGB_vectorizer.pkl", 'rb'))

# user input as txt array for the vectorizer
txtArr = [txtIn]

# find result of both
result_rf = rf_model.predict(vectorizerRF.transform(txtArr))
result_XG = XG_model.predict(vectorizerXG.transform(txtArr))

# print 
print('\n')
print("random forest result: " + str(result_rf))
print('\n')

print("XG Result: " + str(result_XG))
print('\n')

# find google sentiment and print
sentiment = get_sentiment(txtIn)
entsent = get_entity_sentiment(txtIn)
for entity in entsent.entities:
    entSentiment = entity.sentiment
    # Entity[entity.name] = {"score":entSentiment.score,"magnitude":entSentiment.magnitude}
    
print("google sentiment analysis: \n" + str(sentiment))