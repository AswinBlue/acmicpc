# https://www.acmicpc.net/problem/3273
# 두 수의 합

MAX_N = 100000
MAX_X = 2000000
MAX_NUM = 1000000

N = int(input())
nums = list(map(int, input().split()))
X = int(input())

# 숫자 등장 횟수를 기록
number_count = [0 for _ in range(MAX_NUM+1)]
for n in nums:
    number_count[n] += 1

# 전체 수를 돌며 조건에 만족하는 쌍의 갯수를 찾는다.
result = 0
for i in range(1, MAX_NUM+1):
    # i가 한번 이상 등장했고,
    # X - i가 숫자 크기 제한에 걸리지 않으며,
    # X - i 또한 1번 이상 등장했을 때
    if number_count[i] > 0 and X - i <= MAX_NUM and number_count[X - i] > 0:
        # 만약 X-i가 i와 동일하다면, 반으로 나눠야 함
        if X - i == i:
            result += number_count[i] * (number_count[i] - 1)
        else:
            result += number_count[i] * number_count[X - i]
        
print(result // 2)  # (a_i, a_j) 한 쌍을 고를 때, i < j 라는 조건이 있으므로, 2로 나눠야 한다. 지금 'result'는 (a_i, a_j) (a_j, a_i) 를 모두 카운트 하였다.