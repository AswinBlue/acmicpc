if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        k = int(input())
        n = int(input())

        house = [i for i in range(n + 1)]
        # print(house)
        for floor in range(1, k + 1):
            floor_sum = 0
            for room in range(n + 1):
                # print(floor, room)
                floor_sum += house[room]
                house[room] = floor_sum
        print(house[n])



