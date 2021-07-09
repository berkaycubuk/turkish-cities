import json

with open('output.json') as json_file:
    data = json.load(json_file)
    for i in data['cities']['TEKİRDAĞ']['districts']['SÜLEYMANPAŞA']['neighborhoods']:
        print(i)
