#include<iostream>

using namespace std;

#define MAX 1000000000
int main() {
	int N, K, **arr;
	cin >> N >> K;
	//Dynamic programming을 위한 배열
	//arr[n][k] : 숫자 n을 k개의 정수로 만들 수 있는 경우의 수
	arr = new int*[N + 1];
	for (int i = 0; i <= N; i++) {
		arr[i] = new int[K + 1];
		arr[i][1] = 1;
	}

	////K라는 제약조건이 없을 때 풀이
	//arr[1] = 1;

	//for (int i = 2; i <= N; i++) {
	//	int sum = 0;
	//	for (int j = 1; j < i; j++) {
	//		sum += arr[j];
	//	}
	//	arr[i] = sum + 1;
	//}

	//규칙 : 
	//만약 0이 사용되지 않았다면 arr[n][k]는 1<=i<n인 arr[i][k-1] 의 합과 같다.
	//0이 사용되었기 때문에 0<=i<=n로 i의 범위가 바뀐다.

	//arr[1][k] 초기화
	for (int i = 0; i < K; i++) {
		arr[0][i] = 1;
	}

	for (int k = 2; k < K; k++) {
		for (int i = 1; i <= N; i++) {
 			int sum = 0;
			for (int j = 0; j <= i; j++) {
				sum = (sum + arr[j][k - 1]) % MAX;
			}
			arr[i][k] = sum;
		}
	}

	//arr[N][K]를 구한다.
	int sum = 0;
	for (int j = 0; j <= N; j++) {
		sum = (sum + arr[j][K - 1]) % MAX;
	}
	arr[N][K] = sum;
	

	cout << arr[N][K] << endl;
	for (int i = 0; i <= N; i++) {
		delete arr[i];
	}
	delete arr;

	return 0;
}
/*
1 
2 11
3 12/21 111
4 31/13/22 121/211/112 1111
5 41/32/23/14 311/131/221/122/212/113 11111
*/

/*
0 00 000 0000 00000
1 10/01 100/010/001
2 11/20/02 002/101/011/110/200/020
3 03/12/21/30 003/102/012/111/201/021/030/120/210/300
4 31/13/22 121/211/112 1111
5 41/32/23/14 311/131/221/122/212/113 11111
*/