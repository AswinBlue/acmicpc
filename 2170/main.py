# https://www.acmicpc.net/problem/2170
# 선 긋기
from sys import stdin, stdout

N = int(stdin.readline())

lines = []  # 겹치지 않는 선들을 저장할 배열
for _ in range(N):
    x, y = map(int, stdin.readline().split())
    lines.append((x,y))


lines.sort()  # X를 기준으로 정렬. x를 기준으로 정렬했기 때문에 앞에서부터 순서대로 겹치는 부분이 있는지 비교하다 겹치지 않는 선이 나오면 그 뒤의 선들과도 겹치지 않는게 보장됨

ptr = 0  # 포인터
length = 0  # 최종 길이

# 모든 선들을 비교했을 때 종료
while ptr < len(lines):
    X, Y = lines[ptr]
    ptr += 1
    # 이때까지 그었던 선과 비교하여 겹치는 부분 확인. 겹치면 합치고, 겹치는 부분이 없으면 다음으로 이동한다.
    while ptr < len(lines):
        x, y = lines[ptr]
        # case 1, intersect
        if X <= x <= Y <= y:
            Y = y  # 범위 확장
            ptr += 1  # 다음 계산
        # case 2, include
        elif X <= x < y <= Y:
            ptr += 1  # 다음 계산
        # case 3, separated
        else:
            break  # 겹치는 부분 없음
    length += (Y - X)  # 겹치는 부분이 더 없으면 총 길이 계산

stdout.write(str(length))