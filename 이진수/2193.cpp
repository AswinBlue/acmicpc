//https://www.acmicpc.net/problem/2193

#include<iostream>

using namespace std;

//다른방법
unsigned long long dp[90 + 1];
unsigned long long f(int n)
{
	if (n == 1) return 1;
	if (n == 2) return 1;
	if (dp[n] > 0) return dp[n];

	dp[n] = f(n - 1) + f(n - 2);
	return dp[n];
}
////////////////////////////

int main() {
	int num;
	cin >> num;

	unsigned long long* arr = new unsigned long long[num + 1];
	unsigned long long* end_with_1 = new unsigned long long[num + 1]; // 1로 끝나는 수의 갯수
	arr[1] = 1;
	arr[2] = 1;
	end_with_1[1] = 1;
	end_with_1[2] = 1;

	for (int i = 3; i <= num; ++i) {
		arr[i] = arr[i - 1] * 2 - end_with_1[i - 1];
		end_with_1[i] = arr[i - 1] - end_with_1[i - 1];
	}
	//내 방법
	cout << arr[num] << endl;
	//다른 방법
	cout << f(num) << endl;
}