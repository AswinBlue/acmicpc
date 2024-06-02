# 트리의 지름
# https://www.acmicpc.net/problem/1167

# [풀이 방법]
# floyd warshall 알고리즘 ASP(All pair Shortest Path) 은 시간초과로 사용 불가
# tree의 지름은 가장 긴 임의의 두 점 사이의 거리이므로, leaf node ~ leaf node 간 거리가 될 것이다. 
# leaf node 는 연결된 점이 한 개 뿐인 node 들을 모아서 node 간 거리를 탐색한다. 

# tree의 지름 찾는 공식:
# 특정 node 'A' 에서 가장 멀리 떨어진 node 'B' 를 찾은 다음, node 'B' 에서 가장 멀리 떨어진 node 'C' 까지의 거리를 구하면, 이 거리가 tree 의 지름이다.
DEBUG = 0
MAX_VERTEX = 100_000

from sys import setrecursionlimit
setrecursionlimit(MAX_VERTEX)

def Print(*args):
    if DEBUG:
        print(*args)

# DFS 실행
def do_dfs(start, current, distance):
    global links, max_length

    Print("DFS:", start, "->", current, distance)
    result = 0

    for destination, length in links[current]:
        if distance[destination] == -1:
            # update 'distance'
            # (문제에서 주어진 graph는 tree 이기 때문에 어떤 node 'A' 에서 다른 node 'B' 로 갈 수 있는 경로는 둘 이상 존재하지 않는다. 한번만 수행됨이 보장됨)
            distance[destination] = distance[current] + length
            # update 'max_length'
            if max_length < distance[destination]:
                max_length = distance[destination]
                result = destination
            # do next vertex
            ret = do_dfs(start, destination, distance)
            Print("retrurn:", ret, "/", result)
            if distance[result] < distance[ret]:
                result = ret
    return result

if __name__ == '__main__':
    V = int(input())

    # distance = [[0 for _ in range(V + 1)] for _ in range(V + 1)]  # distance[i][j] = i ~ j 까지 거리
    links = [[] for _ in range(V + 1)]  # links[i] = vertex 'i' 에 연결된 vertex 와 그 vertex 까지 거리를 pair로 묶어 배열로 나열
    # number_of_edge = [0 for _ in range(V + 1)]  # node 에 연결된 edge 의 수. 처음에는 필요할줄 알았으나, tree 의 지름을 구하는 공식이 있어서 불필요
    for v in range(1, V + 1):
        line = list(map(int, input().split()))
        vertex = line[0]  # 첫 번째 인자가 vertex를 의미
        idx = 1
        while True:
            # 두 번째 인자부터 두 숫자씩 묶어서 (vertex2, vertex ~ vertex2 까지 거리) 를 의미
            target = line[idx]
            if target == -1:  # 종료조건: 입력을 순차적으로 읽었을 때 -1을 만나는 경우
                break
            length = line[idx+1]
            # distance[vertex][target] = length  # 메모리제한에 의해 사용 불가
            links[vertex].append((target, length))
            # number_of_edge[vertex] += 1  # edge 갯수 추가
            idx += 2
    Print("links:", links)
    # 탐색 시작
    # number_of_edge 가 1 인 vertex 에 대해 확인
    # -> tree 의 지름을 구하는 공식이 있어서 불필요 
    # candidates = []
    # for i in range(1, V + 1):
    #     if number_of_edge[i] == 1:
    #         candidates.append(i)
    # Print("candidates:", candidates)

    max_length = 0

    # 완전탐색 두 번만 수행하면 됨
    distance = [-1 for _ in range(V + 1)]
    distance[1] = 0
    start = do_dfs(1, 1, distance)
    Print(f"distance from 1:{distance}")
    distance = [-1 for _ in range(V + 1)]
    distance[start] = 0
    do_dfs(start, start, distance)
    Print(f"distance from {start}:{distance}")

    print(max_length)