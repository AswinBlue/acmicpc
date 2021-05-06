#include <iostream>
#include <vector>

#define DEBUG 0
#define MAX_N 1000
#define MAX_AB 1000
#define DIV 1000000007

using namespace std;
/*
* 길이 n+1의 임의의 좋은배열 T중 Score(T) 값이 x인 T의 개수를 Num(n,x)라 하자.
* TRY 1: Num(n,x-1)로 Num(n,x)를 계산할 수 있는 공식을 찾자.
* N 최대값이 1000이다. (1001)!/2개의 Num(n,X)는 계산이 불가능하다. 
* 하지만 a,b의 값이 1000 이하이므로,0 ~ 1000 까지만 계산하면 된다. 
* 
*/
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int T;
	cin >> T;
	/* 계산속도를 위해 arr[n][i]에 Num(n, i)의부분합을 저장한다*/
	vector< vector<int> > arr(MAX_N + 1, vector<int>(MAX_AB + 1, 0));

	// when n == 2
	arr[2][0] = 1;
	arr[2][1] = 2;
	for (int i = 2; i <= MAX_AB; ++i) {
		arr[2][i] = 3;
	}
	
	
	/* 1,2,3,...,n-1,n 까지 Num(n,x)를 구한다. 3중 for문을 돌면 timeout이 되므로 부분합을 이용한다. */
	for (int n = 3; n <= MAX_N; ++n) {
		// 부분합 사용
		for (int i = 0; i <= MAX_AB; ++i) {
			int idx = max(-1, i - n - 1);
			arr[n][i] = (arr[n][i - 1] + (idx >= 0 ? arr[n - 1][i] - arr[n - 1][idx] : arr[n - 1][i])) % DIV;
			// 나머지값을 관리하기 때문에 뺄셈의 좌측 피연산자가 우측 피연산자보다 항상 크지 않을수 있다. 예외처리 필요
			if (arr[n][i] < 0) {
				arr[n][i] = (arr[n][i] + DIV) % DIV;
			}
		} // -> for i
		
//	부분합 사용하지 않고 그냥 풀었을 때
// 	for (int n = 3; n <= MAX_N; ++n) {
//		int maxIdx = min(MAX_N, n * (n + 1) / 2 - 1);
		// for (int i = 0; i <= maxIdx; ++i) {
// 			int sum = 0;
			
// 			for (int j = i - n; j <= i ; ++j) {
// 				if (j >= 0) {
// //						cout << "i : " << i << " j : " << j << endl;
// 					sum = (sum + arr[n - 1][j]) % DIV;
// 				}
// 			} // -> for j
		
//			for (auto a : arr[n-4]) {cout << a << " ";}
//			cout << endl;
//		 } // -> for i
	} // -> for n
	
	for (int t = 0; t < T; ++t) {
		int N, A, B;
		cin >> N >> A >> B;
# if DEBUG
		for (int a = 0; a <= N; ++a) {
			for (int b = 0; b <= B; ++b) {
				cout << arr[a][b] << " ";
			}
			cout << endl;
		}
		cout << endl;
# endif
		
		int result = arr[N][B] - (A > 0 ? arr[N][A - 1] : 0);
		// 나머지값을 관리하기 때문에 뺄셈의 좌측 피연산자가 우측 피연산자보다 항상 크지 않을수 있다. 예외처리 필요
		if (result < 0) {
			result = (result + DIV) % DIV;
		}
		
		/* int result = 0;
		for (int x = A; x <= B; ++x) {
			result = (result + arr[N][x]) % DIV;
		
# if DEBUG
			cout << "result : " << result << endl;
# endif
// 			int current;
// 			/*
// 			***********************************************
// 			* n > 3인 길이 n+1의 좋은배열 T중 Score(T) 값이 x인 배열에 대해  
// 			* 0 <= x <= n 를 만족하는 T의 개수 : x + 1
// 			* n + 1 <= x 를 만족하는 T의 개수 : x - (x - (n + 1)) * 2
// 			*********************************************** 
// 			*/
// 			if (N > 3) {
// 				if (x <= N) {
// 					current = x + 1;
// 				}
// 				else {
// 					current = x - (x - (N + 1)) * 2;
// 				}
// 			}
// 			else if (N == 3) {
// 				current = arr3[x];
// 			}
// 			else if (N == 2) { 
// 				current = arr2[x];
// 			}
// 			result = (result + current) % DIV;
// # if DEBUG
// 			cout << "x : " << x << " current : " << current << " result : " << result << endl;
// # endif
		// } // -> for x
		cout << result << "\n";
	} // -> for T
}
/*

<n = 2>
1 2 2 -> 2
2 1 2 -> 1
2 2 1 -> 0


2 + (n+1) : 1
2 + (n) : 
...
2 + 0 : 1 : 1
1 + (n+1) : 1
1 + (n) : 1
...
1 + 0 : 1


result
2 : 1
1 : 1
0 : 1

<n = 3>
5 4 3 2    * 1
4 3 2 1    * 1
3 2 1 0    * 1
result
5 : 1
4 : 2
3 : 3
2 : 3
1 : 2
0 : 1

<n = 4>
9 8 7 6 5    * 1
8 7 6 5 4    * 2
7 6 5 4 3    * 3
6 5 4 3 2    * 3
5 4 3 2 1    * 2
4 3 2 1 0    * 1
result
9 : 1
8 : 3
7 : 6
6 : 9
5 : 11
4 : 11
3 : 9
2 : 6
1 : 3
0 : 1


<n = 5>
14 13 12 11 10  9    * 1
13 12 11 10  9  8    * 3
12 11 10  9  8  7    * 6
11 10  9  8  7  6    * 9
10  9  8  7  6  5    * 11
9   8  7  6  5  4    * 11
8   7  6  5  4  3    * 9
7   6  5  4  3  2    * 6
6   5  4  3  2  1    * 3
5   4  3  2  1  0    * 1
result
14: 1
13: 4
12: 10
11: 19
10: 31
9 : 46
8 : 64
7 : 85
6 : 64
5 : 46
4 : 31
3 : 19
2 : 10
1 : 4
0 : 1
==============

v\n | 2    3    4 ...
-------------------
0 | 1 -> 1 -> 1 ...
1 | 1 -> 2 -> 3 ...
2 | 1 -> 3 -> 6
3 | 0 -> 3 -> 9

0 <= x <= n 까지 개수 : x + 1
n + 1 <= x 개수 : x - (x - (n + 1)) * 2
*/
