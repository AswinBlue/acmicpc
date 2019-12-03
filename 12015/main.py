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

# linear search
def l_search(end, arr, target):
	while arr[end] >= target:
		end -= 1
		if end < 0:
			return 0
	
	return end + 1


if __name__ == '__main__':
	n = int(input())
	seq = []
	for i in map(int, input().split()):
		seq.append(i)

	maxLen = 1
	check = [9999999] * n
	check[0] = seq[0]
	idx = 0
	for i in range(n - 1):
# if increasing sequence
		print(check,idx, seq[i + 1], maxLen)
		if check[idx] < seq[i + 1]:
			idx = b_search(idx, maxLen, check, seq[i + 1])
			check[idx] = seq[i + 1]
		elif check[idx] == seq[i + 1]:
			# do nothing
			None	
# if decreasing sequence, find appropriate index for 'i' in 'check'
		else:
			# idx = l_search(idx, check, seq[i + 1])
			idx = b_search(0, idx, check, seq[i + 1])
			check[idx] = seq[i + 1]

		if maxLen < idx + 1:
			maxLen = idx + 1

	print(maxLen)
