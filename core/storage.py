import json

def saveToJson(filename, data):
    with open(filename, 'a') as f:
        for item in data:
            f.write(json.dumps(item.model_dump()) + '\n')