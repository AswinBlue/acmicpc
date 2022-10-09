# https://www.acmicpc.net/problem/1725
# 히스토그램
# 메모리 초과로 실패

from sys import stdin, stdout

MAX_SIZE = 2000000000
MAX_N = 100000
MAX_HEIGHT = 1000000000

N = int(stdin.readline())

# DP[i][j]는 i~j까지 다이어그램에서 만들 수 있는 최대 넓이와 그 구간의 최소 높이를 저장
DP = [[None for _ in range(N)] for _ in range(N)]
for i in range(N):
    height = int(stdin.readline())
    DP[i][i] = (height, height)  # 넓이 , 높이

# 길이를 2부터 늘려가며 확인
for length in range(2, N+1):
    for left in range(N):
        right = left + length - 1
        # 범위가 배열을 벗어나면 그만
        if right >= N:
            break
        # [left:right+1] 구간을 형성하는 경우는,
        # [left+1:right+1] 구간에 left번째를 더한것, [left:right] 구간에 right번째를 더한 것 두가지 경우가 있음

        # 최소 높이 확인
        min_height = min(DP[left+1][right][1], DP[left][left][1], DP[left][right-1][1], DP[right][right][1])
        # 이전 구간 결과와 현재 구간에서 나올 수 있는 넓이 비교해서 최대값을 취함
        max_width = max(DP[left+1][right][0], DP[left][right-1][0], length * min_height)
        DP[left][right] = (max_width, min_height)

stdout.write(str(DP[0][N-1][0]))