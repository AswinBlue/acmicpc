//https://www.acmicpc.net/problem/1149
//RGB°Å¸®

#include<iostream>
#include<algorithm>
using namespace std;

int main(void)
{
	int n;
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n;
	int **price= new int*[n+1];
	for (int i = 0; i <= n; ++i) {
		price[i] = new int[3];
	}
	price[0][0] = 0;
	price[0][1] = 0;
	price[0][2] = 0;

	int r, g, b;

	int choice = 0;

	for (int i = 1; i <= n; ++i) {
		cin >> r >> g >> b;

		price[i][0] = min(price[i - 1][1], price[i - 1][2]) + r;
		price[i][1] = min(price[i - 1][0], price[i - 1][2]) + g;
		price[i][2] = min(price[i - 1][0], price[i - 1][1]) + b;
	}
		
	//exception when n=1
	if (n == 1) {
		price[1][0] = min(g, b);
		price[1][1] = min(r, b);
		price[1][2] = min(r, g);
	}
	cout << min(min(price[n][0],price[n][1]),price[n][2]) << "\n";
}