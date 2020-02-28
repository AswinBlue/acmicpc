//https://www.acmicpc.net/problem/11399

#include<iostream>

using namespace std;

void sort(int* arr, int s, int e) {
	if (s >= e)
		return;

	int pivot = arr[s];
	int i = s;
	int j = e;
	while (i < j) {
		//find 'j'
		for (; arr[j] > pivot; --j);

		//find 'i'
		//반복 조건에 주의
		for (; arr[i] <= pivot && i < j; ++i);

		//swap 'i' and 'j'
		int tmp = arr[i];
		arr[i] = arr[j];
		arr[j] = tmp;
	}
	//move pivot to right position
	arr[s] = arr[i];
	arr[i] = pivot;

	//recursive to lieft
	sort(arr, s, i - 1);
	//recursive to right
	sort(arr, i + 1, e);
}
int main()
{
	int num;
	cin >> num;
	int * arr = new int[num];
	for (int i = 0; i < num; ++i) {
		cin >> arr[i];
	}
	sort(arr, 0, num - 1);

	int sum = arr[0];
	int total = arr[0];
	for (int i = 1; i < num; ++i) {
		sum = arr[i] + sum;
		total += sum;
	}
	cout << total << endl;
}