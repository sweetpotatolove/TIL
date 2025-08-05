import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    laser = list(
        input())  # ['(', ')', '(', '(', '(', '(', ')', '(', ')', ')', '(', '(', ')', ')', '(', ')', ')', ')', '(', '(', ')', ')']
    stack = []
    count = 0  # 막대 개수 계산할 카운트

    for i, bk in enumerate(laser):
        if bk == '(':
            stack.append(bk)  # 일단 여는 괄호를 스택에 담아.
            if laser[i + 1] != ')':  # 이게 막대면, 막대 개수를 하나 더해줌
                count += 1

        else:
            if stack[-1] == '(':  # 여는괄호와 닫는 괄호가 붙게 된다면 > 레이저 또는 막대 > 걍 빼
                stack.pop()
            if laser[i - 1] == '(':  # 레이저 인지 판단
                count += len(stack)  # 그리고 스택에 있는 막대 개수를 더해줌

    print(f"#{test_case}", count)