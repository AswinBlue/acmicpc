# https://www.acmicpc.net/problem/2261
# 가장 가까운 두 점

def distance_square(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2

DEBUG = 0

if __name__ == "__main__":
    N = int(input())

    save = [0] * N
    for i in range(N):
        x, y = map(int, input().split())
        save[i] = tuple((x, y))

    # sort 'save' by 'x'
    save.sort(key=lambda e: e[0])
    if DEBUG: print(save)

    # set pointA
    idx = 0
    pointA = save[idx]
    x1, y1 = pointA

    # find another point and set pointB
    for i in range(N):
        if save[0] != save[i]:
            idx2 = i
            pointB = save[idx2]
            break

    available = [pointA, pointB]
    min_dist = distance_square(pointA, pointB)

    # for all elements in 'save', compare x-axis distance between two point
    # filter out non-prospective elements by comparing 'minimun-length' & 'x-axis distance'
    # use sweep line algorithm
    while idx2 < N:
        pointB = save[idx2]
        x2, y2 = pointB
        dist = distance_square(pointA, pointB)
        # if distance is 0, 'pointA' & 'pointB' is same point
        if DEBUG:
            print(idx, idx2, x1, y1, x2, y2)
        if dist == 0:
            idx2 += 1
            continue
        min_dist = min(min_dist, dist)

        if DEBUG:
            print(dist, min_dist, "\n", available)
        if (x2 - x1) ** 2 <= min_dist:
            available.append(save[idx2])
            idx2 += 1
        else:
            idx += 1
            pointA = save[idx]

    # print result
    print(min_dist)



