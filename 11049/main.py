# https://www.acmicpc.net/problem/11049
# 행렬 곱셈 순서
from sys import stdin, stdout

MAX_N = 500
MAX_R = 500
MAX_NUM = 2**31

N = int(stdin.readline())
matrix = []
for n in range(N):
    r, c = map(int, stdin.readline().split())
    matrix.append((r,c))

# DP[i][j] 는 i부터 j까지 행렬을 합칠때 최소비용
DP = [[MAX_NUM for _ in range(N)] for _ in range(N)]
for i in range(N):
    DP[i][i] = 0


# 길이 width 에 대해
for width in range(2, N+1):
    # DP[i][j]를 계산
    for i in range(N):
        j = i+width-1
        # 계산 불가능한 경우 생략
        if j >= N:
            break
        # 좌측과 우측을 나눠서 확인. 모든 길이에 대해 확인. 좌측과 우측이 모두 존재해야 하므로 1 ~ width-1 까지 범위로 계산
        for w in range(1, width):
            # 좌측의 길이가 w인 경우. 좌측은 [i:mid], 우측은 [mid:j+1]
            mid = i + w  # 우측 시작점
            DP[i][j] = min(DP[i][j], DP[i][mid-1] + DP[mid][j] + matrix[i][0] * matrix[mid-1][1] * matrix[j][1])
# print(DP)
# print(matrix)

stdout.write('{}\n'.format(DP[0][N-1]))