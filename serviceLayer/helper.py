import json
import os
import ijson
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import matplotlib.pyplot as plt


dataf = []

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
    DIRECTORY = os.path.dirname(os.path.abspath(__file__))+'/data/'

    with open(DIRECTORY + "yelp_business.json") as f:

        for line in f:
            j_content = json.loads(line)
            dataf.append(j_content)
            print(j_content)
    df = pd.DataFrame.from_dict(json_normalize(dataf), orient = 'columns')
    print(list(df.columns.values))
    print(df["name"].value_counts())

    def parse_float(x):
        try:
            x = float(x)
        except Exception:
            x = 0
        return x

    df["longitude"] = df["longitude"].apply(parse_float)
    df["latitude"] = df["latitude"].apply(parse_float)

    print(df["longitude"].values)

    plt.hist(df["name"],bins = 100)


read_djson()

