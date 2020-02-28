//https://www.acmicpc.net/problem/15552
//ºü¸¥ A + B
#include<iostream>
#include<time.h>
using namespace std;
int main()
{
	int count, a, b;
	clock_t start, finish;

	cin.tie(NULL);
	ios::sync_with_stdio(false);

	start = clock();

	cin >> count;
	for (int i = 0; i<count; ++i) {
		cin >> a >> b;
		cout << a + b << "\n";
	}

	finish = clock();

	cout << (finish - start) / CLOCKS_PER_SEC;
}