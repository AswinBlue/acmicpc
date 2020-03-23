#include<iostream>

using namespace std;

int D[100001][101];

int max(int a, int b) {
	return a >= b ? a : b;
}
int main(void) {
	int N = 0;
	int K = 0;
	int value[101] = {0,};
	int weight[101] = {0,};

	
	//	get input
	cin >> N >> K;
	for (int i = 1; i <= N; i++) {
		cin >> weight[i] >> value[i];
	}

	// fill D[i][j]
	for (int i = 1; i <= K; i++) {
		for (int j = 1; j <= N; j++) {
			if (i >= weight[j]) { 
				D[i][j] = max(D[i][j - 1], D[i - weight[j]][j - 1] + value[j]);
			}
			else {
				D[i][j] = D[i][j - 1];
			}
		}
	}


	cout << D[K][N] << endl;

	return 0;
}
