//https://www.acmicpc.net/problem/1003
//피보나치 함수

#include<iostream>

using namespace std;
int main()
{
	int arr0[41] = { -1, };
	int arr1[41] = { -1, };

	arr0[0] = 1;
	arr1[0] = 0;
	arr0[1] = 0;
	arr1[1] = 1;

	for (int i = 2; i <= 40; ++i) {
		arr0[i] = arr0[i - 1] + arr0[i - 2];
		arr1[i] = arr1[i - 1] + arr1[i - 2];
	}
	
	int n;
	cin >> n;
	while (n > 0) {
		int in;
		n--;
		cin >> in;
		cout << arr0[in] << " " << arr1[in] << "\n";
	}
}