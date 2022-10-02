# https://www.acmicpc.net/problem/7579
# 앱

# MAX_MEMORY가 천만, MAX_N이 100이므로 반복횟수가 10억이 되어 시간초과 에상됨

from copy import deepcopy

MAX_N = 100
MAX_M = 10000000
MAX_MEMORY = 10000000
MAX_COST = 100
N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

# DP[i]는 i 만큼의 메모리를 추가 확보하기 위해 필요한 최소한의 비용을 의미한다.
DP = [MAX_COST * MAX_N for _ in range(MAX_MEMORY+1)]  # 최대 비용으로 초기화
DP[0] = 0
# 메모리 절약을 위해 2차원배열 대신 배열 2개를 번갈아가면서 씀
DP2 = deepcopy(DP)

# 앱이 0 ~ N-1 까지 있을 때, 0부터 N-1까지 순회하며 DP를 갱신해 나감
max_memory = 0  # i번째 메모리까지 반환받았을 때 확보 가능한 최대 메모리
for i in range(N):
    max_memory += memory[i]
    print(DP2[:max_memory+1])
    for j in range(1, max_memory+1):
        if j - memory[i] >= 0:
            # 이전 값 참조해서 DP[j]값 갱신
            DP2[j] = min(DP[j - memory[i]] + cost[i], DP[j])
        else:
            # 참조할 이전값이 없으면, DP[j]와 cost[i]값 비교
            DP2[j] = min(DP[j], cost[i])
    tmp = DP  # 임시보관
    DP = DP2  # shallow copy
    DP2 = tmp  # shallow copy(새로 생성하는것보다 이미 생성된 메모리 사용)

print(DP[:M+1])
print(DP[M])