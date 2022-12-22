# https://www.acmicpc.net/problem/2836
# 수상 택시

# 직선 위에서 왼쪽 혹은 오른쪽으로 이동하는 경로들을 받고, 이동 거리를 최소로 하며 모든 경로를 운행하는 방법을 찾아야 한다.
# 방향이 같은 경로들은 겹치는 부분을 제거할 수 있다.
# 시작점에서 최종 목적지로 가는 방향을 순방향으로 할 때, 모든 순방향 경로들을 취합한 값에서 (모든 역방향 경로들을 취합한 값) * 2을 뺀 것이 최종 이동 경로이다.
from collections import deque

START = 0
MAX_N = 300000
MAX_M = 1000000000

N, M = map(int, input().split())
reverse_path = deque()  # 역방향 경로를 담기위한 배열
for i in range(N):
    a, b = map(int, input().split())
    if a > b:
        reverse_path.append((b,a))  # timeout 방지를 위해 deque 사용

reverse_path = sorted(reverse_path)  # 시작점 a 에 대해 오름차순으로 정렬
_a, _b = 0, 0  # 이전 값을 저장하기 위한 변수
length = 0  # 역방향 경로 길이를 저장하기 위한 변수
for a, b in reverse_path:
    # case 1: 일부 포함
    if _a <= a <= _b <= b:
        _b = b  # b 확장
    # case 2: 완전 포함
    elif _a <= a <= b <= _b:
        continue
    # case 2: 완전 포함(역)
    elif _a == a <= _b <= b:
        _b = b  # b 확장
    # case 4: 겹치지 않음
    else:
        length += _b - _a  # 길이에 추가
        _a = a  # _a 갱신
        _b = b  # _b 갱신
# 마지막 경로 적용
length += _b - _a

# 총 이동거리 출력
print(M + length * 2)