# https://www.acmicpc.net/problem/17298
# 오큰수

MAX_N = 1000000
MAX_NUM = 1000000

N = int(input())
arr = list(map(int, input().split()))
result = [ -1 for _ in range(N)]

# i번째 수의 오큰수를 구하려면 [i+1:N+1] 영역의 수를 확인해야 한다.
# i-1의 오큰수는 i번째 수의 오큰수보다 크거나 같다.
# N번 수부터 1번 수까지 거꾸로 거슬러 진행하면 연산을 절약할 수 있다.

S = [0 for _ in range(N)]  # 비교 대상을 stack으로 관리. top에 가까울수록 좌측에 위치한 수
top = 0  # append 많이 사용하면 timeout 걸리니까 변수 top으로 스택 관리

for i in range(N-1, -1, -1):
    while top > 0:
        if S[top-1] <= arr[i]:
            # 현재 수보다 더 작은 수는 더이상 비교할 필요가 없으므로 비교 대상에서 제거
            top -= 1
        else:
            result[i] = S[top-1]  # 결과 설정
            break
    # 현재 위치의 수를 비교 대상에 넣음
    S[top] = arr[i]
    top += 1


print(' '.join(map(str, result)))