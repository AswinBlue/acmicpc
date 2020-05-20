# 길이 2부터 시작, tree형태로 만들기 위해 길이 1인 경우는 제외
"""
                   1    <- 제거, 나중에 갯수 +1로 쳐주도록 하고 계산에서 제외
		          10    <- 길이 2인 수를 root로 depth가 이진수의 자릿수인 tree를 만들 수 있다.
		  100                101
	1000      1001      1010       X
10000 10001 10010 X  10100 10101  X  X
"""
cnt0 = [0, 1, 1, 2, 3] # cnt0[n] = cnt1[n-1] + cnt0[n-1]
cnt1 = [0, 0, 1, 1, 2] # cnt1[n] = cnt0[n-1]


def getCnt0(index):
	if len(cnt0) > index:
		return cnt0[index]
	else:
		cnt0.append(getCnt0(index - 1) + getCnt1(index - 1))
		return cnt0[index]


def getCnt1(index):
	if len(cnt1) > index:
		return cnt1[index]
	else:
		cnt1.append(getCnt0(index - 1))
		return cnt1[index]


def getCountByIndex(index):
	return getCnt0(index) + getCnt1(index)


if __name__ == "__main__":
	K = int(input())
	K -= 1 # 한 자리의 경우(1가지)를 제외했기 때문에 1을 빼줌

	depth = 1
	idx = 1
	while idx < K:
		depth += 1
		idx += getCountByIndex(depth)

	# depth는 K의 자릿수
	# getCountByIndex(depth) < K < index

	# 길이가 1 ~ depth-1 인 모든 이친수의 합
	sum_1_to_depth = 0
	for i in range(depth):
		sum_1_to_depth += getCountByIndex(i)

	# depth 레벨에서 K까지의 이친수 갯수
	K2 = K - sum_1_to_depth

	# 및변의 길이(leaf node의 갯수)가 K2보다 작은 subtree의 depth
	depth2 = 1
	while getCountByIndex(depth2) < K2:
		depth2 += 1
	depth2 -= 1

	# 1에서 depth-1 레벨까지 이친수가 아닌 수의 갯수, binary tree에서 pinary 들을 뺀다.
	non_pinary = 0
	for i in range(1, depth):
		non_pinary += 2 ** (i - 1)

	non_pinary -= getCountByIndex(depth)

	# depth 레벨에서 K 까지의 이친수가 아닌 수의 갯수
	non_pinary2 = 2 ** (depth2 - 1) - getCountByIndex(depth2)

	if non_pinary < 0:
		non_pinary = 0
	if non_pinary2 < 0:
		non_pinary2 = 0

	# 이친수와 이친수가 아닌 수를 모두 포함했을 때 K의 위치(index)
	K3 = K + int(non_pinary) + int(non_pinary2)


	# 결과값 도출

	if K == 0: # 1은 유일한 한자리 수, 한 자리수는 예외로 처리한다.
		print(1)
	else:
		result = []
		while K3 > 1:
			if K3 % 2 > 0:
				result.insert(0,1)
			else:
				result.insert(0,0)
			K3 //= 2
		print(10,end='') # 시작점이 10이므로 결과 출력시 앞에 붙여준다.
		for i in result:
			print(i,end='')
		print()
	
