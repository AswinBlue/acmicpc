from sys import stdin, stdout
# for debugging
DEBUG = 0
def Print(*args):
	if DEBUG:
		print(*args)

# 문제 제한사항 정의
MAX_VALUE_LENGTH_IN_BINARY = 25  # value 값이 2^25 미만이므로 2진수 표현시 최대 25자리
MAX_N_Q = 50000  # n, q 최대값

# 함수 종류별 enum 정의
class FUNC:
	FIND_MIN=1
	FIND_MAX=2
	ADD=3
	REMOVE_MIN=4
	REMOVE_MAX=5
	
# Trie 자료구조
# 2진수로 변형시, tree의 depth 번째 글짜가 1이면 left, 0이면 right로 가도록 설정
# root는 숫자를 의미하지 않고, 시작점을 나타내기 위해 존재함
# root 다음 child 부터 특정 숫자를 의미함. node의 depth가 MAX_VALUE_LENGTH_IN_BINARY - depth + 1 자리수 숫자가 0 또는 1임을 구분하게 됨
# ex) depth가 1인 node들은 25번째 자리수가 0인지 1인지를 나타냄

LEFT = 0
RIGHT = 1
class Tree:
	parent = None  # 부모노드
	left = None
	right = None
	num = 0  # 본 node를 subtree로 할 때 포함되는 node의 개수
	side = -1  # parent입장에서 left child인지 right child인지
	
	# 생성시 parent, side 지정
	def __init__(self, parent=None, side=-1):
		self.parent = parent
		self.side = side
		
	# 모든 함수는 인자로 prefix가 붙지 않은 MAX_VALUE_LENGTH_IN_BINARY 자리의 string형태 2진수를 받는다.
	# ex: binary = 0000000000 0000000000 00011
	
	# 새로운 인자 추가
	# child 에게 recursive로 동작
	def push(self, binary, depth=0):
		# 종료조건, leaft node에서는 더이상 호출하지 않음
		if depth == MAX_VALUE_LENGTH_IN_BINARY:
			Print('push', '-', self.num, depth)
			return self.num
		
		Print('push', binary[depth], self.num, depth)
		res = 0
		b = binary[depth]
		if b == '1':
			# left child 신규 생성 필요시
			if self.left is None:
				self.left = Tree(self, LEFT)
			self.left.num += 1
			res = self.left.push(binary, depth+1)

		elif b == '0':
			# right child 신규 생성 필요시
			if self.right is None:
				self.right = Tree(self, RIGHT)
			self.right.num += 1
			res = self.right.push(binary, depth+1)
			
		else:
			None  # unexpected
			
		return res
			
	# 가장 큰 값 반환
	# recursive하게 동작
	def popMax(self, current_value='', depth=0):
		# left most child를 찾으면 된다.
		Print('popMax', current_value, self.num, depth)
		# 종료시점
		if depth == MAX_VALUE_LENGTH_IN_BINARY:
			return current_value, self, self.num
		
		result_value = 0  # 최종 결과값
		result_node = None  # Max값에 해당하는 node
		erased_num = 0  # 지워질 node에 해당하는 값 개수
		
		if self.left is not None:
			result_value, result_node, erased_num = self.left.popMax(current_value + '1', depth+1)  # 다음 child에서 이어서 계산
		
		elif self.right is not None:
			result_value, result_node, erased_num = self.right.popMax(current_value + '0', depth+1)  # 다음 child에서 이어서 계산
		
		else:
			None  # child가 없는경우는 없음
			
			
		# pop했으므로, 해당node 삭제 및 parent들 정리
		if result_node.side == LEFT and self.left is not None:
			self.left.num -= erased_num
			if self.left.num <= 0:
				del self.left
				self.left = None
				
		elif result_node.side == RIGHT and self.right is not None:
			self.right.num -= erased_num
			if self.right.num <= 0:
				del self.right
				self.right = None
		
		return result_value, self, erased_num
			
	# 가장 작은값반환
	def popMin(self, current_value='', depth=0):
		# right most child를 찾으면 된다.
		Print('popMin', current_value, self.num, depth)
		# 종료시점
		if depth == MAX_VALUE_LENGTH_IN_BINARY:
			return current_value, self, self.num
		
		result_value = 0  # 최종 결과값
		result_node = None  # Min값에 해당하는 node
		erased_num = 0  # 지워질 node에 해당하는 값 개수
		
		if self.right is not None:
			result_value, result_node, erased_num = self.right.popMin(current_value + '0', depth+1)  # 다음 child에서 이어서 계산
			
		elif self.left is not None:
			result_value, result_node, erased_num = self.left.popMin(current_value + '1', depth+1)  # 다음 child에서 이어서 계산
		
		else:
			None  # child가 없는경우는 없음
			
		# pop했으므로, 해당node 삭제 및 parent들 정리
		if result_node.side == LEFT and self.left is not None:
			self.left.num -= erased_num
			if self.left.num <= 0:
				del self.left
				self.left = None
				
		elif result_node.side == RIGHT and self.right is not None:
			self.right.num -= erased_num
			if self.right.num <= 0:
				del self.right
				self.right = None
		
		return result_value, self, erased_num
		
	# XOR비교시 가장 큰 값 반환
	# recursive하게 동작
	def getXorMax(self, binary, depth=0, current_value=''):
		# 종료시점 1. leaf node 도달시
		if depth == MAX_VALUE_LENGTH_IN_BINARY:
			Print('getXorMax', current_value, depth)
			return current_value
		
		Print('getXorMin', current_value, depth, binary[depth])
		
		result_value = 0  # 최종 결과값

		b = binary[depth]  # XOR값이 최대가 되려면 현재 자리수와 반대로 된 수를 찾아야 함
		
		if b == '0':
			# 1이 오는 경우가 최선
			if self.left is not None:
				result_value = self.left.getXorMax(binary, depth+1, current_value + '1')  # 다음 child에서 이어서  계산
			elif self.right is not None:
				# right는 현재 자리수가 0임을 의미하므로, 추가계산 없음
				result_value = self.right.getXorMax(binary, depth+1, current_value + '0')  # 다음 child에서 이어서  계산

		elif b == '1':
			# 0이 오는 경우가 최선
			if self.right is not None:
				# right는 현재 자리수가 0임을 의미하므로, 추가계산 없음
				result_value = self.right.getXorMax(binary, depth+1, current_value + '0')  # 다음 child에서 이어서  계산
			elif self.left is not None:
				result_value = self.left.getXorMax(binary, depth+1, current_value + '1')  # 다음 child에서 이어서  계산
				
		else:
			None  # unexpected
			
		return result_value
		
	# XOR비교시 가장 작은 값 반환
	# recursive하게 동작
	def getXorMin(self, binary, depth=0, current_value=''):
		# 종료시점 1. leaf node 도달시
		if depth == MAX_VALUE_LENGTH_IN_BINARY:
			Print('getXorMin', current_value, depth)
			return current_value
		
		Print('getXorMin', current_value, depth, binary[depth])
		result_value = 0  # 최종 결과값

		b = binary[depth]  # XOR값이 최소가 되려면 현재 자리수와 같은 수를 찾아야 함
		
		if b == '1':
			# 1이 오는 경우가 최선
			if self.left is not None:
				result_value = self.left.getXorMin(binary, depth+1, current_value + '1')  # 다음 child에서 이어서  계산
			elif self.right is not None:
				# right는 현재 자리수가 0임을 의미하므로, 추가계산 없음
				result_value = self.right.getXorMin(binary, depth+1, current_value + '0')  # 다음 child에서 이어서  계산

		elif b == '0':
			# 0이 오는 경우가 최선
			if self.right is not None:
				# right는 현재 자리수가 0임을 의미하므로, 추가계산 없음
				result_value = self.right.getXorMin(binary, depth+1, current_value + '0')  # 다음 child에서 이어서  계산
			elif self.left is not None:
				result_value = self.left.getXorMin(binary, depth+1, current_value + '1')  # 다음 child에서 이어서  계산
				
		else:
			None  # unexpected
			
		return result_value
	
	def print_inorder(self, current_value='', depth=0):
		if self.left is not None:
			self.left.print_inorder(current_value + '1', depth+1)
			
		if depth == MAX_VALUE_LENGTH_IN_BINARY:
			print(int(current_value,2), end=' ')
			
		if self.right is not None:
			self.right.print_inorder(current_value + '0', depth+1)
	
	
def pre_process(n):
	[*a] = map(int, stdin.readline().split())
	S = [*a]
	Print('S:', S)

	tree = Tree(None, -1)  # root node 생성
	
	unique_num = 0
	for s in S:
		b = format(s, '0' + str(MAX_VALUE_LENGTH_IN_BINARY) + 'b')
		num = tree.push(b)  # 반환값은 추가한 값이 현재 몇개 있는지
		if num == 1:
			unique_num += 1
	
	if DEBUG:
		print('=====')
		tree.print_inorder()
		print('\n=====')
			
	return tree, unique_num

def solve(tree, unique_num):
	f = stdin.readline()
	v = None
	if int(f[0]) == FUNC.FIND_MIN or int(f[0]) == FUNC.FIND_MAX or int(f[0]) == FUNC.ADD:
		f, v = map(int, f.split()) # get function and value
	else:
		f = int(f[0])
	
	if f == FUNC.FIND_MIN:
		b = format(v, '0' + str(MAX_VALUE_LENGTH_IN_BINARY) + 'b')
		Print('1:',b)
		stdout.write('{}\n'.format(v ^ int(tree.getXorMin(b), 2)))
		
	elif f == FUNC.FIND_MAX:
		b = format(v, '0' + str(MAX_VALUE_LENGTH_IN_BINARY) + 'b')
		Print('2:',b)
		stdout.write('{}\n'.format(v ^ int(tree.getXorMax(b), 2)))
		
	elif f == FUNC.ADD:
		b = format(v, '0' + str(MAX_VALUE_LENGTH_IN_BINARY) + 'b')
		Print('3:',b)
		num = tree.push(b)  # 반환값은 추가한 값이 현재 몇개 있는지\
		Print('3.unique_num:',num)
		if num == 1:
			# 새로운 값 추가된 경우
			unique_num += 1
			
		# 전체 node 개수 구하는법(문제에서는 필요없음)
		# nodes = 0
		# if tree.left is not None:
		# 	nodes += tree.left.num
		# if tree.right is not None:
		# 	nodes += tree.right.num
			
		stdout.write('{}\n'.format(unique_num))
		
	elif f == FUNC.REMOVE_MIN:
		Print('4:', unique_num)
		unique_num -= 1
		result, node, erased = tree.popMin()
		
		stdout.write('{}\n'.format(int(result, 2)))
			
	elif f == FUNC.REMOVE_MAX:
		Print('5:', unique_num)
		unique_num -= 1
		result, node, erased = tree.popMax()
		
		stdout.write('{}\n'.format(int(result, 2)))
			
	else:
		stdout.write('undefined function\n')
		None # unexpected value
		
	return unique_num
	
if __name__ == '__main__':
	T = int(stdin.readline())
	for t in range(T):
		n, q = map(int, stdin.readline().split())
		tree, unique_num = pre_process(n)  # create data structure
		# trie구조 'tree',와 중복제거 인자 개수 'unique_num' 을 받아온다.
		Print('unique_num:', unique_num)
		for i in range(q):
			unique_num = solve(tree,unique_num)
			if DEBUG:
				print('=====')
				tree.print_inorder()
				print('\n=====')
			