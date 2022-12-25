MAX_N = 100000
MIN_NUM = -100
MAX_NUM = 100

N, K = map(int, input().split())
temperature = list(map(int, input().split()))

# [i, i+K) 구간의 배열 인자를 더한 값을 구하고, 모든 i에 대해(0~N) 구한 값을 비교하여 최대값 선정
# 초기값 세팅
start = 0
end = start + K - 1
max_result = sum(temperature[start:end+1])
current_result  = sum(temperature[start:end+1])

while end < N-1:
    current_result = current_result - temperature[start] + temperature[end+1]
    # print(max_result, current_result)
    max_result = max(max_result, current_result)  # 다음 값과 비교
    start += 1
    end += 1
print(max_result)

