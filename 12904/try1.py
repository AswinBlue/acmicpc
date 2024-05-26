# A와 B
# https://www.acmicpc.net/problem/12904

from sys import setrecursionlimit
setrecursionlimit(10000)

#####
# 문제에 적힌대로 함수를 구현하여 동작 시켜 보았다.
# timeout 이 발생한다.
#####

DEBUG = 1

def Print(*args):
    if DEBUG:
        print(*args)

def func1(string:str):
    # append 'A'
    return string + 'A'

def func2(string:str):
    # reverse the string and append 'B'
    tmp = ''.join(reversed(string))
    tmp += 'B'
    return tmp

def compare(S:str, T:str):
    Print('compere:', S, T)
    if S != T[:len(S)]:
        return False
    if len(S) == len(T):
        if S == T:
            return True
        else:
            return False
    s1 = func1(S)
    if compare(s1, T):
        return True
    s2 = func2(S)
    if compare(s2, T):
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


