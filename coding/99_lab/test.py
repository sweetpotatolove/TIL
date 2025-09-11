import json
import csv

with open('data.json', 'r', encoding='utf-8') as file:
    data_from_json = json.load(file)

fieldnames = ['이름', '나이', '자기소개']

with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    writer.writerows(data_from_json)
