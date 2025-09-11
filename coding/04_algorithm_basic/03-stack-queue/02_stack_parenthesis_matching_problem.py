def check_match(expression):
    # 여는 괄호들을 일단 담아둘 스택
    # 여는 괄호들을 담아두다가 올바른 닫는 괄호가 나왔는지 확인하기 위함
    stack = []

    # 괄호의 짝을 매칭시킬 수 있어야 할 것 같다
    # 문자열도 시퀀스 타입이므로 리스트 아니어도 괜츈
    opening_bracket = '({['
    closing_bracket = ')]}'
    matching_dict = { ')':'(',
                      '}':'{',
                      ']':'['}

    for char in expression:
        if char in matching_dict.values():  # 여는 괄호인지 물어보기
            # 여는 괄호라면 스택에 넣어랏
            stack.append(char)
        elif char in matching_dict.keys():  # 닫는 괄호인지 물어보기
            # 닫는 괄호라면?
            # 스택에서 나와 매칭되는 짝을 찾을 수 있다면, 그 괄호를 제거
            # 단, 스택이 비어있지 않아야 함!
                # 스택이 비었거나, 마지막 요소 값이 내가 찾는 여는 괄호가 아니면 실패
            if not stack or stack[-1] != matching_dict[char]:
                return False

            # 매칭 짝을 찾았으면 제거
            stack.pop()
    # 모든 문자를 다 순회했을 때, 스택이 비어있지 않다면 문제가 있는 것
    return not stack


# 예시
examples = ["(a(b)", "a(b)c)", "a{b(c[d]e}f)"]
for ex in examples:
    if check_match(ex): 
        print(f"{ex} 는 올바른 괄호") 
    else:
        print(f"{ex} 는 올바르지 않은 괄호")  
