# https://www.acmicpc.net/problem/1007
# 벡터 매칭

from itertools import combinations

DEBUG = 0

if DEBUG:
    input = open("1007/input.txt", "r").readline

def Print(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

MAX_N = 20

'''
핵심 아이디어:
N개의 점들은 두 개씩 짝지어져야 한다.
즉, N개의 점들 중 절반은 벡터의 시작점, 나머지 절반은 벡터의 끝점이 된다.
N개의 점을 두 그룹으로 나누는 모든 조합을 시도하여 각 경우에 대해 벡터 합의 크기를 계산하고, 그 중 최소값을 찾는다.
'''
if __name__ == "__main__":
    T = int(input())
    # test case 반복
    for _ in range(T):
        # 입력 수신
        N = int(input())
        points = [list(map(int, input().split())) for _ in range(N)]
        total_x = sum(p[0] for p in points)
        total_y = sum(p[1] for p in points)

        min_dist_sq = float('inf')  # 최종 값 (제곱 형태)
        
        # N개의 점 중 N/2개를 선택하는 조합
        for combo in combinations(points, N // 2):
            # 더하는 그룹(+)의 x, y 좌표 합
            sum_x_plus = sum(p[0] for p in combo)
            sum_y_plus = sum(p[1] for p in combo)

            # 전체 벡터 합 계산
            sum_x = 2 * sum_x_plus - total_x
            sum_y = 2 * sum_y_plus - total_y
            
            dist_sq = sum_x ** 2 + sum_y ** 2
            min_dist_sq = min(min_dist_sq, dist_sq)

        min_dist = min_dist_sq ** 0.5
        print(f"{min_dist:.12f}")
