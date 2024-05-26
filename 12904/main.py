# A와 B
# https://www.acmicpc.net/problem/12904

#####
# T에서 S를 구하는 방식으로 변경하였다.
# 경우의 수가 줄어들어 greedy 방식으로 풀 수 있게 되었다.
#####
from sys import setrecursionlimit
setrecursionlimit(10000)

DEBUG = 0

def Print(*args):
    if DEBUG:
        print(*args)

def func1(string:str):
    # pop 'A'
    return string[:-1]

def func2(string:str):
    # reverse the string and append 'B'
    tmp = ''.join(reversed(string))
    tmp += 'B'
    return tmp

def compare(S:str, T:str):
    while len(S) < len(T):
        Print('compere:', S, T)
        tmp = T[-1]
        T = T[:-1]  # pop T[-1]
        if tmp == 'A':  # last word is 'A'
            pass
        elif tmp == 'B':  # last word is 'B'
            # reverse the string
            T = ''.join(reversed(T))
    if S == T:
        return True
    return False

if __name__ == '__main__':
    S = input()
    T = input()
    s_len = len(S)
    t_len = len(T)

    result = compare(S, T)
    if result:
        print(1)
    else:
        print(0)


