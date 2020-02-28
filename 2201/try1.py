# https://www.acmicpc.net/problem/2201
# 이친수

# 2진트리를 구성하여 이친수를 찾는다. 2진수 중 2친수가 아닌 부분은 -1로 채운다.
def countPinary():
	K = int(input())
	pinary = [0, 1, 2, -1]

	# 예외처리
	if K < 3:
		print (pinary[K])
		return

	i = 2
	K -= 2
	while K > 0:
		i += 2
		current = pinary[i//2]
		if current <= 0:
			pinary.append(-1)
			pinary.append(-1)
			continue

		# 0을 추가
		pinary.append(current << 1)
		# K - 1 == 0 이면 break
		if K == 1:
			break

		# 1을 추가 
		# 1이 연속으로 오지 않도록 하는 로직
		if i % 2 == 0:
			pinary.append((current << 1) + 1)
		else:
			pinary.append(-1)

		K -= 2
		# print(pinary, K)

	print(pinary, pinary[len(pinary)-1])


if __name__ == '__main__':
	countPinary()
