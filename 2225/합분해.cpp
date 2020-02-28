#include<iostream>

using namespace std;

#define MAX 1000000000
int main() {
	int N, K, **arr;
	cin >> N >> K;
	//Dynamic programming�� ���� �迭
	//arr[n][k] : ���� n�� k���� ������ ���� �� �ִ� ����� ��
	arr = new int*[N + 1];
	for (int i = 0; i <= N; i++) {
		arr[i] = new int[K + 1];
		arr[i][1] = 1;
	}

	////K��� ���������� ���� �� Ǯ��
	//arr[1] = 1;

	//for (int i = 2; i <= N; i++) {
	//	int sum = 0;
	//	for (int j = 1; j < i; j++) {
	//		sum += arr[j];
	//	}
	//	arr[i] = sum + 1;
	//}

	//��Ģ : 
	//���� 0�� ������ �ʾҴٸ� arr[n][k]�� 1<=i<n�� arr[i][k-1] �� �հ� ����.
	//0�� ���Ǿ��� ������ 0<=i<=n�� i�� ������ �ٲ��.

	//arr[1][k] �ʱ�ȭ
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

	//arr[N][K]�� ���Ѵ�.
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