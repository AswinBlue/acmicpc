# https://www.acmicpc.net/problem/2201
# 이친수

if __name__ == '__main__':
	K = int(input())
	arr = [1]
	idx = 1
	while idx < K:
		# 뒤에 0 붙이기
		arr.append(arr[0] << 1)
		idx += 1

		if idx == K:
			break

		# 뒤에 1 붙이기
		if arr[0] % 2 == 0:
			arr.append((arr[0] << 1) + 1)
			idx += 1
		del arr[0]

	print(format(arr[-1],'b'))


"""
# 메모리 초과 코드

if __name__ == '__main__':
	K = int(input())
	arr = [1]
	idx = 0
	while len(arr) < K:
		tmp_idx = len(arr)
		for i in range(idx, len(arr)):
			# 뒤에 0 붙이기
			arr.append(arr[i] << 1)
			# 뒤에 1 붙이기
			if arr[i] % 2 == 0:
				arr.append((arr[i] << 1) + 1)
		idx = tmp_idx
	print(format(arr[K-1],'b'))
"""
