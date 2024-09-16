import json


def load(filename):
    file = open(filename)
    data = json.load(file)
    return data
