# https://www.acmicpc.net/problem/3015
# 오아시스 재결합

# 1. 내림차순으로 stack에 입력을 받아가며 내림차순을 깨는 입력이 들어올 경우, lower bound를 찾아 다시 집어넣는다. 
# 2. 이때, 버려지는 인자들에 대해 결과값을 계산한다. 새로 들어온 인자(top) 와 모두 조합이 되고, 서로 앞뒤로 조합이 됨에 주의한다.
# ex) 5 4 2 1 (3) => 2,3 / 1,3 / 2,1 조합 가능
# 3. 키가 같은 사람이 연속해서 여러명 동시에 오게되는 경우, 그들은 서로를 볼 수 있다. 이를 저장해야 문제를 풀 수 있기 때문에 pair 형태로 stack에 저장한다.
# ex) 5 4 2 1 3 3 (3) => 3 3 3 사람들은 서로 볼 수 있으므로 (3 * 2 / 2) 의 조합 가능

from sys import stdin

DEBUG = 0

def Print(*args):
    if DEBUG:
        print(*args)

MAX_N = 500000
MAX_NUM = 2**31


N = int(stdin.readline())

stack = [(MAX_NUM+1, 0) for _ in range(N + 1)]  # 문제 해결을 위한 stack. append의 overhead 줄이기위해 N만큼 초기화
idx = -1
result = 0  # 결과 (서로 볼 수 있는 쌍의 수)
# stack 안의 내용이 내림차순이 유지된다면 current를 stack에 집어넣는다. 
# 내림차순을 깨는 입력을 받게되면 stack이 내림차순이 될 수 있도록 입력에 대해 lower bound를 찾아 idx를 수정하고, 수정하면서 버리게 되는 구간에 대해 result 를 갱신한다.
for i in range(N):
    current = int(stdin.readline())
    Print('current:', current)
    # (만약 A B 사이에 A 혹은 B와 같은 키의 사람 C가 끼면 A와 B가 서로 볼 수 없다면 biesct_left를 사용하면 된다.)

    # lower bound를 찾을 때 까지 new_idx를 옮겨가며 result 갱신
    new_idx = idx
    while new_idx >= 0 and stack[new_idx][0] < current:
        # 'stack에 있는 항목들 중 current보다 작은 항목들이 current와 쌍을 이룰 수 있는 개수' 를 결과에 추가
        result += stack[new_idx][1]
        new_idx -= 1
    Print('new_idx:', new_idx, stack[new_idx], ', result:', result)

    # stack이 내림차순을 유지할 수 있는 위치(new_idx)에 입력받은 값을 집어넣고 idx값을 갱신한다.
    # 단, stack[new_idx] 값이 current와 같은지 체크가 필요하다.
    if new_idx < 0:
        # stack이 비었을 경우, 결과값 갱신없이 추가
        idx = new_idx + 1
        stack[idx] = (current, 1)
    elif stack[new_idx][0] == current:
        # 키가 같은 사람들 끼리 조합 가능 개수 추가
        result += stack[new_idx][1]
        # 이웃한 이전 사람과 조합 가능 개수 추가
        if new_idx-1 >= 0:
            result += 1

        stack[new_idx] = (current, stack[new_idx][1] + 1)
        idx = new_idx
    else:
        # 오름차순이 유지되었기 때문에 바로 앞의 사람과 쌍을 이룰 수 있음
        result += 1

        idx = new_idx + 1
        stack[idx] = (current, 1)

    Print('result:', result, '\n')

print(result)


# 주의할 test case:
# [3 3 2 2 3 3 2 2 3 3]
# [1]
# [1 1 1 1 1]