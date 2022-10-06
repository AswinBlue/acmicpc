# https://www.acmicpc.net/problem/7562
# 나이트의 이동
from collections import deque

MAX_I = 300

T = int(input())
for t in range(T):
    I = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    
    visit = [[0 for _ in range(I)] for _ in range(I)]

    # do BFS
    S = deque()
    S.append((start_x, start_y, 0))
    visit[start_x][start_y] = 1
    while S:
        x, y, count = S.popleft()
        # 도착지점 도달시
        if x == end_x and y == end_y:
            print(count)  # 결과 출력
            break

        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x >= 0 and new_x < I and new_y >= 0 and new_y < I and visit[new_x][new_y] == 0:
                visit[new_x][new_y] = 1
                S.append((new_x, new_y, count + 1))
