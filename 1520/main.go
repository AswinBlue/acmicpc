package main

import "fmt"

type Node struct {
	x int	// cord of x
	y int	// cord of y
	k int	// var for checking where to go next
}

type Stack struct {
	node []Node
	top int
}


func (stack *Stack) push(node Node) {
	stack.node[stack.top] = node
	stack.top += 1
}

func (stack *Stack) pop() Node {
	stack.top -= 1
	return stack.node[stack.top]
}

func main() {
	var M, N int

	fmt.Scan(&M, &N)
	var Map [][]int = make([][]int, M)
	for i := 0; i < M ; i++ {
		Map[i] = make([]int, N)
	}

	// get input
	for i := 0; i < M; i++ {
		for j := 0; j < N; j++ {
			fmt.Scan(&Map[i][j])
		}
	}

	// make array for DP
	var D [][]int = make([][]int, M)
	for i := 0; i < M ; i++ {
		D[i] = make([]int, N)
	}

	// *** fill 2d array 'D'***

	// initialize
	stack := &Stack{make([]Node,500*500), 0} // stack for DFS
	stack.push(Node{M-1, N-1, 0})
	D[0][0] = 1

	dx := []int{0, 0, 1, -1}
	dy := []int{1, -1, 0, 0}
	for stack.top > 0 {
		current := stack.pop()
		i := current.x
		j := current.y

		for k := current.k; k < 4; k++ {
			ii := i + dx[k]
			jj := j + dy[k]
			if ii < 0 || ii >= M || jj < 0 || jj >= N {
				continue
			}
			if Map[i][j] < Map[ii][jj] {
				if D[ii][jj] > 0 {
					D[i][j] += D[ii][jj]
				} else {
					stack.push(Node{i, j, k}) // keep
					stack.push(Node{ii, jj, 0}) // next
					break;
				}
			}
		}
/*
	for a := 0; a < M; a++ {
		for b := 0; b < N; b++ {
			fmt.Print(D[a][b], " ")
		}
		fmt.Println()
	}
	fmt.Println()
*/
	}
/*
	for i := 0; i < M; i++ {
		for j := 0; j < N; j++ {
			print(D[i][j], " ")
		}
		println()
	}
*/
	fmt.Println(D[M-1][N-1])
}
