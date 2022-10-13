# https://www.acmicpc.net/problem/1806
# 부분합
from sys import setrecursionlimit

DEBUG = 0
MAX_N = 100000
MAX_S = 100000000
def Print(*args):
    if DEBUG:
        print(*args)

N, S = map(int, input().split())
nums = list(map(int, input().split()))

# 시작점과 끝점을 두고, 한칸씩 이동해가며 두 범위 안의 수들의 합이 S가 되는지 확인한다.
# S가 된다면, 그 길이를 확인하고, 전체 list를 모두 순회할 때 까지 조건이 만족하는 길이들을 비교한다.
left = right = 0
sum = nums[0]
min_length = 1 if sum >= S else MAX_N + 1  # nums[0]이 S보다 크다면, min_length는 1이다. 아니라면 초기값 'MAX_N + 1' 을 설정한다.
while not (left == right == (len(nums)-1)):
        
    # 이동
    if sum < S and right + 1 < len(nums):
        right += 1
        sum += nums[right]
    else:
        # sum >= S 이거나, right가 끝에 도달해 더이상 이동 못하는 상황
        left += 1
        sum -= nums[left-1]
    # 길이 비교
    if sum >= S:
        min_length = min(min_length, right - left + 1)


# 조건을 만족하는 값을 못찾았으면 0으로 세팅
if min_length == MAX_N+1:
    min_length = 0
print(min_length)

