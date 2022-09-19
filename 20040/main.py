# https://www.acmicpc.net/problem/20040
# 사이클 게임
from sys import stdin, stdout, setrecursionlimit
MIN_N = 3
MAX_N = 500000
MIN_M = 3
MAX_M = 100000
setrecursionlimit(MAX_M)

def find_root(V, a):
    # find root
    result = None
    ptr = a
    while V[ptr] >= 0:
        ptr = V[ptr]

    # collapsing find
    result = ptr
    ptr = a
    while V[ptr] >= 0:
        tmp = ptr
        ptr = V[ptr]
        V[tmp] = result
        
    return result

N, M = map(int, stdin.readline().split())

V = [-1 for _ in range(N)]

result = 0
for m in range(1, M+1):
    a, b = map(int, stdin.readline().split())
    # cycle이 이미 있다면, 더이상 진행 불필요
    if result != 0:
        continue
    A = find_root(V, a)
    B = find_root(V, b)
    
    if A == B:
        # 두 점이 같다면 cycle이 만들어 진다. 더이상 진행 불필요
        result = m
        continue

    # merge two vertex
    if V[A] <= V[B]:
        V[A] += V[B]
        V[B] = A
    else:
        V[B] += V[A]
        V[A] = B

stdout.writelines(str(result))