# https://www.acmicpc.net/problem/1725
# 히스토그램
from collections import deque
from sys import stdin, stdout

MAX_SIZE = 2000000000
MAX_N = 100000
MAX_HEIGHT = 1000000000

N = int(stdin.readline())
hist = [0 for _ in range(N+2)]  # 0번과 N+1번 index는 boundary로 사용해야한다.
for n in range(1, N+1):
    hist[n] = int(stdin.readline())

# i번째 히스토그램의 높이는 hist[i]이다. 
# hist[i]로 만들 수 있는 가장 큰 사각형은 i < j 이면서 hist[i] > hist[j] 인 값이 나왔을 때 결정된다.
# 그 값은 hist[i] * ((j-1) - i - 1) 이 된다.
# 조건을 만족하는 값이 나올 때 까지 i를 stack에 넣어둔 채로 진행한다. 

# 히스토그램을 순회하며 i-1보다 i의 값이 크다면 stack에 i를 집어넣는다.
S = deque([0])  # 시작 index가 1이기에 기준점 0을 추가해서 모든 histogram에 대해 처리가 가능하도록 함
max_width = 0

# 1부터 N+1까지 검사한다. 히스토그램의 양 옆이 높이 0인 값으로 둘러쌓여져 있기 때문에 아래 로직이 끝까지 정상동작 할 수 있음
for i in range(1, N+2):
    # i < j 이면서 hist[i] > hist[j] 을 만족하는 j가 나온 경우, stack에서 pop하고 넓이를 계산한다.
    # 이를 stack의 top부터 조건이 만족하지 않을 때 까지 반복하여 검사한다. 

    # print(S, max_width)
    while S and hist[S[-1]] > hist[i]:
        height = hist[S.pop()]
        length = i - S[-1] - 1  # 구해야 할 부분은 S[-1]+1 ~ i-1 의 길이
        max_width = max(max_width, length * height)  # hist[top] 으로 만들 수 있는 가장 큰 넓이를 구하고, 이를 이전 값과 비교
    S.append(i)  # 현재 값 추가

stdout.write(str(max_width))