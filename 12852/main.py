# https://www.acmicpc.net/problem/12852
# 1로 만들기 2

MAX_N = 1000000

N = int(input())

DP = [N for _ in range(N+1)]  # DP[i]는 i까지 도달하는데 취해야 할 연산의 횟수
parent = [0 for _ in range(N+1)]  # parent[i]는 i값을 1로 만들기 위해 다음번에 선택해야 할 연산을 수행한 결과값
# N이 최대값이므로, 최대값으로 초기화
DP[1] = 0  # 목표값
parent[1] = 0  # 초기화

# 이후 값들은 Dynamic programming으로 계산
for i in range(2, N+1):
    # 가능한 최소값을 찾아야 한다.

    # 1을 더하여 도달하는 경우
    min_val = DP[i-1] + 1
    p = i-1  # parent값
    # 2로 나누어 떨어 진다면
    if i % 2 == 0 and DP[i//2]+1 < min_val:
        min_val = DP[i//2] + 1
        p = i//2
    # 3으로 나누어 떨어 진다면
    if i % 3 == 0 and DP[i//3]+1 < min_val:
        min_val = DP[i//3] + 1
        p = i//3

    DP[i] = min_val
    parent[i] = p

# print(DP, parent)
print(DP[N])
ptr = N
result = ''
while ptr > 0:
    result += str(ptr) + ' '
    ptr = parent[ptr]

print(result)