# 학생들의 이름과 점수를 딕셔너리에 저장
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88,
    "Eve": 95
}
# students 변수에 할당된 데이터 타입이 어떤 타입인지 출력
print(type(students))
print(f'학생들의 이름과 점수 : {students}')

# 모든 학생의 평균 점수
# 모든 value의 합 / 전체 학생 수
avg_score = sum(students.values()) / len(students)
print(f'모든 학생들의 평균 점수 {avg_score:.5f}')

score = 80
top_students = [key for key, value in students.items() if value >= score]
print(top_students)

# sorted함수의 첫번째 인자 : 반복 가능한객체
# students dict가 가지고 있는 키와 value
print(sorted(students.items(), key=lambda item: item[1], reverse=True ))

# 학생의 점수를 가지고 비교, studetns dict 점수 ->  value()
max_value = max(students.values())
min_value = min(students.values())
print(f'점수 차 : {max_value - min_value}')

# 각 학생의 점수가 평균 점수보다 높은지 낮은지를 판단하여, 낮은 학생의 이름과 성적을 함께 출력하시오.
for key in students:
    if students[key] > avg_score:
        status = '이상'
    else:
        status = '이하'
    print(f'{key}인 학생의 점수 {students[key]}값은 평균 {status}이다.')
