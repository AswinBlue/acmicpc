//https://www.acmicpc.net/problem/1068

#include<iostream>

using namespace std;

class tree {
public:
	tree() {
		parent = NULL;
		child = 0;
	}
	tree* parent;
	int num;
	int child;
};
int main() {
	int num;
	cin >> num;

	//create tree
	tree* T = new tree[num];
	for (int i = 0; i < num; ++i) {
		int parent;
		cin >> parent;
		T[i].num = i;
		
		if (parent > -1) {
			T[i].parent = &T[parent];
			T[parent].child += 1;
		}
	}

	//delete one node
	int todelete;
	cin >> todelete;
	if(T[todelete].parent != NULL)
		T[todelete].parent->child -= 1;
	//T[todelete].parent = NULL;

	//count leaf node
	int cnt = 0;
	for (int i = 0; i < num; ++i) {
		//find leaf node
		if (T[i].child == 0) {
			cnt++;
			tree* tmp = &T[i];
			//check if the node is cut out from the tree
			while (tmp) {
				if (tmp->num == todelete) {
					cnt--;
					break;
				}
				tmp = tmp->parent;
			}
		}
	}
	if (cnt < 0) cnt = 0;
	cout << cnt << endl;
	
}