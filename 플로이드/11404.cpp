//https://www.acmicpc.net/problem/11404

#include<iostream>

#define MAX 9999
using namespace std;

class adj {
public:
	adj() {}
	adj(int start, int end, int cost, adj* next) {
		this->start = start;
		this->end = end;
		this->cost = cost;
		this->next = next;
	}

	int start;
	int end;
	int cost;
	adj* next;
};

adj** list, **top;
int main() {
	int city, bus;

	cin >> city >> bus;

	//create list
	list = new adj*[city];
	top = new adj*[city];
	for (int i = 0; i < city; ++i) {
		list[i] = new adj;
		list[i]->next = new adj(i, i, 0, NULL);
		top[i] = list[i]->next;
	}

	//set adjacency graph
	for (int i = 0; i < bus; ++i) {
		int start, end, cost;
		cin >> start >> end >> cost;
		top[start - 1]->next = new adj(start - 1, end - 1, cost, NULL);
		top[start - 1] = top[start - 1]->next;
	}

	//use Dijkstra to find S.S.S.P
	int **D = new int*[city];
	for (int i = 0; i < city; ++i) {
		D[i] = new int[city];
		fill_n(D[i], city, MAX);
	}

	for (int i = 0; i < city; ++i) {
		bool *visit = new bool[city]();
		int cnt = 1;
		visit[i] = true;

		//initialize 'D'
		adj* ptr = list[i]->next;
		while (ptr) {
			if (ptr->cost < D[i][ptr->end])
				D[i][ptr->end] = ptr->cost;
			ptr = ptr->next;
		}

		while(cnt < city) {
			//find min cost from not visited city
			int min = MAX, index;
			for (int j = 0; j < city; ++j) {
				if (visit[j] == false && min > D[i][j]) {
					min = D[i][j];
					index = j;
				}
			}

			adj* ptr2 = list[index]->next;
			while (ptr2) {
				//compare previous cost (i -> end) & new cost (i -> index -> end)
				if (D[i][index] + ptr2->cost < D[i][ptr2->end])
					D[i][ptr2->end] = D[i][index] + ptr2->cost;
				ptr2 = ptr2->next;
			}
			visit[index] = true;
			++cnt;

		}
	}

	for (int i = 0; i < city; ++i) {
		for (int j = 0; j < city; ++j) {
			if (D[i][j] == MAX) {
				D[i][j] = 0;
				cout << 0 << " ";
			}
			else
				cout << D[i][j] << " ";
		}
		cout << endl;
	}
}