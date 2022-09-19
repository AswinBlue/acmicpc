# https://www.acmicpc.net/problem/1976

from gettext import find
from sys import stdin, stdout

MAX_N = 200
MAX_M = 1000

def find_root(S, a):
    ptr_a = a
    while S[ptr_a] >= 0:
        ptr_a = S[ptr_a]
    return ptr_a

def merge_with_collapse(S, a, b):
    res = None
    ptr = None

    # find root
    ptr_a = find_root(S, a)

    # find root
    ptr_b = find_root(S, b)

    # skip merge, if already in same group
    if ptr_a == ptr_b:
        return

    # merge
    if S[ptr_a] <= S[ptr_b]:
        S[ptr_a] += S[ptr_b]
        S[ptr_b] = ptr_a
        ptr = b
        res = ptr_a
    else:
        S[ptr_b] += S[ptr_a]
        S[ptr_a] = ptr_b
        ptr = a
        res = ptr_b

    # collapse
    while S[ptr] >= 0:
        tmp = S[ptr]
        S[ptr] = res
        ptr = tmp

N = int(stdin.readline())
M = int(stdin.readline())

S = [-1 for i in range(N)]
for i in range(N):
    row = list(map(int, stdin.readline().split()))  # node a, b와 ednge 여부
    for j in range(i + 1, N):
        # connected
        if row[j] == 1:
            merge_with_collapse(S, i, j)
            # print(S)


D = set(map(int, stdin.readline().split()))  # node a, b와 ednge 여부
# list 내 모든 인자들에 대해 root가 같은지 확인
res = find_root(S, D.pop() - 1)
result = 'YES\n'
for d in D:
    if res != find_root(S, d - 1):
        result = 'NO\n'
        break

stdout.write(result)

