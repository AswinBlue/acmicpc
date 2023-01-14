# https://www.acmicpc.net/problem/3015
# 오아시스 재결합

# 키가 같은 사람의 경우 '조합'을 사용하여 계산하여야 한다. 1차원 원소 stack으로는 계산이 어렵다. 
# -> 오답
from sys import stdin
from bisect import bisect

DEBUG = 0

def Print(*args):
    if DEBUG:
        print(*args)

MAX_N = 500000
MAX_NUM = 2**31

idx = 0

N = int(stdin.readline())  # 내림차순으로 bisect를 사용하기 위해 음수로 치환
stack = [(MAX_NUM * -1 -1) for _ in range(N + 1)]  # 문제 해결을 위한 stack. 초기값으로 최소값을 하나 가지고 시작한다.
result = 0  # 결과 (서로 볼 수 있는 쌍의 수)

# 입력이 내림차순이라면 stack에 집어넣는다. 
# 내림차순을 깨는 입력을 받게되면 lower bound를 찾아 idx를 수정한다. 수정하면서 버리게 되는 구간에 대해 result 를 갱신한다.
for _ in range(N):
    current = int(stdin.readline()) * -1
    Print('current:', current)
    if current >= stack[idx]:  # 음수로 변경하여 저장했기 때문에 내림차순 조건은 등호가 반대가 된다. 
        idx += 1
        stack[idx] = current
    else:
        new_idx = bisect(stack, current, lo=1, hi=idx)
        # bisect를 사용하면 동일한 수가 나온 경우 우측 index를 반환한다. 문제의 조건에서 동일한 수 끼리도 쌍을 만들 수 있기 때문에 bisect를 사용했다.
        # 만약 A B 사이에 A 혹은 B와 같은 키의 사람 C가 끼면 A와 B가 서로 볼 수 없다면 biesct_left를 사용하면 된다.
        Print('idx / new_idx:', idx, '/', new_idx)

        # new_idx ~ idx 까지의 수들은 stack에서 제거해야 내림차순이 유지된다.
        # 결과값(result)에 값을 추가시켜주며 해당 구간 값들을 stack에서 제거한다.
        result += (idx - new_idx) + (idx - new_idx + 1)  # (new_idx:idx) 구간에서 나올 수 있는 쌍의 개수 + (new_idx:idx) 구간에서 새로 들어온 인자와 합해 나올 수 있는 쌍의 개수
        if idx > 1:
            result += 1  # new_idx 인자와 new_idx - 1 인자 쌍

        # stack이 내림차순을 유지할 수 있는 위치(new_idx)에 입력받은 값을 집어넣고 idx값을 갱신한다.
        idx = new_idx
        stack[idx] = current

    Print(result, stack)

# for문을 모두 돌고 남은 항목들에 대해 결과 계산을 한다.
result += idx - 1

print(result)