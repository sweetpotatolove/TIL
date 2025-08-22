import csv

# with open('data.csv', 'w', newline='', encoding='utf-8') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['이름', '나이', '직업'])
#     csv_writer.writerow(['홍길동', '30', '개발자'])
#     csv_writer.writerow(['김철수', '25', '디자이너'])
#     csv_writer.writerow(['이영희', '28', '기획자'])

with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['이름', '나이', '직업']
    csv_writer = csv.DictWriter(file, fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'이름': '홍길동', '나이': '30', '직업': '개발자'})
    csv_writer.writerow({'이름': '김철수', '나이': '25', '직업': '디자이너'})
    csv_writer.writerow({'이름': '이영희', '나이': '28', '직업': '기획자'})
    