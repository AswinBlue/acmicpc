package main

import "fmt"

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func main() {
	var A, B string

	// get input
	fmt.Scan(&A, &B)

	var A_len int = len(A)
	var B_len int = len(B)

	print(A_len, " ", B_len,"\n")
	var D [][]int = make([][]int, A_len + 1)
	for i := 0; i <= A_len; i++ {
		D[i] = make([]int, B_len + 1)
	}

	// fill 2d array 'D'
	var Max int = 0
	for i := 1; i <= A_len; i++ {
		for j := 1; j <=  B_len; j++ {
			if A[i - 1] == B[j - 1] {
				D[i][j] += D[i - 1][j - 1] + 1
				Max = max(Max, D[i][j])
			}
		}
	}

	fmt.Println(Max)
}
