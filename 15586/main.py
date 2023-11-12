# https://www.acmicpc.net/problem/15586
# MooTube (Gold)

from bisect import bisect

MAX_Q = 100_000
MAX_K = 1_000_000_000

# 문제에서 N-1개의 edge로 모든 node간에 경로가 있도록 설정을 했다고 하였으므로, 
# 이는 cycle이 없는 graph로 봐도 된다 (i에서 j로 가는 경로는 무조건 하나)
# 우리가 구해야 하는 경우는 All Pair Shortest Path 이므로,
# Single Start shortest path 알고리즘 (dijkstra, bellman-ford) 을 사용하기에는 부적합하다.
# All Pair Shortest Path 알고리즘 (floyd-warshall) 을 사용해야 할 것 같지만,
# 시간 복잡도상 사용하지 못한다. 
# 문제 조건에 의해 i에서 j로가는 경로는 무조건 하나이므로, 완전탐색 알고리즘 (BFS) 를 돌려서 
# 모든 경로만 파악해 주면 된다. (경로간의 비용 비교는 필요없음)

DEBUG = True
def Print(*args):
    if DEBUG == True:
        print(*args)

def get_input():
    global N, Q, USADO

    N, Q = map(int, input().split()) # N : 동영상 개수, Q : 문제 개수
    USADO = [[0 for _ in range(N+1)] for _ in range(N+1)] # 유사도를 저장할 list
    graph = [[] for _ in range(N+1)] # edge들을 저장할 list


    # 주어지는 유사도 입력에 대해 list로 저장
    for n in range(N-1):
        p, q, r = map(int, input().split())
        graph[p].append((q,r))
        graph[q].append((p,r))
        Print('p:', p, 'q:', q, 'r:', r)
        # p -> q 유사도 추가
        USADO[p][q] = r
        USADO[q][p] = r
        for x, y in graph[p]:
            # n -> p -> q 로 가는 경로가 없으면 생성
            if USADO[x][q] == 0 and x != q:
                USADO[x][q] = min(y, r)
                USADO[q][x] = min(y, r)
        for n, m in graph[q]:
            # n -> q -> p 로 가는 경로가 없으면 생성
            if USADO[x][p] == 0 and x != p:
                USADO[x][p] = min(y, r)
                USADO[p][x] = min(y, r)
        Print(USADO)

def solve():
    global N, Q, USADO

    # Print(USADO)

    # 받은 유사도를 오름차순으로 정렬
    for n in range(N-1):
        USADO[n].sort()
    
    Print('sorted:', USADO)

    # 문제 입력받아 해결
    for q in range(Q):
        k, v = map(int, input().split())
        # lower bound로 위치 찾고, 전체에서 lower bound 보다 크기가 작은 인자를 제외한 갯수
        lower_bound = bisect(USADO[v], k-1)
        result = len(USADO[v]) - lower_bound
        Print('k:', k, 'v:', v, 'lower_bound:', lower_bound)
        # bisect의 한계에 의해 아래는 수작업을 걸러야 한다. lower-bound가 0번 index의 값보다 작아도 0을 반환하고, 0번 index의 값과 같아도 0을 반환
        # 모두 다 포함되는 경우
        if lower_bound == 0:
            if USADO[v][0][1] >= k:
                print(result)
            # 첫 인자가 빠지는 경우
            else:
                print(result - 1)
        else:
            print(result)

# 필요없네
def binary_search(list, left, right, target):
    # not promising
    if left > right:
        return -1
    
    # found
    mid = (left + right) // 2
    if target == list[mid]:
        return mid
    
    # promising
    l = binary_search(list, left, mid-1, target)
    if l >= 0:
        return l
    r = binary_search(list, mid+1, right, target)
    if r >= 0:
        return r
    
    # not exist
    return -1
    

if __name__ == '__main__':
    get_input()
    solve()



