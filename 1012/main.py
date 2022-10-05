MAX_M = 50
MAX_N = 50
MAX_K = 2500

T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())

    farm = set()
    for k in range(K):
        x, y = map(int, input().split())
        farm.add((x,y))

    # 각 좌표별로 DFS 수행, 더이상 DFS 할게 없으면 한 그룹을 모두 순회한 것
    count = 0
    # 아직 방문하지 않은 좌표가 있으면 탐색 실행
    while farm:
        count += 1
        S = [farm.pop()]  # 전체 목록중 하나를 빼서 stack에 넣고 DFS 시작
        while S:
            x, y = S.pop()
            # 상하좌우 탐색
            for d in -2,0,2,4:
                nx = x + d // 3
                ny = y + d % 3 - 1
                # 새로운 좌표가 기존 좌표에 속한다면
                if (nx,ny) in farm:
                    # 방문한 좌표는 전체 목록에서 제거.
                    farm.remove((nx,ny))
                    # stack에 추가
                    S.append((nx,ny))

    print(count)