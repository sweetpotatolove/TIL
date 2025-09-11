import sys
sys.stdin = open("input.txt")

# 상하좌우 방향벡터 (상:0, 하:1, 좌:2, 우:3)
direction_x = [0, 0, -1, 1]  # x축 이동량
direction_y = [1, -1, 0, 0]  # y축 이동량


def simulate_atom_collision(atom_count, atom_list):
    """
    원자 소멸 시뮬레이션을 실행하여 총 에너지를 계산

    :param atom_count: 원자의 개수
    :param atom_list: 원자 정보 리스트 [x, y, direction, energy]
    :return: 소멸된 원자들의 총 에너지
    """
    total_energy = 0

    # 0.5초를 1로 하여 4001번 반복 (충분한 시간)
    for time_step in range(4001):
        # 각 시간마다 충돌을 확인하기 위한 위치별 원자 저장
        position_map = {}

        # 모든 원자에 대해 이동 및 충돌 처리
        for atom_index in range(atom_count):
            # 원자가 아직 소멸되지 않았다면
            if atom_list[atom_index][3] != 0:
                # 원자를 방향에 따라 이동
                atom_list[atom_index][0] += direction_x[atom_list[atom_index][2]]
                atom_list[atom_index][1] += direction_y[atom_list[atom_index][2]]

                # 원자가 경계 내에 있는지 확인 (-2000 ~ 2000 범위)
                current_x = atom_list[atom_index][0]
                current_y = atom_list[atom_index][1]

                if abs(current_x) <= 2000 and abs(current_y) <= 2000:
                    current_position = (current_x, current_y)

                    # 해당 위치에 다른 원자가 없다면
                    if current_position not in position_map:
                        position_map[current_position] = atom_index
                    else:
                        # 충돌 발생: 두 원자의 에너지를 합산
                        collided_atom_index = position_map[current_position]
                        total_energy += atom_list[collided_atom_index][3] + atom_list[atom_index][3]

                        # 충돌한 두 원자를 소멸시킴 (에너지를 0으로 설정)
                        atom_list[atom_index][3] = 0
                        atom_list[collided_atom_index][3] = 0

    return total_energy


# 테스트 케이스 처리
test_case_count = int(input())
for test_case in range(1, test_case_count + 1):
    atom_count = int(input())
    atom_list = []

    # 원자 정보 입력 받기
    for i in range(atom_count):
        x, y, direction, energy = map(int, input().split())
        # 좌표를 2배로 확대하여 0.5 단위를 정수로 처리
        atom_list.append([x * 2, y * 2, direction, energy])

    # 시뮬레이션 실행
    result = simulate_atom_collision(atom_count, atom_list)
    print(f"#{test_case} {result}")