# https://www.acmicpc.net/problem/14003
# 가장 긴 증가하는 부분수열 5

MAX_N = 1000000
MAX_NUM = 1000000000

MIN_NUM = -1000000000

from bisect import bisect_left
from collections import deque
from sys import stdin, stdout

N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

D = [MAX_NUM+1 for _ in range(N)]  # 오름차순으로 정렬하며 답을 찾아가기 위한 배열
max_length = 0  # D 배열의 max index

P = [0 for _ in range(N)]  # nums의 값들을 D를 이용해 순서를 계산했을 때, 몇 번째 index로 들어갔는지 기록하는 배열

for i in range(N):
    num = nums[i]
    pos = max_length  # D를 오름차순으로 유지하면서 num을 추가할 때, num이 들어가야할 index

    # 연산 효율을 위해, 오름차순으로 만들 수 없는 경우에만 이분검색을 하도록 최적화
    if D[max_length-1] >= num:
        pos = bisect_left(D[:max_length], num)  # 이분 검색으로 들어갈 위치 찾기
    D[pos] = num  # 해당 index에 덮어쓴다.
    P[i] = pos  # 가장 긴 증가하는 부분수열을 찾기 위해 기록
    max_length = max(max_length, pos + 1)

# 가장 긴 증가하는 부분수열 찾기
result = deque()
for i in range(N-1, -1, -1):
    if P[i] == max_length - 1:
        max_length -= 1
        result.appendleft(nums[i])
    if max_length == 0:
        break

# 출력 형식
stdout.write('{}\n'.format(len(result)))
stdout.write(' '.join(map(str, result)))