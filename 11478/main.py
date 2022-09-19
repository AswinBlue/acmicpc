# https://www.acmicpc.net/problem/11478
from sys import stdin, stdout

MAX_LEN = 1000

S = set()

string = stdin.readline()
for i in range(1, len(string)):
    for j in range(i):
        S.add(string[j:i])

stdout.write(str(len(S)))