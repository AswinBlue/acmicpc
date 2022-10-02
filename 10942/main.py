# https://www.acmicpc.net/problem/10942
# 팰린드롬?

from sys import stdin, stdout

MAX_N = 2000
MAX_M = 1000000

# 두 배열이 대칭 형태인지 확인하는 함수
def compare(A, B):
    B.reverse()
    if A == B:
        return 1
    return 0


N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
nums.insert(0, 0)
M = int(stdin.readline())

# DP[i][j]는 i부터 j까지가 팰린드롬이면 1, 아니면 0을 반환
DP = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    DP[i][i] = 1  # 길이가 1이면 무조건 팰린드롬

# i ~ j 까지가 팰린드롬일 때, i-1 번째 숫자와 j+1 번째 숫자가 같다면 i-1 ~ j+1도 팰린드롬
# 길이가 2일 떄 부터 N일 떄 까지 늘려가며 찾아간다.
# 길이가 2일때
for left in range(1, N):
    if nums[left] == nums[left+1]:
        DP[left][left+1] = 1
# 길이가 3 이상일때
for width in range(3, N+1):
    # 시작점을 옮겨가며 확인
    for left in range(1, N+1):
        # 길이와 시작점으로 종료지점 설정
        right = left + width - 1
        # 범위를 초과하면 skip
        if right > N:
            break
        # left+1 ~ right-1 이 팰린드롬이고, 그 좌우에 인접한 값이 동일할 때
        # 길이가 3 이상일때 부터 사용 가능
        if DP[left+1][right-1] == 1 and nums[left] == nums[right]:
            DP[left][right] = 1
# print(DP)
for m in range(M):
    s, e = map(int, stdin.readline().split())
    stdout.write('{}\n'.format(DP[s][e]))