# https://www.acmicpc.net/problem/11047
MAX = 999999999
if __name__ == '__main__':
    N, K = map(int, input().split())
    coin = [0] * (N + 1)
    cost = [MAX] * (K + 1)
    cost[0] = 0

    # get cost of coins
    for i in range(1, N + 1):
        coin[i] = int(input())

    # cost[i] means "number of minimum coin to make price 'i'"
    for i in range(1, K + 1):
        for j in range(1, N + 1):
            if coin[j] <= i:
                tmp  = cost[i - coin[j]] + 1
                if tmp < cost[i]:
                    cost[i] = tmp

    print(cost[K])
