# https://www.acmicpc.net/problem/17299
# 오등큰수

from collections import deque

MAX_N = 1000000
MAX_NUM = 1000000

N = int(input())
arr = list(map(int, input().split()))

# 순열에서 특정 수가 몇번 등장했는지 카운트한 배열
counts = [0 for _ in range(MAX_NUM+1)]

# 갯수 카운트
for num in arr:
    counts[num] += 1

# 결과 저장용 배열
result = [-1 for _ in range(N)]

# 문제의 조건에 의해 i번 오등큰수를 구하기 위해서는 i ~ N 까지 수들이 비교 대상에 속하고
# i-1번째 오등큰수는 i번째 오등큰수보다 크거나 같다. 
# N번부터 0번까지 i번째 오등큰수보다 작은 수들은 비교 대상에서 제외하며 순회한다.
S = deque()  # linked list 사용하여 시간 단축
for i in range(N-1, -1, -1):
    while S:
        # stack의 top과 현재 수 등장 횟수 비교
        if counts[S[-1]] <= counts[arr[i]]:
            # top의 오큰수가 더 작으면 pop
            S.pop()
        else:
            # top의 오큰수가 더 크면
            # 결과에 top을 저장하고 loop 탈출
            result[i] = S[-1]
            break
    # 현재 값도 stack에 추가
    S.append(arr[i])

print(' '.join(map(str, result)))