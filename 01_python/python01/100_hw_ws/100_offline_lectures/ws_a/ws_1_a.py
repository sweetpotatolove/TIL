'''
파이썬의 기본 데이터 타입과 변수 할당을 연습하고자 한다. 요구사항을 만족하는 코드를 작성하시오.

name 변수에 'Alice' 문자열을 할당한다.
age 변수에 25 정수를 할당한다.
height 변수에 5.6 부동 소수점을 할당한다.
is_student 변수에 True 불린 값을 할당한다.
각 변수에 담긴 값을 출력한다.
f-string을 활용하여 'Alice는 25살이고, 키는 5.6이며 학생 여부는 True입니다.' 문자열을 출력한다.
단, name, age, height, is_student 변수를 사용하여야 한다.
'''
# 파이썬에서 문자열을 나타내기 위해서 사용하는 방법은
# '' "" 를 사용해서 나타낸다.
# 어떨때 single 어떨때 double quote를 사용하느냐?
# 작성자 마음. -> 저는 따옴표만 씁니다. 왜? shift 누르기 귀찮아서.
    # 대신, 지켜야 할 것. 
    # 하나의 프로젝트 내에서는 되도록 하나로 통일
'''
    여러줄 문자열 나타낼때 사용하는 따옴표 3개 
    func의 설명문에서도 사용할 수 있다.
'''
name = 'Alice'
age = 25
height = 5.6
is_student = True
# 문자열 보간법 (strint interpolation)
# 잊지 말자. 맨날 print 할때만 쓰다보니까, 이것도 문자열 타입이라는 걸 잊는데,,
f_string = f'{name} {age} {height} {is_student}'