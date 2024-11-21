DEBUG = 0
MOD = 1_000_000_007


def Print(*args):
    if DEBUG:
        print(*args)


# 유니콘 이동 규칙에 따른 가능 경로 확인 함수
def check(x1, y1, x2, y2):
    return (abs(x1 - x2) > 2 and abs(y1 - y2) > 1) or (abs(x1 - x2) > 1 and abs(y1 - y2) > 2)


if __name__ == '__main__':
    N, M, L = map(int, input().split())
    word = list(input())
    
    board = [None for _ in range(N)]  # 알파벳을 기준으로 좌표 저장
    for n in range(N):
        board[n] = input()

    K = len(word)  # 단어 길이
    dp = [[[0] * M for _ in range(N)] for _ in range(K)]

    # 첫 글자의 모든 위치 초기화
    for i in range(N):
        for j in range(M):
            if board[i][j] == word[0]:
                dp[0][i][j] = 1

    # DP 진행
    for k in range(1, K):  # 단어의 두 번째 글자부터
        for i in range(N):  # 현재 좌표 (i, j)
            for j in range(M):
                if dp[k - 1][i][j] > 0:  # 이전 단계에서 도달 가능한 위치
                    for ni in range(N):  # 다음 좌표 (ni, nj)
                        for nj in range(M):
                            if board[ni][nj] == word[k] and check(i, j, ni, nj):
                                dp[k][ni][nj] = (dp[k][ni][nj] + dp[k - 1][i][j]) % MOD

    # 결과 계산
    result = 0
    for i in range(N):
        for j in range(M):
            result = (result + dp[K - 1][i][j]) % MOD

    print(result)
