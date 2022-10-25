# https://www.acmicpc.net/problem/1450
# 냅색문제

import enum
from bisect import bisect, bisect_left, bisect_right
# bisect : upper_bound
# bisect_right : lower_bound

MAX_N = 30
MAX_C = 10**9
MAX_WEIGHT = 10**9

# 물건을 선택하는 경우를 tree 형태로 생각할 때, leaf node가 나타내는 상태 (각 물건의 선택 여부) 의 물건들의 총 무게를 인자로 하는 배열 반환
def get_weight_sum_list(N, C, P, idx, weight):
    # 모든 물건들을 다 확인한 이후 count 하나 올리고 종료
    if idx == N:
        return [weight]

    # 1. 현재 물건을 추가한 경우 (가능한 경우만)
    chosen = []
    if weight + P[idx] <= C:
        chosen = get_weight_sum_list(N, C, P, idx+1, weight + P[idx])
    # 2. 현재 물건을 추가하지 않은 경우
    unchosen = get_weight_sum_list(N, C, P, idx+1, weight)
    return chosen + unchosen

# 오름차순으로 정렬된 리스트에서 타겟 값 이하가 되는 인자 중 가장 큰 index를 반환
def upper_bound(L, target):
    length = len(L)
    # binary search
    start = 0
    end = length-1
    mid = None

    while start <= end:
        mid = (start + end) // 2
        if L[mid] <= target:
            # 중앙값이 target보다 작거나 같은 경우에는, 가장 큰 index를 찾아야 하기 때문에 우측 구간을 살펴본다.
            # 무한 반복을 없애기 위해 종료조건 추가
            if start == mid:
                # satrt + 1 == end 인 경우, 우측값도 확인하고 종료
                if start + 1 == end and L[end] <= target:
                    mid = end
                break
            
            start = mid  # mid 위치의 값도 후보에 포함되기 때문에 mid도 다음 검색 범위에 포함시킴
        else:  # L[mid] > target
            # 중앙값이 target보다 큰 경우에는, 더 작은 수를 찾기 위해 좌측 구간을 살펴본다.
            end = mid - 1

    return mid + 1

N, C = map(int, input().split())
P = list(map(int, input().split()))

D = [{} for _ in range(N+1)]
D[1][P[0]] = 2  # 첫번째 물건을 넣었을 때, 넣지 않았을 때 경우 2개

# MAX_N 이 30이므로, 그대로 검색하면 2**30 번 연산을 수행해야 하여 timeout이 발생한다.
# 2**15 는 계산 가능한 수 이므로, 반으로 나누어 계산한다. 

left = get_weight_sum_list(N//2, C, P[:N//2], 0, 0)  # 좌측 물건들을 선택하는 모든 경우의 무게를 배열로 반환
right = get_weight_sum_list(N - N//2, C, P[N//2:], 0, 0)  # 우측 물건들을 선택하는 모든 경우의 무게를 배열로 반환

result = 0  # 정답을 기록할 변수
right.sort()  # 이분검색을 위해 정렬
for l in left:
    # C - l >= r 인 right의 인자 r을 찾는다.
    # 찾은 인자의 index+1 이 좌측의 무게가 l 인 경우에 우측 물건들을 선택할 수 있는 경우의 갯수
    index_r = upper_bound(right, C - l)
    result += index_r

print(result)