////https://www.acmicpc.net/problem/3745
////오름세
//#include<iostream>
//#include<string>
//#include<queue>
//using namespace std;
//#define MAX 100000
//#define MIN -100000
//int main(void)
//{
//	int num;
//	string in = to_string(MAX);
//	int previous, current;
//	int stat;
//	int max_len;
//	int *arr;
//	queue<int> index;
//
//	while (getline(cin, in)){
//		num = atoi(in.c_str());
//		if (num != 0)
//			max_len = 1;
//		else
//			max_len = 0;
//		
//		arr = new int[num];
//
//		previous = MAX;
//		for (int i = 0; i < num; ++i) {
//			cin >> current;
//			arr[i] = current;
//			if (current > previous) {
//				//++stat;
//				//if (max < stat)
//				//	max = stat;
//			}
//			else {
//				//stat = 1;
//				index.push(i);
//			}
//			previous = current;
//		}
//
//		while (index.size() > 0) {
//			stat = 0;
//
//			int k = index.front();
//			index.pop();
//			int l;
//			if (index.size() > 0)
//				l = index.front();
//			else
//				l = num;
//			int min = arr[k];
//			int max = arr[l - 1];
//
//			previous = MIN;
//
//			for (int i = 0; i < k; ++i) {
//				current = arr[i];
//				if (current > previous) {
//					if (current < min)
//						++stat;
//					previous = current;
//				}
//			}
//
//			stat += l - k;
//
//			for (int i = l; i < num; ++i) {
//				current = arr[i];
//				if (current > previous) {
//					if (current > max)
//						++stat;
//				}
//				previous = current;
//			}
//
//			if (stat > max_len)
//				max_len = stat;
//
//		}
//
//
//
//
//
//
//
//
//
//		cout << max_len << endl;
//		if(max_len!=0)
//			getline(cin, in);
//
//		delete arr;
//
//	}
//}

#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int _lower_bound(int start, int end, int *arr, int target)
{
	int mid;
	while (end - start > 0)  // 주어진 범위[start,end]에서 탐색하도록 한다. start == end이면 반복 종료
	{
		mid = (start + end) / 2;  // 주어진 범위의 중간 위치를 계산한다

		if (arr[mid] < target) // 찾고자 하는 값보다 작으면 오른쪽으로 한 칸만 더 시작 구간 갱신
			start = mid + 1;

		else  // 찾고자 하는 값보다 크면 거기까지 끝 구간 갱신
			end = mid;
	}
	return end + 1; // 찾는 구간에 없는 경우 가장 마지막 +1 위치 전달
}


int main()
{
	int arr[100001];
	int lis[100001];
	int n, i, j, cnt;

	while (scanf("%d", &n) != EOF)
	{
		// 초기화
		for (i = 1; i <= n; i++)
			lis[i] = 0;

		j = 0;
		i = 0;
		cnt = 0;

		// 값입력
		for (i = 0; i < n; i++)
			scanf("%d", &arr[i]);

		i = 0;

		lis[i] = arr[i];
		i++;

		while (i < n)
		{
			// lis의 가장 큰 값보다 더 큰값이 들어오면
			if (lis[j] < arr[i])
			{
				lis[j + 1] = arr[i];
				j++;
			}

			else
			{
				int ans = _lower_bound(0, j, lis, arr[i]);
				lis[ans - 1] = arr[i];
			}

			i++;
		}

		for (int t = 0; lis[t] != NULL; t++)
			cnt++;

		printf("%d\n", cnt);
	}

	return 0;
}


