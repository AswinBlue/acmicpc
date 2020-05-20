#include<iostream>
#include<queue>

#define MAX 999999999
#define DEBUG 0

using namespace std;

int main() {
	int city, bus;
	int map[100][100];

	cin >> city >> bus;

	// init map
	for (int i = 0; i < city; i++) {
		fill_n(map[i], city, MAX);
		map[i][i] = 0;
	}

	// get inputs
	for (int i = 0; i < bus; ++i) {
		int start, end, cost;
		cin >> start >> end >> cost;
		if (map[start - 1][end - 1] > cost) {
			map[start - 1][end - 1] = cost;
		}
	}

	// use mapijkstra to find S.S.S.P
	// map[i][j] means Shortest path from 'i' to 'j'

#if DEBUG
	cout << endl;
	for(int x = 0; x < city; x++){
		for(int y = 0; y < city; y++) {
			cout << map[x][y] << " ";
		}
		cout << endl;
	}
	cout << endl;
#endif

	// for all City, find shortest path to other Cities
	for (int k = 0; k < city; ++k) {
		for (int i = 0; i < city; ++i) {
			for (int j = 0; j < city; ++j) {
				if (map[i][j] > map[i][k] + map[k][j]) {
					map[i][j] = map[i][k] + map[k][j];
#if DEBUG
					cout << "i : " << i << " j : " << j << "map[i][j]" << map[i][j] << endl;
#endif
				}
			}
		}
	}

	// print result
	for (int i = 0; i < city; ++i) {
		for (int j = 0; j < city; ++j) {
			if (map[i][j] >= MAX) {
				map[i][j] = 0;
				cout << 0 << " ";
			}
			else {
				cout << map[i][j] << " ";
			}
		}
		cout << endl;
	}
}
