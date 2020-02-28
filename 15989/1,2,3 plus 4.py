# <1차시도>
# 어떤 수 x를 1,2,3의 조합으로 나타낸 방법을 나열한 것을 f(x)라 하자.
# 이때 6 이상의 수, 즉 1,2,3이 한번 이상씩 나올 수 있는 숫자n에 대해 f(n+3)과 f(n+2)의 차이는 다음과 같다.
# 1) 기본적으로 f(n+3) = f(n+2) + 1 (<f(n+2)에 1을 더 붙인 것> + <1을 사용하지 않고 이루어진 수>)
# 2) n+3이 2의 배수이면 +1 (2로만 이루어진 수 추가)
# 3) n+3이 3의 배수이면 +1 (3으로만 이루어진 수 추가)
# <1차시도>
"""
for j in range(T):
    n = int(input())
    C = [0, 1, 2, 3, 4, 5, 7, 8]
    for i in range(8, n + 1):
        c = C[i-1] + 1
        if i%2 == 0:
            c+=1
        if i%3 == 0:
            c+=1
        C.append(int(c))
    print(C[n])
"""
# <2차시도>
# C[n] = C[n-1] + (C[n-2] - '1 이 하나라도 들어간 경우) + (C[-3] - '1이나 2가 하나라도 들어간 경우)
'''
T = int(input())
    for t in range(T):
        n = int(input())
        C = [0, 1, 2, 3]
        for i in range(4, n+1):
            result = C[i-1]
            # expressions without '1' in C[i-2]
            if (i-2) % 2 == 0:
                result += (C[i - 2] // 6) + 1
            elif (i-2) % 2 == 1:
                result += (C[i - 2] - 3) // 6 + 1

            # expressions without '1' and '2' in C[i-3]
            if (i-3) % 3 == 0:
                result += 1
            C.append(result)
        print(C[n])
'''
# <3차시도>
# BFS를 이용한 경우의 수 찾기, brute force
# 1) 1을 더할 수 있을 때까지 더한다.
# 2) 각각의 경우 2를 더할 수 있는 만큼 추가한다.
# 3) 또다시 3을 더할 수 있는 만큼 추가한다.
# ex) {1} {11} {111} ... {11111...}
# {12} {112} {1112} ... {2222}
# {123} {1123} {11123} ...

'''
def add1(cur, n):
    if cur == n:
        global result
        result += 1
        return True
    if cur > n:
        return False

    add1(cur + 1, n)
    add2(cur + 2, n)
    add3(cur + 3, n)

def add2(cur, n):
    if cur == n:
        global result
        result += 1
        return True
    if cur > n:
        return False

    add2(cur + 2, n)
    add3(cur + 3, n)


def add3(cur, n):
    if cur == n:
        global result
        result += 1
        return True
    if cur > n:
        return False

    add3(cur + 3, n)


if __name__ == '__main__':
    T = int(input())
    global result
    for t in range(T):
        result = 0
        n = int(input())
        add1(0, n)
        print(result)
'''
# <4차시도> recursion을 iteration으로 변환
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n = int(input())
        stack = []
        # fill stack with 1
        for i in range(n):
            stack.append(1)
        # pop 1 item from stack
        # if the item is 1, try to push 2 and 3
        # if the item is 2, try to push 3
        # if the item is 3, pop once again
        result = 1
        num = n
        while len(stack) > 0:
            item = stack.pop()
            if item == 1:
                num -= 1
                while num+2 <= n:
                    stack.append(2)
                    num += 2
                    if num == n:
                        result += 1
            elif item == 2:
                num -= 2
                while num+3 <= n:
                    stack.append(3)
                    num += 3
                    if num == n:
                        result += 1
            elif item == 3:
                num -= 3
                continue
        print(result)
'''
11
2

111
12
3


11111 11111
11111 1112
11111 113
11111 122
11111 23
11113 3
11112 22
11122 3
11233
1333
11222 2
12223
2233
22222

11111 1111
11111 112
11111 13
11111 22
11112 3
11133
11122 2
11223
1233
333
12222
2223

11111 111
11111 12
11111 3
11112 2
11123
1133
11222
1223
233
2222

11111 11
11111 2
11113
11122
1123
133
1222
223

11111 1
11112
1113
1122
123
33
222

11111
1112
113
122
23

'''