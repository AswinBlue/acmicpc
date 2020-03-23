class Tree :
	def __init__(self, node):
		self.node = node

		self.tree = [0 for i in range(4 * node + 1)]

	def init(self):
		self.innerNodeStart =  


if __name__ == '__main__':
    n = int(input())
    seq = []
    for i in map(int,input().split()):
        seq.append(i)

    check = [seq[0]]
    for i in seq[1:]:
        # if increasing sequence
        if check[-1] < i:
            check.append(i)
        # if not, find appropriate index for 'i' in 'check'
        else:
            # find from end to front
            for j in range(len(check)-1, -1, -1):
                if check[j] < i:
                    check[j+1] = i
                    break
                elif j == 0:
                    check[0] = i

    print(len(check))
