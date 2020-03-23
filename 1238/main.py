if __name__ == "__main__":
	N, M, X  = map(int, input().split())
	
	edge = [[9999999 for i in range(N + 1)] for i in range(N + 1)]

	# get inputs	
	for i in range(M):
		start, end, weight = map(int, input().split())
		edge[start][end] = weight

	for i in range(N + 1):
		edge[i][i] = 0

	## from X to HOME

	D = [9999999 for i in range(N + 1)]
	visited = [0 for i in range(N + 1)]


	# initialize
	current = X
	D[X] = 0

	for t in range(N-1):
		# mark visited
		visited[current] = 1

		# Dijkstra comparison
		for k in range(1, N + 1):
			if visited[k] == 0:
				D[k] = min(D[k], D[current] + edge[current][k])

		# find next 'current'
		min_value = 9999999
		min_idx = 0
		for i in range(1, N + 1):
			if visited[i] == 0:
				if min_value > D[i]:
					min_value = D[i]
					min_idx = i
		current = min_idx


	## from HOME to X

	D2 = [9999999 for i in range(N + 1)]
	visited2 = [0 for i in range(N + 1)]

	# initialize
	current = X
	D2[X] = 0

	for t in range(N-1):
		# mark visited
		visited2[current] = 1

		# Dijkstra comparison
		for k in range(1, N + 1):
			if visited2[k] == 0:
				D2[k] = min(D2[k], D2[current] + edge[k][current])

		# find next 'current'
		min_value = 9999999
		min_idx = 0
		for i in range(1, N + 1):
			if visited2[i] == 0:
				if min_value > D2[i]:
					min_value = D2[i]
					min_idx = i
		current = min_idx

	# find result
	result = 0
	for i in range(1, N + 1):
		result = max(result, D[i] + D2[i])

	print(result)
