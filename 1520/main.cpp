#include<iostream>
#define DEBUG 0

using namespace std;

#define MAX 500

int M, N;
int** Map;
int** D;

class Node {
public:
	int x;
	int y;

	Node() { }
	Node(int x, int y) {
		this->x = x;
		this->y = y;
	}
};

int doSearch(int i, int j) {
	if (D[i][j] >= 0) return D[i][j];

	D[i][j] = 0; // check visited

	int dx[] = {0, 0, 1, -1};
	int dy[] = {1, -1, 0, 0};
	for (int k = 0; k < 4; k++) {
		int ii = i + dx[k];
		int jj = j + dy[k];
		if (ii < 0 || ii >= M || jj < 0 || jj >= N) {
			continue;
		}
		if (Map[i][j] > Map[ii][jj]) {
			D[i][j] += doSearch(ii, jj);
		}
	}
# if DEBUG
	for (int a = 0; a < M; a++) {
		for (int b = 0; b < N; b++) {
			cout << D[a][b] << " ";
		}
		cout << endl;
	}
	cout << endl;
# endif

	return D[i][j];
}

int main(void) {

	cin >> M >> N;
	Map = new int*[M]; 
	for (int i = 0; i < M ; i++) {
		Map[i] = new int[N];
	}

	// get input
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			cin >> Map[i][j];
		}
	}

	// make array for DP
	D = new int*[M];
	for (int i = 0; i < M ; i++) {
		D[i] = new int[N];
		fill_n(D[i], N, -1);
	}

	D[M - 1][N - 1] = 1;
	doSearch(0, 0);
	// fill 2d array 'D'
	cout << D[0][0] << endl;
}
