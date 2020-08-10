# https://www.acmicpc.net/problem/11047
if __name__ == '__main__':
    N, K = map(int, input().split())
    coin = [0] * (N + 1)

    # get cost of coins
    for i in range(1, N + 1):
        coin[i] = int(input())

    # count coins
    num = 0
    while K > 0:
        for i in range(N, 0, -1):
            num += K // coin[i]
            K = K % coin[i]

    print(num)

