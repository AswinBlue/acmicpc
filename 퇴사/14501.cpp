//https://www.acmicpc.net/problem/14501

#include<iostream>

using namespace std;

int workDay, *T, *P, maxWage;


void resign(int cur, int price) 
{
	//등호 주의
	if (cur >= workDay) {
		if (maxWage < price)
			maxWage = price;
		return;
	}
	//등호 주의
	if(cur + T[cur] <= workDay)
		resign(cur + T[cur], price + P[cur]);
	resign(cur + 1, price);
}
int main()
{
	cin >> workDay;

	T = new int[workDay];//time to spend for work
	P = new int[workDay];//money you earn from work

	for (int i = 0; i < workDay; ++i) {
		cin >> T[i] >> P[i];
	}
	resign(0, 0);

	cout << maxWage << endl;
}