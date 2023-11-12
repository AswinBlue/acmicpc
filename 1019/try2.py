# https://www.acmicpc.net/problem/1019
# 책 페이지

# 폐기 원인 : R[i] 는 R[i-1]과의 연관성을 가지게 점화식을 만들어야하는데 점화식을 잘못 만들었다.


# 전체 페이지를 N 이라 하고, N의 각 자릿수를 n_1, n_2, n_3 ... n_x 라 칭하겠다.(N은 x자리의 수, ex: 123 -> n_3 = 1, n_2 = 2, n_1 = 3)
# Q[i][j] 는 10**i 보다 작은 모든 자연수에서 j가 들어있는 갯수라 하자. (i > 1)
# -> Q[0][j] = 0 (initialize)
# -> Q[1][j] = 1
# -> Q[2][j] = (1 * 10) + 10 = 20
# -> Q[3][j] = (20 * 10) + 100 = 300
# -> Q[i][j] = Q[i-1] * 10 + 10**(i-1)
# 단, j==0일 땐 식이 아래와 같다.
# -> Q[i][0] = 10**(i-1) -1

# R[i][j] = N을 i자리까지만 포함해서 자른 수를 마지막 장으로 하는 책에 들어있는 숫자 j의 갯수라 할 때
# R[i][j] = Q[i-1][j] * n_i + (if n_i == j : R[i-1][j] : 0)

DEBUG = 1
def Print(*args):
    if DEBUG:
        print(*args)

MAX_N = 1_000_000_000
MAX_LEN = 10

# N의 길이를 구하는 함수
def get_length(N):
    temp = N
    length = 0 # N의 길이
    while temp > 0:
        temp = temp // 10
        length += 1
    return length

# N을 자리수마다 나누어 배열로 만드는 함수
def split_N(N):
    array = [0]
    temp = N
    while temp > 0:
        array.append(temp % 10)
        temp = temp // 10
    Print(array)
    return array



# 배열 Q 를 초기화하여 반환하는 함수
#  x : N의 길이
def init_Q(x):
    Q = [[0 for _ in range(10)] for _ in range(x+1)] # x by 10 짜리 2차원 배열
    for i in range(1, x+1):
        for j in range(10):
            if j == 0:
                Q[i][j] = 10**(i-1) -1 # 0은 1자리수에서 사용 불가능하여 1 빼주고, 제일 앞자리가 0으로 시작할 수 없기에 식이 다름
            else:
                Q[i][j] = Q[i-1][j] * 10 + 10**(i-1)
    Print(Q)
    return Q

N = int(input())
R = [[0 for _ in range(10)] for _ in range(MAX_LEN + 1)] # 각 숫자가 몇번 나왔는지 결과를 저장할 배열
length = get_length(N)  # N이 몇자리 수인지 구하기
Q = init_Q(length)  # 초기값 세팅
X = split_N(N)

# 점화식을 위해 초기값 세팅
for i in range(10):
    R[0][i] = 1

# 결과 계산
for i in range(1, length+1):
    for j in range(10):
        R[i][j] = Q[i-1][j] * X[i]
        if X[i] == j:
            R[i][j] += R[i-1][j]  # 점화식 초기세팅 R[0][i] = 1 이 적용되는 부분
    Print(f'R[{i}] : {R[i]}')

'''


for j in range(10):
    if X[1] >= j:  # 첫번째 자리 계산
        R[j] += 1
    for i in range(2, length+1):  # 2~마지막 자리까지 계산
        Print(f'i:{i}, R[{j}]:{R[j]}, add:{Q[i-1][j] * X[i]}')
        R[j] += Q[i-1][j] * X[i]
'''

# 모든 자리 수에대해 반복하고 나면 R[i]에는 전체 페이지 중 i가 등장한 횟수가 기록되어 있다. 결과를 출력한다.
for k in range(10):
    print(R[length][k], end=' ')