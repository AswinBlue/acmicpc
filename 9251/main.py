#!/usr/bin/env python3

if __name__ == "__main__":
	A = str(input())
	B = str(input())

	len_A = len(A) 
	len_B = len(B)

	D = [ [0 for j in range(len_B + 1)] for i in range(len_A + 1)]
	
	for x in range(1,len_A + 1):
		for y in range(1, len_B + 1):
			if A[x - 1] == B[y - 1]:
				D[x][y] = D[x-1][y-1] + 1
			else:
				D[x][y] = max(D[x-1][y],D[x][y-1])

	print(D[len_A][len_B])
