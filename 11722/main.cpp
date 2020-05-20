#include<iostream>

#define MAX 1000

using namespace std;

int N, arr[MAX+10];

int binarySearch(int left, int right, int target) {
#if DEBUG
	cout << "bs:" << left << " " << right << endl;
#endif
	if (left >= right) return left; // nothing match
	if (left < 0 || right >= N) return -1; // wrong range
	
	int mid = (left + right) / 2;
	if (arr[mid] == target) {
		return mid;
	}
	else if (arr[mid] < target) {
#if DEBUG
	cout << "bs -> left" << endl;
#endif
		int res1 = binarySearch(left, mid, target);
		if(res1 >= 0) return res1;
	}
	else {
#if DEBUG
	cout << "bs -> right" << endl;
#endif
		int res2 = binarySearch(mid+1, right, target);
		if(res2 >= 0) return res2;
	}
}

int main(void) {
	int A[MAX+10] = {0,};
	cin >> N;
	
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	int cnt = 0;
	for (int i = 0; i < N; i++) {
#if DEBUG
		cout << "input : " << A[i] << endl;
#endif
		int res = binarySearch(0, cnt, A[i]);

		if (arr[res] != A[i]) {
			arr[res] = A[i];
			cnt++;
		}
		/*
		// push arr[] one click 
		if (arr[res] != A[i]) {
			int tmp = arr[res];
			int tmp2;
			for (int j = res; j < cnt; j++) {
				if(arr[j] == 0) break;

				tmp2 = arr[j+1];
				arr[j+1] = tmp;
				tmp = tmp2;
			}
			arr[res] = A[i];
			cnt++;
		}
		else {
			; // do nothing
		}
		*/


#if DEBUG 
		cout << "cnt: " << cnt << endl;
		for(int j=0; j<=cnt; j++) {
			cout << arr[j] << " ";
		}
		cout << endl;
#endif
	}
	int max = 0;
	for (; max < N; max++) {
		if (arr[max] <= 0) {
			break;
		}
	}
	cout << max << endl;
}
