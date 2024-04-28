import json


def save_json(content):
    with open('debugging_result.json', 'w') as json_file:
        json.dump(content, json_file, indent=4)
