# https://www.acmicpc.net/problem/2470
# 두 용액

import enum
from gc import collect


MAX_PH = 1000000000
MIN_PH = -1000000000
MAX_N = 100000

N = int(input())
liquid = list(map(int, input().split()))
# 두 수의 절대값이 비슷할 수록 합이 0에 가까움.
# 절대값으로 정렬하고, 인접한 두 수의 합을 비교
min_result = MAX_PH * 2
result = None
liquid.sort(key=lambda x:(abs(x)))
for idx in range(len(liquid) - 1):
    # 인접한 두 수의 합의 절대값 중 가장 작은 값을 채택
    if abs(liquid[idx] + liquid[idx+1]) < min_result:
        min_result = abs(liquid[idx] + liquid[idx+1])
        result = [liquid[idx], liquid[idx+1]]

result.sort()  # 문제에서 오름차순으로 출력을 요구함
print(' '.join(map(str, result)))