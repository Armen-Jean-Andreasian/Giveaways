import json


def save_json(content, file_name: str = 'debugging_result'):
    with open(f'{file_name}.json', 'w', encoding='utf-8') as json_file:
        json.dump(content, json_file, indent=4)


def save_html(content, file_name: str = 'debugging_result'):
    with open(f'{file_name}.html', 'w', encoding='utf-8') as html_file:
        html_file.write(content)
