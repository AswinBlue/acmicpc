# 제곱 ㄴㄴ수
# https://www.acmicpc.net/problem/1016

# 1 ≤ min ≤ 1,000,000,000,000
# min ≤ max ≤ min + 1,000,000

DEBUG = 0
if DEBUG:
    input = open("1016/input.txt", "r").readline

def Print(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

'''
핵심 아이디어
에라토스 테네스의 채 처럼 제곱수를 지워 나가며 값을 구한다.
'''
if __name__ == "__main__":
    min_val, max_val = map(int, input().split())
    size = max_val - min_val + 1
    is_not_square_free = [False] * size  # True: 제곱 ㄴㄴ수, False: 제곱 ㄴㄴ수가 아님

    limit = int(max_val**0.5) + 1
    for i in range(2, limit):
        # 2부터 limit까지 제곱수를 구한다.
        square = i * i  
        # start는 min_val 에서 max_val 사이 값들 중 square로 나눠 떨어지는 가장 작은 수
        start = (min_val + square - 1) // square * square
        for j in range(start, max_val + 1, square):
            # min_val에서 max_val까지 suqare로 나눠 떨어지는 수를 후보에서 제외
            is_not_square_free[j - min_val] = True

    result = is_not_square_free.count(False)
    print(result)