# https://www.acmicpc.net/problem/1019
# 책 페이지

# 폐기원인: 재귀를 통해 해결하려 접근하였으나 재귀식을 잘못 짠 case, 재귀식이 너무 복잡하고 예외도 많았다. 


# 길이가 i이면서 i번쨰 자리에 숫자가 j이고 나머지 자릿수는 모두 0인 수를 M이라 하자. (ex: 10, 3000, 5, 90000)
# P[i][j] 는 M 보다 작은 수에서 i번쨰 자리에 j가 되는 수의 갯수라 하자. (0 <= j <= 9)
# 전체 책에서 볼 수 있는 번호 j의 갯수 R[j] 를 구해야 한다. (0 <= j <= 9)
# 전체 페이지를 N 이라 하고, N의 각 자릿수를 n_1, n_2, n_3 ... n_x 라 칭하겠다.
# 그러면 R[j] = P[1][n_1] + p[2][n_2] + ... p[x][n_x] 가 성립한다.
# P[i][j] 는 j <= x 일 떄 1, j > x 일때 0이다. 
# 
# 예를들어 x = 5이면서 n_1 = e, n_2 = d, n_3 = c, n_4 = b, n_5 = a 인 수 abcde 에 대해 R을 계산해 보면
# R[j] = P[1][j]
#       + P[2][j] + 10^0 * d
#       + P[3][j] + (10^1 + 10^0) * c
#       + P[4][j] + (10^2 + 10^1 + 10^0) * b
#       + P[5][j] + (10^3 + 10^2 + 10^1 + 10^0) * a 가 된다.
#      = P[1][j]
#       + P[2][j] + 1 * d
#       + P[3][j] + 11 * c
#       + P[4][j] + 111 * b
#       + P[5][j] + 1111 * a 가 된다.
# 단, j==0인 경우 P[i][0] == 0 임에 주의한다.

# 자릿수를 하나씩 늘려가며 계산하는 방식으로 계산한다면 R[]을 구할 수 있다.

DEBUG = 1
def Print(*args):
    if DEBUG:
        print(*args)

MAX_N = 1_000_000_000

# P[i][j]를 구하는 함수
# N을 i번째 자리까지 자 수 M에 대해, M의 i번쨰 자리에 j가 오는 경우의 수를 구함
def get_p(N, i, j):
    
    n = 10**(i-1)  # i번쨰 자리 수를 구하기위한 변수
    num = (N // n) % 10 # i번쨰 자리의 수
    res = None

    # 0이 가장 처음 오는 경우는 없기 때문에 0을 반환
    if j == 0: 
        res = 0
    elif j < num:
        res = 1
    elif j > num:
        res = 0
    else: # j == num
       res = N % n + 1 # 0 ~ (N%n) 까지 수의 갯수

    Print(f'P[{i}][{j}]:{res}')    
    return res


N = int(input())
# 1. 초기값 세팅
R = [0 for _ in range(10)] # 각 숫자가 몇번 나왔는지 결과를 저장할 배열

# 2. N이 몇자리 수인지 구하기
temp = N
length = 0 # N의 길이
while temp > 0:
    temp = temp // 10
    length += 1

# 3.아랫 자릿수부터 반복하여 result 값 구하기
temp = N
alpha = 0 # 자릿수가 늘어날 때 마다 P[i][j] 뒤에 더해지는 수 계산을 위한 변수
for i in range(1, length+1):
    num = temp % 10 # i번째 자리의 수
    temp = temp // 10 # 반복문을 위한 값 갱신
    if i > 1: # 둘쨰자리 이상부터 유효
        alpha += 10 ** (i-2)

    # R 값을 갱신해준다.
    for k in range(0, 10):
        current = get_p(N, i, k) + alpha * (num) # (M의 i번째 자리에 k가 나올 확률) + (M에서 10^(i-1) 이하 수에서 k가 나올 확률)
        R[k] += current
        Print(f'i:{i} k:{k} num:{num} current:{current} R[{k}]:{R[k]}')
    Print('- - - - -')
# 4. 모든 자리 수에대해 반복하고 나면 R[i]에는 전체 페이지 중 i가 등장한 횟수가 기록되어 있다. 결과를 출력한다.
for k in range(10):
    print(R[k], end=' ')