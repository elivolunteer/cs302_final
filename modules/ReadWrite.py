# This file should parse twitter json file and create new json file containing the id and values.
import json
from genericpath import exists
import os
import  sys

def get_data(filename): # This returns a object of twitter json information 
    with open(filename, 'r') as fp:
        obj = json.load(fp)
    return obj

def get_value_by_id(dataframe, id):
    return dataframe["{}".format(id)]


def store_data(file,_dict):
    file = open(file,mode='w', encoding='utf-8')
    with file as feedsjson:
        # if exists(os.path.join(sys.path[0],file)) == True:
        #     feed = json.load(feedsjson)
        #     json.dump(_dict,feed)
        # else:
        json.dump(_dict,feedsjson,indent=4)
            