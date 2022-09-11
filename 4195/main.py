# https://www.acmicpc.net/problem/4195
# 친구 네트워크
from sys import stdin, stdout

MAX_F = 100000
DEBUG = 0

def Print(*arg):
    if DEBUG:
        print(arg)

def find_root(network, name):
    ptr = name
    # find root
    while type(network[ptr]) is str:
        ptr = network[ptr]
    result = ptr
    # collapsing find
    ptr = name
    while type(network[ptr]) is str:
        tmp = ptr
        ptr = network[ptr]
        network[tmp] = result

    return result

T = int(stdin.readline())
for t in range(T):
    F = int(stdin.readline())
    network = {}
    
    for f in range(F):
        a, b = list(stdin.readline().split())
        # a가 기존에 있던 경우
        if a in network:
            A = find_root(network, a)
            # b 가 기존에 있었으면
            if b in network:
                B = find_root(network, b)
                # root가 같은 경우는 생략해야함. 아니면 무한루프에 진입
                if A != B:
                    # 숫자가 큰곳에 이어붙임
                    if network[B] > network[A]:
                        network[B] += network[A]
                        network[A] = B
                    else:
                        network[A] += network[B]
                        network[B] = A
            # b 가 없었으면 새로 만들고 a에 이어붙임
            else:
                network[b] = A
                network[A] += 1
        else:
            # a가 처음 나온 경우
            if b in network:
                # b 가 기존에 있었으면
                B = find_root(network, b)
                network[B] += 1
                network[a] = B
            else:
                # b 가 기존에 없었으면
                network[a] = b
                network[b] = 2

        Print(a, find_root(network, a), network[find_root(network, a)], "\n", network)
        # print result, a 의 친구 네트워크에는 몇명이 있는지 출력
        stdout.writelines("{}\n".format(network[find_root(network, a)]))