# https://www.acmicpc.net/problem/1019
# 책 페 이지

# 전체 페이지를 N 이라 하고, N의 각 자릿수를 n_1, n_2, n_3 ... n_x 라 칭하겠다.(N은 x자리의 수, ex: 123 -> n_3 = 1, n_2 = 2, n_1 = 3)
# Q[i][1] 는 10**i 보다 작은 모든 자연수에서 j가 들어있는 갯수라 하자. (i > 1)
# -> Q[0][1] = 0 (initialize)
# -> Q[1][1] = 1  # 1의자리count
# -> Q[2][1] = (1 * 10) + 10 = 20  # 1의자리count + 10의자리count
# -> Q[3][1] = (20 * 10) + 100 = 300  # 1,10의자리count + 100의자리count
# -> Q[i][1] = Q[i-1] * 10 + 10**(i-1)  # 1~(i-1)의자리count + i의자리count
# 단, j==0 인 경우는 식이 아래와 같다. (i자리보다 윗자리가 모두 0인경우, i에 0이 들어오는 경우를 count를 하면 안되기 때문)
# -> Q[1][0] = 0  # (0단독은 자연수 아님)
# -> Q[2][0] = 1*(10-1) = 9  # 1의자리count(10의자리가 0인 case 제외)
# -> Q[3][0] = 10*(10-1) + 1*(10*10-1) = 189 # 10의자리count(100의자리가 0인case 제외) + 1의자리count(100,10의자리가 모두 0인 case 제외)
# -> Q[4][0] = 100*(10-1) + 10*(10*10-1) + 1*(10*10*10-1) = 189 # 100의자리count(1000의자리가 0인 case 제외) + 10의자리count(1000,100의자리가 0인case 제외) + 1의자리count(1000,100,10의자리가 모두 0인 case 제외)
# -> Q[i][0] = (10**(i-2-k) * (10**(k+1) -1)) for k in range(i-1)
'''
N=999일때 0의갯수
1의자리
10 20 30 40 50 60 70 80 90
100 110 120 130 140 150 160 170 180 190
...
900 910 920 930 940 950 960 970 980 990
-> 99 = 10 * 10 - 1 = (n_i + 1) * 10 - 1
10의자리
100 101 102 103 104 105 106 107 108 109 
200 201 202 203 204 205 206 207 208 209 
...
900 901 902 903 904 905 906 907 908 909
-> 90 = 9 * 10 = n_i * 10
'''
# R[i][j] = N을 i자리까지만 포함해서 자른 수를 마지막 장으로 하는 책(N % 10**i)에 들어있는 숫자 j의 갯수라 할 때,
# i == length 이면서 j == 0이라면
# R[i][j] = Q[i-1][1] * (n_i - 1)       # i 위치에 1 ~ n_i-1 수가 오는 경우, 1 ~ i-1자리의 위치에서 나오는 '0'의 갯수
#            + Q[i-1][0]                # i 위치에 0이 오는 경우, 1 ~ i-1자리의 위치에서 나오는 '0'의 갯수
#            + R[i-1][0]                # i 위치에 n_length 가 오는 경우, 1 ~ i-1자리의 위치에서 나오는 '0'의 갯수
# 그 외에는
# R[i][j] = Q[i-1][j] * n_i + R[i-1][j]   # 1 ~ i-1자리의 위치에서 나오는 'j'의 갯수
#          + (
#               if n_i == j : n_i-1~n_1 + 1  # i자리에서 나오는 j의 갯수, j가 n_i라면 N을 i-1번째 자리까지 잘라서 만든 수 + 1
#               elif n_i < j : 0             # j가 n_i보다 작으면 0개
#               elif n_i > j : 10**(i-1)     # j가 n_i보다 크면 10**(i-1)개
#            )
# R[0][j] = 1

DEBUG = 0
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
    return array

# 배열 Q 를 초기화하여 반환하는 함수
#  x : N의 길이
def init_Q(x):
    Q = [[0 for _ in range(2)] for _ in range(x+1)] # x by 10 짜리 2차원 배열
    for i in range(1, x+1):
        for j in range(2):
            if j == 0:
                for k in range(i-1):
                    Q[i][j] += (10**(i-2-k) * (10**(k+1) -1)) 
            else:
                Q[i][j] = Q[i-1][j] * 10 + 10**(i-1)
    return Q

if __name__ == '__main__':
    # 초기화 및 사전 준비
    N = int(input())
    R = [[0 for _ in range(10)] for _ in range(MAX_LEN + 1)] # 각 숫자가 몇번 나왔는지 결과를 저장할 배열
    length = get_length(N)  # N이 몇자리 수인지 구하기
    Q = init_Q(length)  # 초기값 세팅
    Print(f'Q : {Q}')
    X = split_N(N)
    Print(f'X : {X}')

    # 결과 계산
    num = 0  # N을 i-1번째 자리까지 잘라서 만든 수, i==1일때만 예외적으로 1
    for i in range(1, length+1):  # 1~length 까지 i 순회
        for j in range(10):  # 0~9까지 j 순회
            # if i == 1 and j == 0:  # 0 단독으로는 자연수가 아니므로 예외
            #     continue
            if i == length and j == 0:  # 0은 첫번째 자리에 오는 경우는 예외적이다.
                # 1 ~ i-1자리 에서 발생하는 0의 갯수 count
                # i번쨰 자리가 1~n_i 일 때 0의 의 갯수
                R[i][j] += Q[i-1][1] * (X[i] - 1) + R[i-1][j]  # i==length이므로 X[i] == 0 이 될 수 없음 보장됨
                # i번째 자리가 0일때 0의 갯수
                R[i][j] += Q[i-1][0]
            else:
                # 1 ~ i-1자리 에서 발생하는 j의 갯수
                R[i][j] += Q[i-1][1] * X[i] + R[i-1][j]
                # i번째 자리에서 발생하는 j의 갯수
                if X[i] == j:
                    R[i][j] += (num + 1) # 0 ~ num 까지의 갯수
                elif X[i] > j:
                    R[i][j] += 10**(i-1)
                else:  # X[i] < j
                    continue  # i자리에서는 j 이상의 수가 나타나지 않음

        num += X[i] * (10**(i-1))  # 다음 cycle을 위해 num 갱신

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