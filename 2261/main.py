# https://www.acmicpc.net/problem/2261
# 가장 가까운 두 점

# 접근방식
# MAX_N이 10만이기 때문에 모든 점의 위치를 다 구하는건 시간초과다
# 불필요한 연산을 줄여내고 promising 한 점들만 비교하는 요령이 필요하다. promising한 점들을 찾아내자.
# 1. x좌표에 대해 오름차순으로 정렬을 하면, 일단 x 좌표상 거리는 알 수 있다.
#    x좌표상 인접한 두 점의 거리 'd'를 하나 구하고, x축 거리가 'd'보다 크다면 후보에서 제외한다.
# 2. 후보군에 든 점들 사이를 계산하며 'd'를 추출, 'd'들의 최소값 'min_d'를 갱신하며 찾아낸다. 
#    계산할 때 y좌표도 promising 한지 점검하면 연산을 아낄 수 있다. 
# 3. 후보군을 모두 검사했으면 다음 점을 추가하고, x축 상 거리에 의해 후보군에서 제외되는 점은 제외한다.
# 4. 추가된 점을 기준으로 2번 과정을 다시 수행하고, 이후 3번 과정을 수행한다. 더 이상 후보군에 넣을 점이 없을 때 까지 이를 반복한다.

# 개선
# pow / sqrt 연산이 많아지면 시간초과가 발생한다. 
# Y좌표의 promising을 추가로 계산한다.
# bisect 로 이분탐색 연산을 이용하여 연산시간을 최적화 한다.

DEBUG = 1

from collections import deque
from math import sqrt
import operator
from bisect import bisect, bisect_left, bisect_right


MAX_XY = 10_000
MIN_XY = -10_000
MAX_N = 100_000
MIN_N = 2


def Print(*args):
    if DEBUG:
        print(*args)

# 두 좌표를 입력받아 거리의 제곱을 반환하는 함수
def distance_square(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2

if __name__ == "__main__":
    N = int(input())
    save = [0 for _ in range(N)]
    for i in range(N):
        x, y = map(int, input().split())
        save[i] = (x, y)

    # sort 'save' by 'x'
    save.sort(key=operator.itemgetter(0, 1))  # REF: 0번 index 우선 정렬, 이후 1번 index 정렬. lambda x: (x[0], x[1]) 보다 함수호출이 적어 빠름 (https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes)
    Print(save)

    # set pointA
    idx = 0
    pointA = save[0]

    # set second point as pointB
    pointB = save[1]
    idx2 = 2  # increase

    # promising = save[idx:idx2]. I will remove add add promising point by moving 'idx' and 'idx2'
    powed_min_dist = distance_square(pointA, pointB)
    min_dist = sqrt(powed_min_dist)
    # for all elements in 'save', compare x-axis distance between two point
    # filter out non-prospective elements by comparing 'minimun-length' & 'x-axis distance'
    # use sweep line algorithm
    Print(f'{save[0]}~{save[1]}={powed_min_dist}')
    while idx2 < N:
        # idx2 = next point to add in 'promising' pool
        if powed_min_dist == 0:# 0 is the shortest length, no need to find more
            break
        pointB = save[idx2]
        x2, y2 = pointB

        while idx < idx2:
            if abs(x2 - save[idx][0]) >= min_dist:
                # check 'x' axis and remove unpromising points
                idx += 1
            elif x2 == save[idx][0] and abs(y2 - save[idx][1]) >= min_dist:
                # check 'y' axis and remove unpromising points
                idx += 1
            else:
                break  # if 'idx' is promising, 'idx + a' will promising too

        if idx >= idx2:
            idx2 += 1
            continue  # promising 한 case가 없는 경우에 해당. continue
        # filter promising points by 'y' axis distance. lower-upper bound can be found because 'save' is arranged by Y axis, too.
        upper_bound = bisect_right(save, y2 + min_dist, lo=idx, hi=idx2, key=operator.itemgetter(1)) # find upper bound
        if upper_bound > idx2:
            upper_bound = idx2
        lower_bound = bisect_left(save, y2 - min_dist, lo=idx, hi=idx2, key=operator.itemgetter(1)) # find lower bound
        if lower_bound < idx:
            lower_bound = idx
        # REF: pair 를 bisect로 비교하는 방법 (https://stackoverflow.com/questions/20908047/using-bisect-in-a-list-of-tuples)
        Print(f'idx:{idx}, idx2:{idx2}, minY:{y2-min_dist}, maxY:{y2+min_dist}, [{lower_bound}:{upper_bound}]')
        # check distance from all 'promising point' to 'pointB'
        for i in range(lower_bound, upper_bound):
            dist = distance_square(save[i], pointB)
            powed_min_dist = min(powed_min_dist, dist)  # update powed_min_dist
            min_dist = sqrt(powed_min_dist)  # update min_dist

            Print(f'[{lower_bound}:{upper_bound}] i={i}, p1:{save[i]}, p2:{pointB}, dist:{dist}/{powed_min_dist}')
            # Print(f'{promising}')
        # add current target point(pointB) to promising pool and increase index to find next pointB
        idx2 += 1

    # print result
    print(powed_min_dist)