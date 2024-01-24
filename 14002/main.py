# https://www.acmicpc.net/problem/14002
# 가장 긴 증가하는 부분 수열 4
from bisect import bisect_left
# REF:
# bisect_left : lower bound (x보다 같거나 큰 수들 중 최좌측 값의 위치)
# bisect_right : upper bound (x보다 큰 수들 중 최좌측 값의 위치)
# bisect : lower bound (lower bound 를 찾았는데 동일 값이 존재할 경우 최우측 값의 위치)
MAX_N = 1000
MAX_NUM = 1000

N = int(input())
nums = list(map(int, input().split()))
nums = nums[:N]  # N 초과하면 버림(쓸데없을듯)

# nums에 담긴 숫자들을 순회하며 check 배열의 0번 index부터 채워넣는다.
# 만약 이전 값보다 현재 값이 작을경우(오름차순이 아니게 될 경우) check 배열이 오름차순을 유지하도록 알맞은 위치부터 덮어쓴다.
check = [(MAX_NUM + 1) for _ in range(N)]  # 문제 풀이를 위한 배열
max_length = 0  # 가장 길었던 오름차순의 길이
position = [0 for _ in range(N)]  # nums[i] 가 check 배열에 들어갔을 때 index를 position[i]에 저장
for i, number in enumerate(nums):
    # 알맞은 위치 찾아 idx 수정
    idx = bisect_left(check[:max_length], number)  # 0 ~ max_length 까지 인자들 사이에서 알맞은 위치를 찾음
    # print(number, idx, check)
    check[idx] = number  # 값을 덮어쓰고 계속 진행
    position[i] = idx  # 위치 기억
    if idx + 1 > max_length:
        max_length = idx + 1
        result_list = check[:max_length]

print(max_length)

# 가장 긴 오름차순 배열을 찾는 과정
# position 배열을 뒤에서 부터 순회하며 가장 큰 index(max_length - 1) 부터 index를 순차적으로 찾아나가면 된다.
result_list = []
for i in range(N-1, -1, -1):
    if position[i] == max_length-1:
        result_list.append(nums[i])
        max_length -= 1
print(*reversed(result_list))