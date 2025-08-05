import sys
sys.stdin = open('input.txt')

# 암호 패턴 사전
# 0111011
code_dict = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}

DECODE_FAIL = -1


# 암호 해독 함수
def decode(code):
    decoded = ''
    for i in range(0, len(code), 7):
        # 리스트를 문자열로 변환
        chunk = ''.join(map(str, code[i:i + 7]))
        # 딕셔너리에 키가 없으면 FAIL값 리턴
        if chunk not in code_dict: return DECODE_FAIL

        # 있으면 복호화된 숫자 추가
        decoded += code_dict[chunk]

    return decoded


# 유효성 검사 함수
def is_valid(code):
    # 파이썬에서 슬라이싱은 범위를 벗어나도 IndexError가발생하지 않는다.
    # 그런 상황을 대비하기 위해서, 56글자가 아니면 그냥 0 반환하겠다.
    if len(code) != 56: return 0

    # 복호화 함수 호출
    decoded = decode(code)
    # 복호화 실패
    if decoded == DECODE_FAIL: return 0

    odd_sum = sum(int(decoded[i]) for i in range(0, 8, 2))  # 홀수 자리
    even_sum = sum(int(decoded[i]) for i in range(1, 8, 2))  # 짝수 자리

    total = odd_sum * 3 + even_sum

    if total % 10 == 0:
        return odd_sum + even_sum
    else:
        return 0


# 입력 처리
T = int(input())  # 테스트 케이스 수, 단일 테스트인 경우 무시 가능
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # 2차원 배열 입력
    encoded = [list(map(int, input().strip())) for _ in range(N)]

    # 유효한 암호 코드 추출
    target_code = []
    for line in encoded:
        if 1 in line:
            # 뒤에서 부터 1 찾아서 56개 슬라이싱
            last_idx = ''.join(map(str, line)).rfind('1')
            target_code = line[last_idx - 55: last_idx + 1]
            break
    print(target_code)

    # 결과 출력
    print(f'#{test_case} {is_valid(target_code)}')
