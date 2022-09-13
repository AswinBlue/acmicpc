# https://www.acmicpc.net/problem/10815

from sys import stdin, stdout
MAX_N = 500000
MIN_NUM = -10000000
MAX_NUM = 10000000

# get inputs
N = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))

# cards 리스트에 숫자가 있으면 1, 없으면 0을 표시하는 체크리스트
# MIN_NUM 이 0에 해당하므로, index = num + MIN_NUM 가 된다. 
nums = [0 for i in range(MAX_NUM - MIN_NUM + 1)]  

for c in cards:
    nums[c + MIN_NUM] = 1

M = int(stdin.readline())
check = list(map(int, stdin.readline().split()))
for c in check:
    stdout.write('{} '.format(nums[c + MIN_NUM]))


