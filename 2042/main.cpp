#include<iostream>
#define MAX_N 1000000

using namespace std;

long long tree[MAX_N * 4];
long long arr[MAX_N + 1];
int leafIdx[MAX_N + 1];

// put leaf node where it should be
void leafNode(int tree_index, int arr_index, int count) {
	if (count == 1) {
		tree[tree_index] = arr[arr_index + count];
		leafIdx[arr_index + count] = tree_index;
		return;
	}

	if (count % 2) {
		leafNode(tree_index * 2, arr_index, count - 1); // left child
		tree[tree_index * 2 + 1] = arr[arr_index + count - 1]; // right child
	}
	else {
		leafNode(tree_index * 2, arr_index, count / 2); // left child
		leafNode(tree_index * 2 + 1, count/2 + 1, count / 2); //right child
	}
}
// start ~ end : range to sum / left ~ right : range of tree
long long getSum(int start, int end, int left, int right) {
	if (start > end || left > right) { // wrong case
		return 0;
	}

	if (left < end || right < start) { // out of range
		return 0;
	}

	if (start == left && end == right) {
		return 0;
	}
	
	// case 1 : left < start < end < right
	// case 2 : left < start < right < end
	// case 3 : start < left < end < right
	int mid = (left + right) / 2;
	return getSum(start, end, left, mid) + getSum(start, end, mid + 1, right);
}

int main(void) {
	int N, M, K;

	cin >> N >> M >> K;
	for (int i = 1; i <= N; i++) {
		cin >> arr[i];
	}

	// put leafnode
	leafNode(1, 1, N);

	for (int i = 0; i < M + K; i++) {
		int a, b, c;
		cin >> a >> b >> c;

		if (a == 1) { // change tree[N + 'b'] as 'c'
			b += N;
			tree[b] = c;
			while (b > 1) { // update 'tree'
				if (b % 2 == 0) { // if 'b' is odd(because N inverse the 'b')
					tree[b / 2] = tree[b] + tree[b - 1];
				}
				else { // if 'b' is even
					tree[b / 2] = tree[b] + tree[b + 1];
				}
				b /= 2;
			}
		}
		else if (a == 2) { // print sum('b','c')
			
		}
		else {
			// not expected, do nothing
		}
	}
}
