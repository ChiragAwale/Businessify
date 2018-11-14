import json
import os

def read_json(json_data):
    loaded_json= json.loads(json_data)
    print(loaded_json)


def read_json_from_file():
    DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    #print(DIRECTORY)
    with open(DIRECTORY+'/response.json') as f:
        data = json.load(f)
        return data