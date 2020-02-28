#include<iostream>

using namespace std;

int main() 
{
	int n, *arr;
	cin >> n;
	arr = new int[n];

	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
	}
	/*
	<1�� �õ�> �ð��ʰ�
	//������ ���̰� i�� �� �ִ밪
	int *C;
	C = new int[n+1];

	//������ ���� i
	for (int i = 1; i <= n; ++i) {
	int max = 0;
	//�������� j
	for (int j = 0; j + i < n; ++j) {
	int num = 0;
	//j~k���� ��
	for (int k = j; k < j + i; ++k) {
	num += arr[k];
	}
	if (max < num) {
	max = num;
	}
	}
	C[i] = max;
	}
	*/

	/*
	<2�� �õ�> �޸� �ʰ�

	//C[i][j] : j���� �����ϴ� i�� ���Ұ� �ִ� ���� 
	
	int **C;
	int max = 0;

	C = new int*[n+1];
	for (int i = 0; i < n; ++i) {
		C[i] = new int[n];
	}
	for (int i = 0; i < n; ++i) {
		C[1][i] = arr[i];
		if (max < C[1][i])
			max = C[1][i];
	}

	
	for (int i = 2; i <= n; ++i) {
		for (int j = 0; i + j < n; ++j) {
			C[i][j] = C[i - 1][j] + arr[i + j - 1];

			if (max < C[i][j])
				max = C[i][j];
		}
	}
	*/

	//<3�� �õ�>
	// i ������ �ִ밪�� i�� ��, �� ū���� ����
	int *C;
	C = new int[n];
	C[0] = arr[0];
	int max = arr[0];

	for (int i = 1; i < n; ++i) {
		if (C[i - 1] + arr[i] > arr[i])
			C[i] = C[i - 1] + arr[i];
		else
			C[i] = arr[i];

		if (max < C[i])
			max = C[i];
	}
	cout << max << endl;
}