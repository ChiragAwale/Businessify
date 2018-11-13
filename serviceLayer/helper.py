import json


def read_json(json_data):
    loaded_json= json.loads(json_data)
    print(loaded_json)


def read_json_from_file():
    with open('response.json') as f:
        data = json.load(f)
        return data