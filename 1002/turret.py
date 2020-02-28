import math

if __name__ == '__main__':
    t_case = int(input())

    for i in range(t_case):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        dist = math.sqrt(math.pow(x1 - x2,2) + math.pow(y1 - y2,2))
        if dist == 0 and r1 == r2:
            if r1 > 0:
                print(-1)
            elif r1 == 0:
                print(1)
        elif dist == 0 and r1 != r2:
            print(0)
        # independent two circle / circle in the other circle
        # 이거해서 틀렸음 : r1 + r2 > dist > max(r1, r2) or max(r1, r2) > dist > abs(r1 - r2):
        elif r1 + r2 > dist > abs(r1 - r2):
            print(2)
        # circumscribe & inscribe
        elif dist == r1 + r2 or dist == abs(r1 - r2):
            print(1)
        # independent two circle / circle in the other circle
        elif dist > r1 + r2 or dist < abs(r1 - r2):
            print(0)