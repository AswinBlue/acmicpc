# https://www.acmicpc.net/problem/2261
# 가장 가까운 두 점

# 접근방식
# MAX_N이 10만이기 때문에 모든 점 사이의 거리를 구하는건 시간초과다
# 불필요한 연산을 줄여내고 promising 한 점들만 비교하는 요령이 필요하다. promising한 점들을 찾아내자.
# 1. 어떤 점 A와 어떤 점 B 사이의 거리 dist를 안다면, 어떤 점 C와 어떤 점 D 사이의 x간 거리가 dist보다 크다면 거리를 계산할 필요가 없다. 
#    마찬가지로 C와 D사이의 y간 거리가 dist보다 커도 계산을 하지 않아도 된다.
# 2. 점 B가 정해지면, 점 B와 promising한 점들(1번 조건에 부합하는 점들)에y축에 대한 거리를 계산하여야 한다. 
# 3. 모든 점들이 점 B가 되어 2번 과정을 거쳐야 한다. 
# 4. 점들을 저장한 배열(이하 save)을 x좌표에 대해 오름차순으로 정렬을 하면 x좌표상 promising 한 점들은 아래와 같다.
#    target(*) 을 기준으로 좌측 일정 구간만 promising(O) 하게 된다. (우측은 아직 미확인 영역)
#    |-----OOO*-----|
#    promising 한 점들 중 최 좌측의 위치를 'idx'라 하고, target의 좌표를 'idx2' 라 하자.
#    idx를 1씩 증가시키며 save[idx2][0] 과 save[idx][0] 을 서로 비교하여 [idx:idx2] 구간이 promising 하게 만드는 idx를 찾는다.
# 5. y좌표는 정렬되어있지 않기 때문에 linear search로 promising 여부를 판단해야 하는데, 이 경우 시간초과가 발생한다. log(N) time 으로 줄일 수 있어야 한다.
#    y축에 대한 promising 여부를 빠르게 측정하기 위해, X축에서 promising 한 대상을 뽑아 새로운 배열을 만들고, Y축에 대해 정렬되도록 한다. (이하 배열 'promising')
#    (이후, 'promising' 배열에 item을 추가할 때 정렬이 유지되도록 index를 정해서 추가해야 시간이 절약된다)
#    추출한 'promising' 배열에 대해서 이분검색으로 lower bound / upper bound를 추출하여 y좌표상 promising 한 대상들만 거리 계산을 수행한다. 
# 6. target(save[idx2])을 promising pool에 집어넣고, idx2는 1 증가시킨다. (target = save[idx2] -> save[idx2+1]) 
#    그 후 [idx:idx2] 구간 중, 'target' 과 x축을 비교해 promising 하지 않은 점들은 'promising' 배열에서 제거한다.(promising pool 갱신)
#    'promising' 배열을 모두 순회하며 확인 할 수도 있지만, 이 경우 linear search를 하기 때문에 시간이 초과된다.
#    'promising' 배열에서 제거할 좌표를 찾는 것도 log(N) 시간 안에 수행되어야 하므로 binary search를 이용한다.
# 7. 최소값 'min_d'를 갱신하며 4~6 과정을 반복한다. 

# 알고리즘 키워드
# sweep line algorithm
# binary search, lower_bound / upper_bound
# 적합한 자료구조 찾기 
# - O(1) 만에 item 접근이 가능하고 정렬된 경우 이분탐색이(log(n)) 가능한 자료구조가 필요했다. 
# - https://stackoverflow.com/questions/3099383/can-bisect-be-applied-using-dict-instead-of-lists


# 개선과정
# - pow / sqrt 연산이 많아지면 시간초과가 발생한다. promising 관리가 필수
# - X좌표 뿐 아니라 Y좌표의 promising도 판단해야 한다.
# - X축에 대해서는 bisect 로 이분탐색 연산을 이용하여 연산시간을 최적화 한다.
# - 

DEBUG = 0

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

# 이분탐색
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


if __name__ == "__main__":
    N = int(input())
    save = [0 for _ in range(N)]
    for i in range(N):
        x, y = map(int, input().split())
        save[i] = (x, y)

    # remove duplicated point
    save = set(save)
    unique_N = len(save)
    save = list(save)
    # sort 'save' by 'x'
    save.sort(key=operator.itemgetter(0, 1))  # REF: 0번 index 우선 정렬, 이후 0번 index 정렬. lambda x: (x[0], x[1]) 보다 함수호출이 적어 빠름 (https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes)
    Print(save)

    # exception, if no more than two unique points
    if unique_N < 2:
        print(0)
        exit(0)
    
    idx = 0 # index of promising pool's head
    idx2 = 2  # index of target point
    
    promising = dict()
    promising[0] = save[0]
    promising[1] = save[1] # push item to promising pool
    sorted(promising.items(), key=lambda x: x[1][1])  # y축에 대해 정렬
    # REF: sorted의 return은 list형태이다. 
    # promising = save[idx:idx2]. I will remove add add promising point by moving 'idx' and 'idx2'
    powed_min_dist = distance_square(save[0], save[1])  # get distance of first two points
    min_dist = sqrt(powed_min_dist)
    Print(f'init state : {save[0]}, {save[1]} / min_disit={powed_min_dist}')
    # initialization done.

    # for all elements in 'save', compare x-axis distance between the element and 'target'
    while idx2 < unique_N:
        if powed_min_dist == 0:# 0 is the shortest length, no need to find more
            break
        # filter out non-prospective elements by comparing 'minimun-length' & 'x-axis distance'
        target = save[idx2]
        x, y = target
        print(promising)
        while idx < idx2:
            if abs(x - save[idx][0]) >= min_dist:
                # check 'x' axis and remove unpromising points
                del promising[idx]
                Print(f'Delete idx{idx}, promising:{len(promising)}')
                idx += 1
            else:
                break  # if 'idx' is promising, 'idx + a' will promising too

        # now, save[idx:idx2] is promising

        lower_bound = bisect_right(promising.items(), y - min_dist, key=operator.itemgetter(1)) # find lower bound
        upper_bound = bisect_right(promising.items(), y + min_dist, key=operator.itemgetter(1)) # find upper bound
        # REF: pair 를 bisect로 비교하는 방법 (https://stackoverflow.com/questions/20908047/using-bisect-in-a-list-of-tuples)

        # filter promising points by 'y' axis distance
        Print(f'idx:{idx}, idx2:{idx2}, minY:{y-min_dist}, maxY:{y+min_dist}')
        # check distance from all 'promising point' to 'target'
        for i in range(lower_bound, upper_bound):
            # check distance and update min_dist
            dist = distance_square(promising.items()[i], target)
            powed_min_dist = min(powed_min_dist, dist)  # update powed_min_dist
            min_dist = sqrt(powed_min_dist)  # update min_dist
                

            Print(f'[{lower_bound}:{upper_bound}] i={i}, p1:{promising.items()[i]}, p2:{target}, dist:{dist}/{powed_min_dist}')
            # Print(f'{promising}')
        # add 'target' to promising pool and increase index to find next target
        index_to_insert = bisect_right(promising.items(), save[idx2][1], key=lambda x: x[1][1]) # find index to insert save[i] on 'promising' while not breaking 'y' axis arrangement
        promising.items().insert((index_to_insert, save[idx2]))  # REF: https://stackoverflow.com/questions/44390818/how-to-insert-key-value-pair-into-dictionary-at-a-specified-position
        idx2 += 1

    # print result
    print(powed_min_dist)