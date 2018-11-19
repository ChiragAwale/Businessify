import json
import os
import ijson
import pandas as pd



def read_json(json_data):
    loaded_json= json.loads(json_data)
    print(loaded_json)


def read_json_from_file(file_name):
    DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    #print(DIRECTORY)
    with open(DIRECTORY+'/data/'+file_name+'.json') as f:
        data = json.load(f)
        return data

def read_djson():

    dataf = []
    DIRECTORY = os.path.dirname(os.path.abspath(__file__))+'/data/'

    with open(DIRECTORY + "yelp_business.json") as f:

        for line in f:
            j_content = json.loads(line)
            dataf.append(j_content)

    df = pd.DataFrame.from_dict(dataf, orient = 'columns')
    print(df["state"].value_counts())


read_djson()