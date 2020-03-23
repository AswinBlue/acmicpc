#include<iostream>
#define DEBUG 0

using namespace std;

#define MAX 500

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

class Stack {
	Node** node;
public:
	int top;
	Stack() {
		top = 0;
		node = new Node*[MAX * MAX]();
	}

	void push(Node* node) {
		delete this->node[top];
		this->node[top] = node;
		top++;
	}

	Node pop() {
		top--;
		return *node[top];
	}
};

int main(void) {
	int M, N;

	cin >> M >> N;
	int** Map = new int*[M]; 
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
	int** D = new int*[M];
	for (int i = 0; i < M ; i++) {
		D[i] = new int[N];
	}

	// fill 2d array 'D'

	Stack stack;
	stack.push(new Node(0, 0));

	int dx[] = {0, 0, 1, -1};
	int dy[] = {1, -1, 0, 0};
	while (stack.top > 0) {
		Node current = stack.pop();
		int i = current.x;
		int j = current.y;
		D[i][j]++;

		for (int k = 0; k < 4; k++) {
			int ii = i + dx[k];
			int jj = j + dy[k];
			if (ii < 0 || ii >= M || jj < 0 || jj >= N) {
				continue;
			}
			if (Map[i][j] > Map[ii][jj]) {
				stack.push(new Node(ii,jj));
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
	}
	cout << D[M-1][N-1] << endl;
}
