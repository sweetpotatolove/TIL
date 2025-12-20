import csv

# with open('users.csv', 'r', encoding='utf-8') as file:
#     # content = file.read()
#     # print(content)
#     csv_reader = csv.reader(file)
#     # print(csv_reader)
#     for row in csv_reader:
#         print(row)

with open('users.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    print(csv_reader.fieldnames)
    for row in csv_reader:
        print(row)

    