# https://www.acmicpc.net/problem/3745
# 오름세

import sys

# binary search
# timeComplexity O(log(n))
def b_search(start, end, arr, target):
	while start <= end:
		mid = (start + end) // 2
		if arr[mid] < target:
			start = mid + 1
		elif arr[mid] > target:
			end = mid - 1
		# if target destination found
		else:
			return mid
	# if nothing found, return start
	return start


if __name__ == '__main__':
	for line in sys.stdin:
		N = line
		maxLen = 0
		check = [9999999] * int(N)

		for i in map(int, input().split()):
			idx = b_search(0, maxLen, check, i)
			check[idx] = i

			if maxLen < idx + 1:
				maxLen = idx + 1

		print(maxLen)
