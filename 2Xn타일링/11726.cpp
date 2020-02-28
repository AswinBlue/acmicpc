//https://www.acmicpc.net/problem/11726

#include<iostream>

#define MAX_VAL 10007
#define MAX 1000
using namespace std;


int counts[MAX + 1];

int main() {
	
	int num;

	cin >> num;
	counts[1] = 1;
	counts[2] = 2;
	for (int i = 3; i <= num; ++i) {
		counts[i] = (counts[i - 1] + counts[i - 2])%MAX_VAL;
	}

	cout << counts[num] << endl;
}