//https://www.acmicpc.net/problem/5719

#include<iostream>

#define MAX 99999

using namespace std;

class adj {
public:
	adj(int a, int b, int w, adj* n) {
		A = a;
		B = b;
		weight = w;
		next = n;
	}
	int A;
	int B;
	int weight;
	adj* next;
};
adj** list;
adj** endp;

int main()
{
	list = new adj*[500];
	endp = new adj*[500];
	while (true) {
		//get node & edge, make adjacency list
		int node, edge;
		cin >> node >> edge;

		//exit condition
		if (node == 0 && edge == 0)
			break;

		//list = new adj*[node];
		//endp = new adj*[node];

		//get start & end, initialize adjacency list
		int start, end;
		cin >> start >> end;

		for (int i = 0; i < node; ++i) {
			list[i] = new adj(i, i, 0, NULL);
			endp[i] = list[i];
		}
		//treat inputs
		for (int i = 0; i < edge; ++i) {
			int a, b, w;
			cin >> a >> b >> w;
			endp[a]->next = new adj(a, b, w, NULL);
			endp[a] = endp[a]->next;
		}


		//find S.S.S.P with dijkstra
		int *dijkstra = new int[node];
		bool *visited = new bool[node]();
		adj **parent = new adj*[node];//최단거리에 사용되는 edge 바로 앞 edge를 저장
		int result = MAX;

		for (int i = 0; i < node; ++i) {
			dijkstra[i] = MAX;
			parent[i] = NULL;
		}
		adj* ptr = list[start];
		adj* prev = NULL;
		int min = MAX;

		while (ptr->next) {
			prev = ptr;
			ptr = ptr->next;
			dijkstra[ptr->B] = ptr->weight;
			parent[ptr->B] = prev;
		}


		for (int cnt = 1; cnt < node; ++cnt) {
			int min = MAX, index = -1;
			for (int i = 0; i < node; ++i) {
				if (min > dijkstra[i] && !visited[i]) {
					min = dijkstra[i];
					index = i;
				}
			}
			//finish condition
			if (index == end)
				break;
			//no route
			else if (index == -1)
				break;

			visited[index] = true;
			ptr = list[index];
			while (ptr->next) {
				prev = ptr;
				ptr = ptr->next;
				if (dijkstra[ptr->B] > dijkstra[ptr->A] + ptr->weight) {
					dijkstra[ptr->B] = dijkstra[ptr->A] + ptr->weight;
					parent[ptr->B] = prev;
				}
			}
		}

		result = dijkstra[end];

		//loop for multiple shortest path
		while (true) {
			//최단거리에 사용된 edge 제거
			ptr = parent[end];//(목적지 -1) -> (목적지)로 가는 edge
			while (ptr) {
				adj* tmp = ptr->next;
				ptr->next = tmp->next;
				delete tmp;
				ptr = parent[ptr->A];//바로 앞 edge로 ptr 전환
			}
			/*
			int s = parent[end];
			int e = end;
			while (s >= 0) {
				adj* prev = NULL;
				ptr = list[s];
				while (ptr->next) {
					prev = ptr;
					ptr = ptr->next;
					if (ptr->B == e) {
						prev->next = ptr->next;
						delete ptr;
						break;
					}
				}
				e = s;
				s = parent[s];
			}
			*/

			//find semi Shortest Path
			for (int i = 0; i < node; ++i) {
				dijkstra[i] = MAX;
				visited[i] = false;
				parent[i] = NULL;
			}
			ptr = list[start];
			while (ptr->next) {
				prev = ptr;
				ptr = ptr->next;
				dijkstra[ptr->B] = ptr->weight;
				parent[ptr->B] = prev;
			}

			for (int cnt = 1; cnt < node; ++cnt) {
				int min = MAX, index = -1;
				for (int i = 0; i < node; ++i) {
					if (min > dijkstra[i] && !visited[i]) {
						min = dijkstra[i];
						index = i;
					}
				}
				//finish condition
				if (index == end)
					break;
				else if (index == -1) {
					//no route
					break;
				}

				visited[index] = true;
				ptr = list[index];
				while (ptr->next) {
					prev = ptr;
					ptr = ptr->next;
					if (dijkstra[ptr->B] > dijkstra[ptr->A] + ptr->weight) {
						dijkstra[ptr->B] = dijkstra[ptr->A] + ptr->weight;
						parent[ptr->B] = prev;
					}
				}
			}

			if (dijkstra[end] == result) {
				//another shortest path, remove again
				continue;
			}

			if (dijkstra[end] == MAX)
				cout << -1 << endl;
			else
				cout << dijkstra[end] << endl;
			/*
			for (int i = 0; i < node; ++i) {
				ptr = list[i];
				while (ptr->next) {
					adj* rmv = ptr;
					ptr = ptr->next;
					delete rmv;
				}
			}
			delete list;
			delete endp;
			*/
			break;
		}
	}
}