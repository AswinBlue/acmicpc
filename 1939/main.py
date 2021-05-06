if __name__ == "__main__":
    INF = 1000000001
    N, M = map(int, input().split())
    arr = [[] for i in range(N)]

    for i in range(M):
        A, B, C = map(int, input().split())
        arr[A-1].append((B-1,C))
        arr[B-1].append((A-1, C))
    start, end = map(int, input().split())

    # print(arr)

    visited = [0 for i in range(N)]
    weight = [0 for i in range(N)]
    visited[start - 1] = 2
    for d, w in arr[start - 1]:
        weight[d] = w
        visited[d] = 1

    visit_cnt = 1
    while True :
        if visit_cnt >= N:
            break
        #print('@', visit_cnt)
        current = -1
        for t in range(N):
            if visited[t] != 2:
                if current == -1:
                    current = t
                elif  weight[current] < weight[t]:
                    current = t

        if visited[current] != 2:
            visit_cnt += 1
            visited[current] = 2
            #print('#', current+1, visited, weight)
            for d, w in arr[current]:
                if visited[d] != 2:
                    visited[d] = 1
                    if weight[current] > w:
                        if weight[d] < w and w < INF:
                            weight[d] = w
                    else:
                        weight[d] = weight[current]
                    #print(d+1, weight)

    print(weight[end - 1])

