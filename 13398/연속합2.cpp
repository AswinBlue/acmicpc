#include<iostream>
#include<queue>

using namespace std;

/*
반례 : 
10
100 -1000 1 1 1 -1 -1 10 20 30
결과 : 103
정답 : 161
*/
int main() {
	int n;
	int *arr, *arr1;
	queue<int> Q;
	
	cin >> n;
	arr = new int[n+1];
	arr1 = new int[n+1];

	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
	}
	//한 개를 빼지 않고 최대값 구하기(연속합 1과 동일) 
	arr1[0] = 0;
	int max = arr[1];

	for (int i = 1; i <= n; i++) {
		if (arr1[i - 1] + arr[i] > arr[i])
			arr1[i] = arr[i] + arr1[i - 1];
		else {
			arr1[i] = arr[i];
		}

		if (arr1[i] > max)
			max = arr1[i];

		//입력이 음수일 때 인덱스 저장
		if (arr[i] < 0) {
			Q.push(i);
		}
	}

	//한 개를 뺐을 때 최대값 구하기
	int idx = n+1, idx2 = n+1, compare;
	if (!Q.empty()) {
		idx = Q.front();
		Q.pop();
	}
	
	while (!Q.empty()) {
		idx2 = Q.front();
		Q.pop();
		if(arr1[idx] < 0)
			compare = arr1[idx2 - 1] + arr1[idx - 1];
		else
			compare = arr1[idx2 - 1] - arr[idx];

		if (compare > max)
			max = compare;
		idx = idx2;
	}
	if (idx < n) {
		if (arr[idx] <= 0)
			compare = arr[n] + arr[idx - 1];
		else
			compare = arr[n] - (arr[idx] - arr[idx - 1]);

		if (compare > max)
			max = compare;
	}

	cout << max << endl;


	return 0;
}


/*

int main() {
	int n;
	int *arr, *arr1, *arr2;
	queue<int> Q;

	cin >> n;
	arr = new int[n+1];
	arr1 = new int[n+1];
	arr2 = new int[n+1];
	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
	}
	//한 개를 빼지 않고 최대값 구하기(연속합 1과 동일)
	int current;
	arr1[0] = 0;
	for (int i = 1; i <= n; i++) {
		if (arr1[i - 1] + arr[i] > arr[i])
			arr1[i] = arr[i] + arr1[i - 1];
		else {
			arr1[i] = arr[i];
		}
	}

	arr2[0] = arr[1];
	arr2[1] = arr[1];
	int max = arr2[1];
	for (int i = 2; i <= n; i++) {
		if (arr2[i - 1] + arr[i] >= arr1[i - 2] + arr[i] && arr2[i - 1] + arr[i] >= arr[i])
			arr2[i] = arr2[i - 1] + arr[i];
		else if(arr[i] >= arr1[i - 2] + arr[i] && arr2[i - 1] + arr[i] <= arr[i]){
			arr2[i] = arr[i];
		}
		else {
			arr2[i] = arr1[i - 2] + arr[i];
		}

		if (arr2[i] > max)
			max = arr2[i];
	}

	cout << max << endl;

	return 0;
}
*/