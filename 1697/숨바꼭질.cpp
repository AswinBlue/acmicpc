#include<iostream>
#include<queue>
using namespace std;

#define MAX 100000
int N, K;
int diff;
int D[MAX + 1];

//bool hide_and_seek(int u, int level) {
//	D[u] = level;
//	if (u == K) {
//		return true;
//	}
//
//	if (level + 1 < D[u + 1]) {
//		if (u <= K) {
//			if (hide_and_seek(u + 1, level + 1))
//				return false;
//		}
//	}
//
//	if (level + 1 < D[u * 2]) {
//		if (u < K) {
//			if (hide_and_seek(u * 2, level + 1))
//				return false;
//		}
//	}
//
//	if (level + 1 < D[u - 1]) {
//		if (level < diff && u - 1 >= 0) {
//			if (hide_and_seek(u - 1, level + 1))
//				return false;
//		}
//	}
//
//}

int main() {
	cin >> N >> K;

	diff = abs(N - K);
	//result = diff;
	
	fill_n(D, MAX + 1, MAX);
	D[N] = 0;
	// ===== recursive way =====
	//hide_and_seek(N, 0);

	// ===== iterative way =====
	// 'stack' for DFS
	queue<pair<int,int>> Q;
	// in 'pair<u,v>', u = position, v = hops from N to 'u'
	
	Q.push(make_pair(N,0));
	while (!Q.empty()) {
		int u = Q.front().first;
		int v = Q.front().second;
		Q.pop();

		//check end condition
		if (u == K)
			break;
		
		if (D[u + 1] > v + 1 && u <= K) {
			Q.push(make_pair(u + 1, v + 1));
			D[u + 1] = v + 1;
		}
		if (u * 2 <= MAX) {
			if (D[u * 2] > v + 1 && u < K) {
				Q.push(make_pair(u * 2, v + 1));
				D[u * 2] = v + 1;
			}
		}
		if (D[u - 1] > v + 1 && v < diff && u - 1 >= 0) {
			Q.push(make_pair(u - 1, v + 1));
			D[u - 1] = v + 1;
		}
	}

	cout << D[K]; // �ٹٲ�(endl) ������ Ʋ��;;
	return 0;
}