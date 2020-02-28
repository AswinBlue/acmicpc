//https://www.acmicpc.net/problem/1699

#include<iostream>
#include<cmath>
using namespace std;

int main() {

	int N;
	cin >> N;

	int* arr = new int[N + 1]();
	arr[1] = 1;
	
	for (int i = 2; i <= N; ++i) {
		int limit = sqrt(i);
		for (int j = 1; j <= limit; j++) {
			int tmp;
			if ((tmp = arr[i - (j*j)] + 1) < arr[i] || arr[i] == 0) {
				arr[i] = tmp;
			}
		}
	}

	cout << arr[N] << endl;
	delete arr;
	return 0;
}
/*
<1차 시도> 모든 경우 다 방문 안되는 오류
반례 : 16+16+16+81
int cnt, min = 99999;
for (int start = sqrt(N); start > 0; start--) {
int sum = 0, n = start;
cnt = 0;
while (n > 0) {
int p = pow(n, 2);
if (sum + p <= N) {
sum += p;
cnt++;
}
else {
n--;
}

if (sum == N)
break;
}
if (sum == N) {
if (cnt < min)
min = cnt;
}
}

cout << min << endl;
*/