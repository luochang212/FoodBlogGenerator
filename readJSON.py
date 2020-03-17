import json


def read_json():
    filename = "data.json"
    with open(filename, mode='r', encoding="utf-8") as curFile:
        return json.loads(curFile.read())
