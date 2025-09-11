# import sys
# sys.stdin = open('input.txt')

TC = int(input())
for test_case in range(1, TC + 1):
    str_input = input().replace('()', 'l')  # 레이저는 l로 바꿈

    stack = []
    result = 0

    for i in range(len(str_input)):
        if str_input[i] == '(':  # 열린 괄호
            stack.append('(')    # 막대기 스택에 넣기
        elif str_input[i] == 'l':  # 레이저
            result += len(stack)  # 겹친 막대기 수만큼 잘림
        else:  # 닫는 괄호
            stack.pop()
            result += 1  # 막대기 하나 사라지면서 잘린 조각 추가

    print(f'#{test_case} {result}')
