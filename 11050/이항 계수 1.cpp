//https://www.acmicpc.net/problem/11050
//이항 계수 1

#include<iostream>
using namespace std;

int Combination(int N, int K);
int Combination_perm(int N, int K, int result);
int Combination_div(int K, int result);

int main(void)
{
	int N, K;
	cin >> N >> K;
	cout << Combination(N, K);

}
int Combination(int N, int K)
{
	return Combination_perm(N, K, 1)/Combination_div(K,1);
}
int Combination_perm(int N, int K, int result)
{
	if (K == 0)
		return result;
	Combination_perm(N - 1, K - 1, result*N);
}
int Combination_div(int K, int result)
{
	if (K == 0)
		return result;
		Combination_div(K - 1, result*K);
}