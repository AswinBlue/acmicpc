#!/usr/bin/env python3
if __name__ == '__main__':
	A = input()
	B = input()

	A_len = len(A)
	B_len = len(B)
	
	D = [[0 for i in range(B_len + 1)] for j in range(A_len + 1)]
	
	# fill 'D'

	Max = 0
	for i in range(1, A_len + 1):
		for j in range(1, B_len + 1):
			if A[i - 1] == B[j - 1]:
				D[i][j] += D[i - 1][j - 1] + 1

				Max = max(Max, D[i][j])
			else :
				None	# do nothing

	print(Max)
