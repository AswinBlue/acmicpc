import heapq

def distance(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2

if __name__ == "__main__":
    N = int(input())

    save = [0] * N
    for i in range(N):
        x, y = map(int, input().split())
        save[i] = tuple((x, y))
        
    # sort 'save' by 'x'
    heapq.heapify(save)

    result = distance(save[0], save[1])
    available = []
    idx = 0
    
    # add save[0], save[1] to 'available'
    heapq.heappush(available, save[0][::-1]) # to make heap with 'y', reverse tuple
    heapq.heappush(available, save[1][::-1])

    pointA = 0

    for pointB in range(2, N):
        x1, y1 = save[pointB]

        while pointA < pointB:
            x2, y2 = save[pointA]
            # check 'pointA' is qualified in regard of 'x'
            if (x2 - x1) ** 2 > result: 
                # if not qualified, check next
                heapq.heappop(available)
                pointA += 1
            # if qualified, go to  next step
            else:
                break

        # check 'pointA' is qualified in regard of 'y' 
        diff = int(result ** 0.5) + 1
        y_start = 0
        size = len(available) - 1

        while available[y_start][0] <= pointB - diff and y_start < size:
            y_start += 1 

        y_end = y_start
        while available[y_end][0] < pointB + diff and y_end < size:
            y_end += 1 

        # for all 'point' in y_start <= 'point' < y_end, recalculate 'result'
        for i in range(y_start, y_end):
            diff = distance(available[i][::-1], save[pointB])
            if (diff < result):
                result = diff

    # print result
    print(result)



