obj = map(int, '123')
print(obj) # <map object at 0x000002D870709D80>
print(type(obj)) # <class 'map'> -> map 객체다.
print(type('123')) # <class 'str'> -> str 객체다.
# map obj 자체를 사용하는데는 문제가 없다.
# for item in obj:
#     print(type(item)) # <class 'int'>
#     print(item) # 1 2 3

# 이러한 경우에 보통 list로 형 변환한 후 사용한다. -> 명시적 형변환
my_list = list(obj)
print(my_list) # [1, 2, 3]

def func(num):
    return num ** 2

obj2 = list(map(func, [1, 2, 3])) # [1, 4, 9]
print(obj2)

# 함수를 재사용할 일이 없다면 lambda 를 사용해서 익명 함수로 만들 수도 있다.
obj3 = list(map(lambda x: x ** 2, [1, 2, 3])) # [1, 4, 9]
print(obj3)

user_input = '1 2 3 4 5'
arr = list(map(int, user_input.split(' ')))
for item in arr:
    print(item * 2)