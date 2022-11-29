# https://www.acmicpc.net/problem/2170
# 선 긋기
# 본 방법은, (1, 3) (5, 7) (2, 6) 순서로 선이 오는 경우 잘못된 값을 반환하므로 실패한다.
from sys import stdin, stdout

N = int(stdin.readline())

lines = []  # 겹치지 않는 선들을 저장할 배열
for _ in range(N):
    x, y = map(int, stdin.readline().split())
    handled = False  # 이떄까지 그은 선과 겹치는 부분이 있는지 체크하는 flag
    # 이때까지 그었던 선과 비교하여 겹치는 부분 확인
    for idx, (X, Y) in enumerate(lines):
        # case 1, intersect
        if x < X <= y < Y:
            lines[idx] = (x, Y)
            handled = True
            break
        elif X < x <= Y < y:
            lines[idx] = (X, y)
            handled = True
            break
        # case 2, include
        elif x <= X < Y <= y:
            lines[idx] = (x, y)
            handled = True
            break
        elif X <= x < y <= Y:
            handled = True
            break  # skip
        # case 3, separated
        else:
            pass  # find next
    # 겹치는 부분 없었으면 추가
    if not handled:
        lines.append((x,y))

# 최종 결과 계산
length = 0
for x, y in lines:
    length += (y - x)

stdout.write(str(length))