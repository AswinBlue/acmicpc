# 울타리
# https://www.acmicpc.net/problem/1047

from bisect import bisect_left, bisect

DEBUG = 0
def Print(*arg):
    if DEBUG:
        print(*arg)

MAX_N = 40
MIN_N = 2
MAX_VALUE = 1_000_000

def solve(x1, x2, y1, y2):
    global N, max_chopped_tree, x_sorted, y_sorted, v_sorted
    
    # 울타리의 경계지점 좌표를 확보
    left_x =  min(x1,x2)
    right_x = max(x1,x2)
    down_y = min(y1,y2)
    up_y =  max(y1,y2)

    # 배열에서 경계지점에 포함되는 index를 찾는다. 
    # 문제에서는 중복된 x,y값이 없다고 했는데 중복되는 값이 있을 경우에도 동작되도록 짜본다.
    idx_left_x = bisect_left(x_sorted, left_x, key= lambda x : x[X])
    idx_right_x = bisect(x_sorted, right_x, key= lambda x : x[X]) - 1
    idx_down_y = bisect_left(y_sorted, down_y, key= lambda x : x[Y])
    idx_up_y = bisect(y_sorted, up_y, key= lambda x : x[Y]) - 1
    
    # 울타리에서 벗어나는 나무들을 잘라낸다.
    # 잘라낸 나무의 index 저장
    is_chopped = [0 for _ in range(N)]
    # 잘라낸 나무의 수 저장
    tree_to_chop = 0
    # 나무를 잘라서 획득한 목재
    lumber = 0
    # 울타리 설치에 필요한 목재
    required_lumber = (abs(x2 - x1) + abs(y2 - y1)) * 2

    Print(f"X:{idx_left_x} ~ {idx_right_x}, Y:{idx_down_y} ~ {idx_up_y}")

    # x 배열상 잘라내야하는 나무 체크
    for t in range(0, idx_left_x):
        if is_chopped[x_sorted[t][INDEX]] == 0:
            # 이미 잘렸는지 체크 후 처리
            is_chopped[x_sorted[t][INDEX]] = 1
            lumber += x_sorted[t][VALUE]
            tree_to_chop += 1

    for t in range(idx_right_x + 1, N):
        if is_chopped[x_sorted[t][INDEX]] == 0:
            # 이미 잘렸는지 체크 후 처리
            is_chopped[x_sorted[t][INDEX]] = 1
            lumber += x_sorted[t][VALUE]
            tree_to_chop += 1

    # y 배열상 잘라내야하는 나무 체크
    for t in range(0, idx_down_y):
        if is_chopped[y_sorted[t][INDEX]] == 0:
            # 이미 잘렸는지 체크 후 처리
            is_chopped[y_sorted[t][INDEX]] = 1
            lumber += y_sorted[t][VALUE]
            tree_to_chop += 1

    for t in range(idx_up_y + 1, N):
        if is_chopped[y_sorted[t][INDEX]] == 0:
            # 이미 잘렸는지 체크 후 처리
            is_chopped[y_sorted[t][INDEX]] = 1
            lumber += y_sorted[t][VALUE]
            tree_to_chop += 1

    Print(f"chopped_tree:{tree_to_chop}, lumber:{lumber}/{required_lumber}")

    # 목재가 충분하지 않다면 목재가 많이 나오는 나무부터 하나씩 잘라봄
    for t in range(N):
        # 울타리 생성 조건이 충분하다면 통과
        if required_lumber <= lumber:
            break

        if is_chopped[v_sorted[t][INDEX]] == 0:
            # 아직 자르지 않은 나무에 대해서만 처리
            is_chopped[v_sorted[t][INDEX]] = 1
            lumber += v_sorted[t][VALUE]
            tree_to_chop += 1

    # 나무를 다 잘라도 모자라면 pass
    if required_lumber > lumber:
        return

    # 최종 값 비교
    if tree_to_chop < max_chopped_tree:
        max_chopped_tree = tree_to_chop


if __name__ == '__main__':
    X = 0
    Y = 1
    VALUE = 2
    INDEX = 3

    N = int(input())
    x_sorted = [None for _ in range(N)]
    v_sorted = [None for _ in range(N)]
    y_sorted = [None for _ in range(N)]
    x_left = x_right = 0
    y_left = y_right = 0
    v_right = 0

    for n in range(N):
        x,y,v = map(int, input().split())
        tree = [x,y,v,n]  # x좌표, y좌표, 울타리 재료 양, index
        x_sorted[x_right] = tree
        x_right += 1
        y_sorted[y_right] = tree
        y_right += 1
        v_sorted[v_right] = tree
        v_right += 1


    # 나무의 속성을 배열로 구성하였다. 배열은 mutable 객체이므로 x_sort[] 와 y_sort[] 는 동일한 객체의 주소를 참조하도록 설정된다. 
    x_sorted = sorted(x_sorted, key=lambda t : t[0])  # REF: python sorting
    y_sorted = sorted(y_sorted, key=lambda t : t[1])
    v_sorted = sorted(v_sorted, key=lambda t : t[2], reverse=True)

    Print(f"{x_sorted}\n{y_sorted}\n{v_sorted}")

    x_right = y_right = N - 1  # 시작 위치 세팅

    max_chopped_tree = MAX_N  # 최대 벌목한 나무

    # 임의의 두 X좌표 x1,x2(x1==x2일 수 있다) 에 대해 
    for i in range(N):
        x1 = x_sorted[i][X]
        for j in range(i, N):
            x2 = x_sorted[j][X]
            # 임의의 두 Y좌표 y1,y2(y1==y2일 수 있다) 에 대해 
            for k in range(N):
                y1 = x_sorted[k][Y]
                for l in range(k, N):
                    y2 = x_sorted[l][Y]
                    solve(x1, x2, y1, y2)

    print(max_chopped_tree)

