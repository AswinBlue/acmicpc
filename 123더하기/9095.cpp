//123¥ı«œ±‚
//https://www.acmicpc.net/problem/9095
#include<iostream>

#define MAX_VAL 11

using namespace std;

int main(void)
{
	int T, n;
	cin >> T;

	int combination[MAX_VAL + 1] = { 0. };

	combination[0] = 1;

	for (int i = 1; i < MAX_VAL; ++i) {
		if (i >= 1)
			combination[i] += combination[i - 1];
		if (i >= 2)
			combination[i] += combination[i - 2];
		if (i >= 3)
			combination[i] += combination[i - 3];
	}
	for (int i = 0; i < T; ++i) {
		cin >> n;
		cout << combination[n] << endl;
	}


}