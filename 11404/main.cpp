#include<iostream>
#include<queue>

#define MAX 999999
#define DEBUG 0

using namespace std;

// class for heap
class node {
	public:
		int value;
		int index;

		node(int value, int index) {
			this->value = value;
			this->index = index;
		}
};

struct compare {
	bool operator() (node*& a, node*& b) {
		return a->value > b->value;
	}
};

// class for adjacency list
class adj {
	public:
		int start;
		int end;
		int cost;
		adj* next;

		adj() {}
		adj(int start, int end, int cost, adj* next) {
			this->start = start;
			this->end = end;
			this->cost = cost;
			this->next = next;
		}
};

// declare adjacency list
adj **list;

int main() {
	int city, bus;

	cin >> city >> bus;

	// create adjacency list
	list = new adj*[city];
	for (int i = 0; i < city; ++i) {
		list[i] = new adj(i, i, 0, NULL);
	}

#if DEBUG
	cout << "get input" << endl;
#endif

	// get inputs & fill adjacency graph
	for (int i = 0; i < bus; ++i) {
		int start, end, cost;
		cin >> start >> end >> cost;
		adj *tmp = new adj(start - 1, end - 1, cost, list[start - 1]->next);
		list[start - 1]->next = tmp;
	}

#if DEBUG
	for (int i = 0; i < city; i++) {
		adj *ptr = list[i];
		while (ptr) {
			cout << ptr->start << " " << ptr->end << " " <<ptr->cost << endl;
			ptr = ptr->next;
		}
	}
	cout << "make array \'D\'" << endl;
#endif

	// use Dijkstra to find S.S.S.P
	// D[i][j] means Shortest path from 'i' to 'j'
	int **D = new int*[city];
	for (int i = 0; i < city; ++i) {
		D[i] = new int[city];
		fill_n(D[i], city, MAX);
	}
#if DEBUG
	cout << endl;
	for(int x = 0; x < city; x++){
		for(int y = 0; y < city; y++) {
			cout << D[x][y] << " ";
		}
		cout << endl;
	}
	cout << endl;
#endif

	// for all City, find shortest path to other Cities
	for (int i = 0; i < city; ++i) {
		// init Dijkstra variables
		priority_queue<node*, vector<node*>, compare> Q;
		bool *visit = new bool[city]();
		Q.push(new node(D[i][i], i));
		D[i][i] = 0;

#if DEBUG 
		cout << "start, i : " << i << endl;
#endif

		while (!Q.empty()) {
			int top = Q.top()->index;
			Q.pop();
			visit[top] = true;
#if DEBUG
			cout << "top : " << top << endl;
#endif
			adj *ptr = list[top]->next;

#if DEBUG
			cout << "ptr : " << ptr << endl;
#endif

			while (ptr) {
				if (visit[ptr->end] == true) {
					ptr = ptr->next;
					continue;
				}
#if DEBUG
				cout << "start, end, cost : " << ptr->start << " " << ptr->end << " " << ptr->cost << endl;
#endif

				if (D[i][ptr->end] > D[i][ptr->start] + ptr->cost) {
					D[i][ptr->end] = D[i][ptr->start] + ptr->cost;
					Q.push(new node(D[i][ptr->end], ptr->end));
				}
				ptr = ptr->next;
#if DEBUG
	cout << "Print \'D\'" << endl;
	for(int x = 0; x < city; x++){
		for(int y = 0; y < city; y++) {
			cout << D[x][y] << " ";
		}
		cout << endl;
	}
	cout << endl;
#endif
			}
		}
	}
	
	// free memories
	for (int i = 0; i < city; i++) {
		adj *ptr = list[i];
		while (ptr) {
			adj *tmp = ptr;
			ptr = ptr->next;
			delete tmp;
		}
	}


	// print result
	for (int i = 0; i < city; ++i) {
		for (int j = 0; j < city; ++j) {
			if (D[i][j] >= MAX) {
				D[i][j] = 0;
				cout << 0 << " ";
			}
			else
				cout << D[i][j] << " ";
		}
		cout << endl;
	}
}
