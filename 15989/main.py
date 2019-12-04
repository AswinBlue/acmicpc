# https://www.acmicpc.net/problem/15989
# 1,2,3더하기4

if __name__ == '__main__':
	arr = [[], [0, 1, 0, 0], [0, 1, 1, 0], [0, 1, 1, 1]]
	for i in range(4, 10001):
		arr.append([0, arr[i-1][1], arr[i-2][1] + arr[i-2][2], arr[i-3][1] + arr[i-3][2] + arr[i-3][3]])

	T = int(input())
	for t in range(T):
		n = int(input())
		print(arr[n][1] + arr[n][2] + arr[n][3])

