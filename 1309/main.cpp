#include <iostream>

#define MAX 100000

using namespace std;

int main(void) {
	int arr1[MAX] = {1,};
	int arr2[MAX] = {1,};
	int arr3[MAX] = {1,};
	int N;
	cin >> N;
	
	for (int i = 1; i < N; i++) {
		arr1[i] = (arr2[i-1] + arr3[i-1]) % 9901;
		arr2[i] = (arr1[i-1] + arr3[i-1]) % 9901;
		arr3[i] = (arr1[i-1] + arr2[i-1] + arr3[i-1]) % 9901;
	}

	cout << (arr1[N-1] + arr2[N-1] + arr3[N-1]) % 9901 << endl;
}
