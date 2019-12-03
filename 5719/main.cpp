//https://www.acmicpc.net/problem/5719
// 거의 최단 경로

#include<iostream>
#include<queue>
#include<cstdio>
#include<utility>

#define MAX 99999
#define MAX_NODE 500
#define MAX_EDGE 10000

using namespace std;

class adj {
	public:
		adj(int a, int b, int w, adj* n, adj* r) {
			A = a;
			B = b;
			weight = w;
			next = n;
			rev = r;
		}
		int A;
		int B;
		int weight;
		adj* next;
		adj* rev;
};

struct cmp {
	bool operator() (pair<int, int> a, pair<int, int> b) {
		return a.second > b.second;
	}
};

int main()
{
	adj* list[MAX_NODE] = {0, };
	adj* rlist[MAX_NODE] = {0, };

	freopen("input.txt","r",stdin);

	while (true) {
		// get node & edge, make adjacency list
		int node, edge;
		cin >> node >> edge;

		// exit condition
		if (node == 0 && edge == 0)
			break;

		// get start & end, initialize adjacency list
		int start, end;
		cin >> start >> end;

		for (int i = 0; i < node; ++i) {
			list[i] = new adj(i, i, 0, NULL, NULL);
			rlist[i] = new adj(i, i, 0, NULL, NULL);
		}
		// get road infos
		for (int i = 0; i < edge; ++i) {
			int a, b, w;
			cin >> a >> b >> w;
			list[a]->next = new adj(a,b,w,list[a]->next, rlist[b]->rev);
			rlist[b]->rev = list[a]->next;
		}

		// find S.S.S.P with dijkstra
		int dijkstra[MAX_NODE];
		priority_queue<pair<int, int>, vector<pair<int, int> >, cmp> heap;
		bool visited[MAX_NODE];
		adj *ptr = 0, *prev = 0;

		// initialize
		for (int i = 0; i < node; ++i) {
			dijkstra[i] = MAX;
			visited[i] = false;
		}
		dijkstra[start] = 0;	
		heap.push(make_pair(start,0));

		// find shortest path
		while (!heap.empty()) {
			int current = heap.top().first;
			heap.pop();
			visited[current] = true;

			prev = list[current];
			ptr = prev->next;
			while (ptr) {
				int now = dijkstra[ptr->B];
				int cmp = dijkstra[ptr->A] + ptr->weight;
				if (visited[ptr->B] == false && now >= cmp) {
					dijkstra[ptr->B] = cmp; 

					heap.push(make_pair(ptr->B, dijkstra[ptr->B]));
				}
				prev = ptr;
				ptr = ptr->next;
			}
		}
		// remove shortest paths
		queue<int> toDelete;
		toDelete.push(end);
		
		while (!toDelete.empty()) {
			int now = toDelete.front();
			toDelete.pop();

			ptr = rlist[now]->rev;
			while (ptr) {
				int now = dijkstra[ptr->B];
				int cmp = dijkstra[ptr->A] + ptr->weight;

				if (now == cmp) {
					toDelete.push(ptr->A);
					ptr->weight = MAX;
				}
				ptr = ptr->rev;
			}

		}

		// initialize
		while (!heap.empty()) heap.pop();
		for (int i = 0; i < node; ++i) {
			dijkstra[i] = MAX;
			visited[i] = false;
		}
		dijkstra[start] = 0;	
		heap.push(make_pair(start,0));

		// find shortest path
		while (!heap.empty()) {
			int current = heap.top().first;
			heap.pop();
			visited[current] = true;

			prev = list[current];
			ptr = prev->next;
			while (ptr) {
				int now = dijkstra[ptr->B];
				int cmp = dijkstra[ptr->A] + ptr->weight;
				if (visited[ptr->B] == false && now >= cmp) {
					dijkstra[ptr->B] = cmp; 

					heap.push(make_pair(ptr->B, dijkstra[ptr->B]));
				}
				prev = ptr;
				ptr = ptr->next;
			}
		}

		// clear memory
		while (!heap.empty()) heap.pop();
		for (int i = 0; i < node; i++) {
			ptr = list[i];
			while (ptr) {
				prev = ptr;
				ptr = ptr->next;
				delete prev;
			}
			ptr = rlist[i];
			while (ptr) {
				prev = ptr;
				ptr = ptr->next;
				delete prev;
			}
		}

		// print answer
		if (dijkstra[end] == MAX)
			cout << -1 << endl;
		else
			cout << dijkstra[end] << endl;
	} // ->while
	return 0;
}
