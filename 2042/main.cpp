//https://www.acmicpc.net/problem/2042
// 구간합 구하기
// segment tree를 이용하여 부분합을 구하는 가장 기본적인 문제. 아래 두 가지 실수에 주의하자
// 1. arr을 업데이트 해주는 부분에 주의하자
// 2. 결과값을 long long으로 처리해야 함에 주의하자

#include<iostream>
#define DEBUG 0
#define MAX_N 1000000

using namespace std;

long long tree[MAX_N * 4];
long long arr[MAX_N + 1];

// put leaf node where it should be, make tree
long long init(int tree_index, int left, int right) {
    if (left == right) {
        return tree[tree_index] = arr[left];
    }
    return tree[tree_index] = init(tree_index * 2, left, (left + right) / 2) + init(tree_index * 2 + 1, (left + right) / 2 + 1, right);
}
// start ~ end : range to sum / left ~ right : range of tree
long long getSum(int index, int start, int end, int left, int right) {
	if (start > end || left > right) { // wrong case
		return 0;
	}
    // case 1 : out of range
	else if (end < left || right < start) {
		return 0;
	}
	// case 2 : left ~ right includes start ~ end
    else if (left < start && end < right) {
        return getSum(index * 2, start, end, left, (left + right) / 2) + getSum(index * 2 + 1, start, end, (left + right) / 2 + 1, right);
    }
    // case 3 : start ~ end includes left ~ right
    else if (start <= left && right <= end) {
        return tree[index];
    }
	// case 3 : they don't includes each other
    else {
        return getSum(index * 2, start, end, left, (left + right) / 2) + getSum(index * 2 + 1, start, end, (left + right) / 2 + 1, right);
    }
}

void update(int index, int node, long long diff, int left, int right) {
    tree[index] -= diff;
    if (left == right) {
        return;
    }
    int mid = (left + right) / 2;
    if (node <= mid) {
        update(index * 2, node, diff, left, mid);
    }
    else {
        update(index * 2 + 1, node, diff, mid + 1, right);
    }
}

int main(void) {
	int N, M, K;

	cin >> N >> M >> K;
	for (int i = 1; i <= N; i++) {
		cin >> arr[i];
	}

	// make tree from root to leaf
    init(1, 1, N);

#if DEBUG
    cout << "init" << endl;
    for (int i = 0; i <= N * 4; i++) {
        cout << tree[i] << " ";
    }
    cout << endl;
# endif
	for (int i = 0; i < M + K; i++) {
		int a;
		cin >> a;

		if (a == 1) { // change value of arr[b] in 'tree' to 'c'
            int b;
            long long c;
            cin >> b >> c;
            update(1, b, arr[b] - c, 1, N);
            arr[b] = c; // ! don't forget to update
#if DEBUG
    cout << "updated" << endl;
    for (int i = 0; i <= N * 4; i++) {
        cout << tree[i] << " ";
    }
    cout << endl;
# endif
		}
		else if (a == 2) { // print sum('b','c')
#if DEBUG
    cout << "print" << endl;
# endif
            int b, c;
            cin >> b >> c;
		    cout << getSum(1, b, c, 1, N) << endl;
		}
		else {
			// not expected, do nothing
		}
	}

    return 0;
}
