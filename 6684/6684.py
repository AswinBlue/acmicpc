# https://www.acmicpc.net/problem/6684
# Hexagonal Routes

# axis x: ↘
# axis y: ↗
# axis z: ↑
class Coordinate:
    x = 0
    y = 0
    z = 0


if __name__ == "__main__":
    while True:
        a, b = map(int, input().split())

        if a == 0 and b == 0:
            break

        # To make 'b' bigger than 'a'
        if a > b:
            cnt = a
            a = b
            b = cnt

        # Σi = p
        # 6 * p + 1 = 1,7,19, ... (cells under 'number 1' cell)
        # i_a will be distance from cell 1 to cell a
        # p_a will be biggest number cell which has same distance (from 1 to the cell) with a
        # i_b, p_b are same as above

        i_a = p_a = p_b = i_b = 0

        while (6 * p_a + 1) < a:
            i_a += 1
            p_a = p_a + i_a

        while (6 * p_b + 1) < b:
            i_b += 1
            p_b = p_b + i_b

        p_a = 6 * p_a + 1
        p_b = 6 * p_b + 1

        # calculate coordination of a
        diff = p_a - a

        # divide by 0 exception
        if i_a != 0:
            cnt = int(diff / i_a)
        else:
            cnt = 0

        A = Coordinate()
        A.x = 0
        A.y = 0
        A.z = -i_a

        if cnt == 0:
            # divide by 0 exception
            if i_a != 0:
                A.y += (diff % i_a)

        elif cnt > 0:
            A.y += i_a
            cnt -= 1

            if cnt == 0:
                A.z += (diff % i_a)

            elif cnt > 0:
                A.z += i_a
                cnt -= 1

                if cnt == 0:
                    A.x -= (diff % i_a)

                elif cnt > 0:
                    A.x -= i_a
                    cnt -= 1

                    if cnt == 0:
                        A.y -= (diff % i_a)

                    elif cnt > 0:
                        A.y -= i_a
                        cnt -= 1

                        if cnt == 0:
                            A.z -= (diff % i_a)

                        elif cnt > 0:
                            A.z -= i_a
                            cnt -= 1

                            if cnt == 0:
                                A.x += (diff % i_a)

        # calculate coordination of b
        diff = p_b - b

        # divide by 0 exception
        if i_b != 0:
            cnt = int(diff / i_b)
        else:
            cnt = 0

        B = Coordinate()
        B.x = 0
        B.y = 0
        B.z = -i_b

        if cnt == 0:
            # divide by 0 exception
            if i_b != 0:
                B.y += (diff % i_b)

        elif cnt > 0:
            B.y += i_b
            cnt -= 1

            if cnt == 0:
                B.z += (diff % i_b)

            elif cnt > 0:
                B.z += i_b
                cnt -= 1

                if cnt == 0:
                    B.x -= (diff % i_b)

                elif cnt > 0:
                    B.x -= i_b
                    cnt -= 1

                    if cnt == 0:
                        B.y -= (diff % i_b)

                    elif cnt > 0:
                        B.y -= i_b
                        cnt -= 1

                        if cnt == 0:
                            B.z -= (diff % i_b)

                        elif cnt > 0:
                            B.z -= i_b
                            cnt -= 1

                            if cnt == 0:
                                B.x += (diff % i_b)

        # calculate distance
        X = A.x - B.x
        Y = A.y - B.y
        Z = A.z - B.z

        # make sum of absolute X,Y,Z the smallest
        # use these rules
        # (-n,n,0) = (0,0,n)
        # (n,0,n) = (0,n,0)
        # (0,-n,-n) = (n,0,0)

        # (-n,n,0) = (0,0,n)
        if (X < 0 and Y > 0) or (X > 0 and Y < 0):
            if abs(X) > abs(Y):
                if Y > 0:
                    Z += abs(Y)
                else:
                    Z -= abs(Y)
                X += Y
                Y = 0

            else:
                if X < 0:
                    Z += abs(X)
                else:
                    Z -= abs(X)
                Y += X
                X = 0

        # (n,0,n) = (0,n,0)
        if (X > 0 and Z > 0) or (X < 0 and Z < 0):
            if abs(X) > abs(Z):
                if Z > 0:
                    Y += abs(Z)
                else:
                    Y -= abs(Z)
                X -= Z
                Z = 0

            else:
                if X > 0:
                    Y += abs(X)
                else:
                    Y -= abs(X)
                Z -= X
                X = 0

        # (0,n,-n) = (n,0,0)
        if (Y > 0 and Z < 0) or (Y < 0 and Z > 0):
            if abs(Y) > abs(Z):
                if Z < 0:
                    X += abs(Z)
                else:
                    X -= abs(Z)
                Y += Z
                Z = 0

            else:
                if Y > 0:
                    X += abs(Y)
                else:
                    X -= abs(Y)
                Z += Y
                Y = 0

        length = abs(X) + abs(Y) + abs(Z)
        route = 1
        denominator = 1

        # route = length ! / (X! * Y! * Z!)
        for i in range(2, length + 1):
            route *= i

        for i in range(abs(X), 1, -1):
            route = int(route / i)

        for i in range(abs(Y), 1, -1):
            route = int(route / i)

        for i in range(abs(Z), 1, -1):
            route = int(route / i)

        print("There is " + str(route) + " route of the shortest length " + str(length) + ".")