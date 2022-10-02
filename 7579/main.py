# https://www.acmicpc.net/problem/7579
# 앱
from copy import deepcopy

MAX_N = 100
MAX_M = 10000000
MAX_MEMORY = 10000000
MAX_COST = 100
N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

# DP[i]는 i 비용으로 얻을 수 있는 최대 메모리를 뜻한다.
DP = [0 for _ in range(MAX_COST * MAX_N + 1)]
# 리소스 절약을 위해 2차원배열 대신 배열 2개를 번갈아가면서 씀
DP2 = deepcopy(DP)

# 앱이 0 ~ N-1 까지 있을 때, 0부터 N-1까지 순회하며 DP를 갱신해 나감
max_cost = sum(cost)  # N-1번째 앱까지 고려했을 때 사용 가능한 최대 비용
for i in range(N):
    for j in range(max_cost+1):
        if j - cost[i] >= 0:
            # 이전 값 참조해서 DP[j]값 갱신
            DP2[j] = max(DP[j - cost[i]] + memory[i], DP[j])
    DP = deepcopy(DP2)

# print(DP[:max_cost+1])
# 전체 리스트를 순회하며 최초로 M 이상이 되는 cost(index)을 찾는다.
for i in range(max_cost+1):
    if DP[i] >= M:
        print(i)
        break