//https://www.acmicpc.net/problem/230NUM

#include<iostream>
#define NUM 9
using namespace std;

bool dwarf[NUM];
int dwarf_height[NUM];
bool done = false;//결과를 찾았는지 여부

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

void findSpy(int cur,int n_true,int total) {
	//exit condition
	if (done)
		return;

	//finish condition
	if (n_true >= 7) {
		if (total == 100) {
			for (int i = 0; i < NUM; ++i) {
				if (dwarf[i])
					cout << dwarf_height[i] << endl;
			}
			done = true;
			return;
		}
		else
			return;
	}

	//exit condition 2
	if (cur >= NUM)
		return;

	//'cur'을 선택 한 경우
	dwarf[cur] = true;
	findSpy(cur + 1, n_true + 1, total + dwarf_height[cur]);
	//'cur'을 선택하지 않은 경우
	dwarf[cur] = false;
	findSpy(cur + 1, n_true, total);

}

int main()
{
	for (int i = 0; i < NUM; ++i) {
		cin >> dwarf_height[i];
	}

	sort(dwarf_height, 0, NUM - 1);
	
	//find 7 dwarf
	findSpy(0, 0, 0);
		
}