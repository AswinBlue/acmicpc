# https://www.acmicpc.net/problem/1717
from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
S = [-1 for i in range(n+1)]
for i in range(m):
    f, a, b = map(int, stdin.readline().split())

    if f == 0:
        # A root 검색
        ptr = a
        while S[ptr] >= 0:
            ptr = S[ptr]
        resA = ptr

        # B root 검색
        ptr = b
        while S[ptr] >= 0:
            ptr = S[ptr]

        resB = ptr

        # 이미 같은 그룹이면 병합 생략
        if resA == resB:
            continue


        # 병합
        res = None
        if S[resA] < S[resB]:
            S[resA] += S[resB]
            S[resB] = resA
            ptr = b
            res = resA
        else:
            S[resB] += S[resA]
            S[resA] = resB
            ptr = a
            res = resB

        # 하위 node들도 결과 갱신
        while S[ptr] >= 0:
            tmp = ptr
            ptr = S[ptr]
            S[tmp] = res

    if f == 1:
        
        while S[a] >= 0:
            a = S[a]
        while S[b] >= 0:
            b = S[b]
        if a == b:
            stdout.writelines('YES\n')
        else:
            stdout.writelines('NO\n')
    # print(S)