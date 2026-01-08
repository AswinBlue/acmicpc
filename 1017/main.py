# https://www.acmicpc.net/problem/1017
# 1017 소수 쌍

import sys
import math

DEBUG = 0

def Print(*args):
    if DEBUG:
        print(*args)

# 이분 매칭을 위한 DFS 함수
def bpm(u, left, right, matchR, visited):
    """
    u: 좌측 node 의 index
    left: 좌측 노드 값 리스트
    right: 우측 노드 값 리스트
    matchR: 우측 node 의 index와 매칭된 좌측 node 의 index
    visited: 현재 DFS 탐색에서 방문한 우측 node 여부
    """
    global primes
    for v in range(len(right)):
        # left[u]와 right[v]의 합이 소수이고, 아직 v를 방문하지 않았다면
        if primes[left[u] + right[v]] and not visited[v]:
            visited[v] = True
            # v가 아직 매칭되지 않았거나,
            # 기존에 v와 매칭된 노드가 다른 노드와 매칭될 수 있다면 (재귀 호출)
            if matchR[v] == -1 or bpm(matchR[v], left, right, matchR, visited):
                matchR[v] = u
                return True
    # 모든 우측 node 를 탐색했음에도 매칭이 불가능한 경우
    return False

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int, input().split()))

    first = nums[0]

    # 에라토스테네스의 체를 이용한 소수 판별
    primes = [True] * 2001
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(2000)) + 1):
        if primes[i]:
            for j in range(i * i, 2001, i):
                primes[j] = False

    # 2를 제외한 소수는 기본적으로 모두 홀수이다.
    # 짝수와 홀수 분리하여 이분 매칭 그래프 구성
    even_nums = []
    odd_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)

    # 짝수와 홀수의 개수가 다르면 완벽한 매칭이 불가능
    if len(even_nums) != len(odd_nums):
        print(-1)
        exit()
        
    # 첫 번째 수의 짝수/홀수 여부에 따라 left, right 설정
    if first % 2 == 0:
        left = even_nums
        right = odd_nums
    else:
        left = odd_nums
        right = even_nums

    result = []
    # 좌측 node(left)에서 우측 node(right)로 이분매칭 수행
    for i in range(len(right)):
        if primes[first + right[i]]:
            matchR = [-1] * (N // 2)
            matchR[i] = 0  # 첫 번째 짝수 수와 매칭하여 소수가 되는 홀수 고정
            result_count = 1
            for u in range(1, len(left)):  # u=0은 이미 첫번째 수로 매칭되었으므로 1부터 시작
                visited = [False] * len(right)
                visited[i] = True  # 이미 매칭된 홀수 수는 방문 처리
                # 좌측 node에서 우측 node 매칭 시도
                if bpm(u, left, right, matchR, visited):
                    result_count += 1
            Print(f'[DEBUG] Trying right[{i}] = {right[i]}, matched count = {result_count}, matchR = {matchR}')
            # 모든 수가 매칭된 경우 결과에 추가
            if result_count == N // 2:
                result.append(right[i])
    if result:
        result.sort()
        print(' '.join(map(str, result)))
    else:
        print(-1)