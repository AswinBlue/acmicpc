# https://www.acmicpc.net/problem/17435
# 합성함수와 쿼리

from sys import stdin, stdout
import math

MAX_M = 200000
MAX_Q = 200000
MAX_N = 500000

M = int(stdin.readline())
F = list(map(int, stdin.readline().split()))
Q = int(stdin.readline())
F.insert(0,0)  # 0번 index 에 빈값 집어넣음
DP = [F]  # dynamic programming
# 1 ~ log2(MAX_N) 까지 수에 대해 sparse table을 작성한다.
# 2^k >= MAX_N 을 만족하는 가장 작은 k가 log2(MAX_N) 이다.
for m in range(math.ceil(math.log2(MAX_N))):
    row = [DP[m][f] for f in DP[m]]
    DP.append(row)
    
for q in range(Q):
    n, x = map(int, stdin.readline().split())
    d = 0
    num = x
    while n > 0:
        if n & 1:
            num = DP[d][num]
        d += 1
        n >>= 1
    stdout.write('{}\n'.format(num))
