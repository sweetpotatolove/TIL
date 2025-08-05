import sys
# open input text file
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(T):
    K, N, M = map(int, input().split())
    stop_list = list(map(int, input().split()))

    charge_count = 0
    relative_location = []

    for station in stop_list:
        relative_location.append(K - station)
    print(relative_location)

    def how_many_stops(charge_count, relative_location):
        continued = []

        if len(relative_location) == 0:
            print(f"#{test_case+1} {charge_count}")
        elif relative_location[0] < 0:
            print(f"#{test_case+1} 0")
        elif len(relative_location) == 1:
            if relative_location[0] >= N - stop_list[-1]:
                print(f"#{test_case+1} {charge_count}")
            elif relative_location[0] < N - stop_list[-1]:
                    if N - stop_list[-1] <= K:
                        charge_count += 1
                        print(f"#{test_case+1} {charge_count}")
                    else:
                        print(f"#{test_case+1} 0")

            else:
                print(f"#{test_case+1} 0")
        else:
            for loc in relative_location:
                if loc >= 0:
                    continued.append(loc)
                else:
                    charge_count += 1
                    break

            relative_location[:] = relative_location[len(continued):]
            if len(relative_location) == 0:
                charge_count += 1

            for i in range(len(relative_location)):
                relative_location[i] += K - continued[-1]

            how_many_stops(charge_count, relative_location)

    how_many_stops(charge_count, relative_location)