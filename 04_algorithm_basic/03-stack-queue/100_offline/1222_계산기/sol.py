import sys
sys.stdin = open('input.txt')

'''
    해당 문제 해결을 위해서는 + 연산에 대한 처리만 하면 되지만,
    후위표기법 연습도 할 겸, +-*/ () 모두를 포함하여 처리한 코드를 작성하였음.
'''

def postfix(expression):
    # 덧셈, 뺄셈은 곱셈, 나눗셈보다 우선순위가 낮음.
    # 닫는 괄호는 연산 처리 기준 가장 우선순위가 낮음. -> 여는 괄호를 만나기 전까지 모든 연산자를 다 뺄 것
    operator_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []
    postfix_expression = ''
    for char in expression:
        if char.isnumeric():        # 피연산자면 후위표현식에 일단 추가
            postfix_expression += char
        elif char == '(':           # 여는 괄호면 연산자 stack에 무조건 삽입
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix_expression += stack.pop()
            stack.pop()
        else:                       # 그 외 연산자의 경우,
            # 스택에 삽입 전, 이미 스택에 있는 값들중, 나보다 우선순위가 높은 값들을 빼서
            # 후위표현식에 추가하고 난뒤, 나를 삽입
            while stack and operator_priority[char] <= operator_priority[stack[-1]]:
                postfix_expression += stack.pop()
            stack.append(char)
    # 모든 처리 후, 남은 stack 비우기
    while stack:
        postfix_expression += stack.pop()
    return postfix_expression

def calc(expression):
    stack = []      # 피연산자 삽입할 stack
    for char in expression:
        if char.isnumeric():    # 정수면 삽입
            stack.append(int(char))
        else:   # 연산자인 경우,
            # 피연산자가 2개 이상이여야 하지만, 지금은 아닌경우는 없으므로 조건 무시
            # if len(stack) >= 2:
            # 피연산자 2개 반환
            y = stack.pop()
            x = stack.pop()
            if char == '+':
                stack.append(x + y)
            elif char == '-':
                stack.append(x - y)
            elif char == '*':
                stack.append(x * y)
            # 나눗셈은 피연산자 순서 중요.
            elif char == '/':
                stack.append(x / y)
    # 연산 종료되었으면 마지막까지 남은 피연산자가
    # 식 실행 결과
    return stack[0]

for tc in range(1, 11):
    N = int(input())
    data = input()
    postfix_expression = postfix(data)
    result = calc(postfix_expression)
    print(f'#{tc} {result}')