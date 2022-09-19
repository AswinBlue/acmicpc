# https://www.acmicpc.net/problem/1269

from sys import stdin, stdout

a, b = map(int, stdin.readline().split())
A = set(map(int, stdin.readline().split()))
B = set(map(int, stdin.readline().split()))
stdout.writelines(str(len(A-B) + len(B-A)))

