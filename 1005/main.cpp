// https://www.acmicpc.net/problem/1005
// ACM Craft

#include<iostream>
#include<cstdio>
#include<cstring>
#include<list>
#include<queue>

using namespace std;

void dfs(int *visit, list<int>* lst, list<int>* order, int current) {
	visit[current] = 1;
	for (list<int>::iterator itr = lst[current].begin(); itr != lst[current].end(); itr++) {
		if(visit[*itr] == 0) {
			dfs(visit, lst, order, *itr);
		}
	}
	(*order).push_back(current);
}

void topologicalSort(list<int>* lst, list<int>* order, int W) {
	int visit[1001] = {0,};
	
	dfs(visit, lst, order, W);
}

int main(void) {
	int N, K, W, T, X, Y;
	list<int> build[1001];
	int cost[1001];
	int time[1001];
	list<int> order;

freopen("in.txt","r",stdin);

	cin >> T;

	// for all testcases
	for (int tc = 0; tc < T; tc++) {
		cin >> N >> K;

		for (int i = 1; i <= N; i++) {
			cin >> cost[i];
		}

		// X의 건설 시간을 weight로 index Y에 저장
		// topological sort를 위해 거꾸로 저장함
		for (int i = 0; i < K; i++) {
			cin >> X >> Y;
			build[Y].push_back(X);
		}
		
		// 모든 node는 0으로 연결된다. topological sort 후 계산을 위해
		for (int i = 1; i <= N; i++) {
			build[i].push_back(0);
		}

		cin >> W;
		
		// reset 'time' array
		memset(time, 0, 1001 * sizeof(int));

		// 시작점을 알 수 없기 때문에 그래프의 방향을 모두 반대로 하고, 끝점에서부터 DFS를 수행해 topological sort를 한다.
		topologicalSort(build, &order, W);

		for (list<int>::iterator itr = order.begin(); itr != order.end(); itr++) {
				cout << *itr << " ";
		}
		cout << "//" << endl;

		for (int i = 0; i <= N; i++) {
				for (list<int>::iterator itr = build[i].begin(); itr != build[i].end(); itr++) {
						cout << *itr << " ";
				}
		}
		cout << endl;

		for (list<int>::iterator itr1 = order.begin(); itr1 != order.end(); itr1++) {
			int current = *itr1;

			list<int>::iterator itr2 = build[current].begin();
		
			while (itr2 != build[current].end()) {
				int next = *itr2;
				int c = cost[current] + time[next];
				
				if (c > time[current]) {
					time[current] = c;
				}
				itr2++;
			}
		}

		// 결과 출력
		cout << time[W] << endl;

		// delete list
		for (int i = 0; i <= N; i++) {
				build[i].clear();
//				for (list<int>::iterator itr = build[i].begin(); itr != build[i].end();) {
//						build[i].erase(itr++);
//				}
		}
		order.clear();

//		for (list<int>::iterator itr = order.begin(); itr != order.end();) {
//			order.erase(itr++);
//		}
	}
}
