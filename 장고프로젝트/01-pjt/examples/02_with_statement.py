# import sys
# print(sys.getdefaultencoding())

# open함수를 사용하는 방법은 open(filename, mode, encoding)
# data = open('example.txt', 'r', encoding='utf-8')
# data = open('example.txt', 'r')
# print(data)
# print(data.read())
# data.close()
# print(data.read())
'''
with 표현식 as 변수: # alias (별칭) 표현식의 결과값을 변수에 할당
    코드 블럭
with문 종료 시, 리소스 해제
'''

with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
print(file.read())