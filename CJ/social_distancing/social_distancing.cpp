#include <iostream>
#include <vector>
#include <algorithm>

#define DEBUG 0
using namespace std;

int main(void) {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int N, S;
		cin >> N >> S;
		vector<int> X;
//		vector<int> length;

		for (int n = 0; n < N; n++) {
			int tmp;
			// cin >> tmp;
			scanf("%d", &tmp);
			
			X.push_back(tmp);
		} // -> for n
		// ascending sort
		sort(X.begin(), X.end());
//		for (int x = 1; x < N; ++x) {
//			length.push_back(X[x] - X[x - 1]);
//		}
		// ascending sort
//		sort(length.begin(), length.end());
		// sort(length.begin(), length.end(), [] (int a, int b) -> bool {return a > b;}); 
		
# if DEBUG
		cout << "X : ";
		for (auto x : X) {
			cout << x << " ";
		}
		cout << endl;
//		cout << "length : ";
//		for (auto l : length) {
//			cout << l << " ";
//		}
//		cout << endl;
# endif
		
		int answer = -1;

//		for (int s = 0, e = (length.size() - 1) * 2; s < e;) {
//			int b_search = length[m];
		for (int s = 1, e = X[N - 1] - X[0]; s < e;) {
			int m = (s + e) / 2;
			int cnt = 1; // 1 is a count of start position, 'X[0]'
# if DEBUG
			cout << " s, e, m : " << s << " " << e << " " << m << endl;
# endif
			// for all elements in 'X', check if 'mid' satisfy the condition
			for (int i = 1, pos = 0; i < N; ++i) {
//				if (X[i] - X[pos] >= b_search) {
				if (X[i] - X[pos] >= m) {
					pos = i;
					++cnt;
				}
				// quick stop
				if (cnt >= S)	break;
			}
# if DEBUG
//			cout << "b_search, cnt : " << b_search << " " << cnt << endl;
# endif
			// satisfied
			if (cnt >= S) {
				// "previous answer < current answer" always true
//				answer = b_search;
				// exit condition for prevent infinite loop
				if (s == m) {
					answer = m;
					break;
				}
				s = m;
			}
			// not satisfied
			else {
				e = m;
			}
# if DEBUG
//			cout << "answer : " << answer << endl;
# endif
		} // -> for i
		
		// check 'answer + 1' satisfy the condition
		for (int i = 1, pos = 0, cnt = 1; i < N; ++i) {
			if (X[i] - X[pos] >= answer + 1) {
				pos = i;
				++cnt;
			}
			// quick stop
			if (cnt >= S)	{
				++answer;
				break;
			}
		}
		
		// print result
		cout << answer << endl;
	} // -> for t
}
