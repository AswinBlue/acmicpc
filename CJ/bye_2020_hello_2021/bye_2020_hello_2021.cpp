#include <iostream>
#include <algorithm>
#include <map>

#define DEBUG 0
using namespace std;

int main(void) {
	int T;
	cin >> T;
	
	long long target[] = {202021, 20202021, 202002021, 202012021, 202022021, 202032021, 202042021, 202052021, 202062021, 202072021, 202082021, 202092021};
	int len = sizeof(target) / sizeof(long long);
#if DEBUG
	cout << "len : " << len << endl;
#endif
	for (int t = 0; t < T; ++t) {
		int N;
		cin >> N;
		unsigned long long answer = 0;
# if DEBUG
		cout << "===== start =====" << endl;
# endif
		
		// get inputs
		map<long long, unsigned long long> nums;
		for (int n = 0; n < N; ++n) {
			int tmp;
			// cin >> tmp;
			scanf("%d", &tmp);
			if (nums.find(tmp) == nums.end()) {
				nums.insert(make_pair(tmp, 1));
			}
			else {
				nums[tmp] += 1;
			}
# if DEBUG
		cout << tmp << "," << nums[tmp] << endl;
# endif
		} // -> for n
		
		// do compare
		for (auto num = nums.begin(); num != nums.end(); num++) {
			long long f = (*num).first;
			unsigned long long s = (*num).second;
# if DEBUG
			cout << ">>" << f << "," << s << endl;
# endif
			for (int j = 0; j < len; ++j) {
				/*
				if (nums.find(target[j] - f) == nums.end()) {
					// nothing match, do nothing
				}
				else {
					answer += s * nums[target[j] - f];
				}
				*/
				if (nums.find(target[j] - f) != nums.end()) {
					answer += s * nums[target[j] - f];
# if DEBUG
				cout << j << ":" << answer << "//" << target[j] - f
					<< "///" << nums[target[j] - f] << endl;
# endif
				}

			} // -> for j
		} // -> for num
		 
		/*
		vector<int> nums;
		for (int n = 0; n < N; ++n) {
			int tmp;
			cin >> tmp;
			nums.push_back(tmp);
		} // -> for N
#if DEBUG
		cout << "inputs : ";
		for (int i = 0; i < N; ++i) {
			cout << nums[i] << " ";
		}
		cout << endl;
#endif
		
		sort(nums.begin(), nums.end());
		
#if DEBUG
		cout << "sorted : ";
		for (int i = 0; i < N; ++i) {
			cout << nums[i] << " ";
		}
		cout << endl;
#endif
		
		for (auto num = nums.begin(); num != nums.end(); num++) {
			for (int j = 0; j < len; ++j) {
				if (binary_search(num + 1, nums.end(), target[j] - *num)) {
					++answer;
				}
# if DEBUG
					cout << *num << "/" << j << "/" << answer << "//" << target[j] - *num << endl;
# endif
			}
		}
		*/
		//cout << answer / 2 << "\n";
		printf("%llu\n", answer/2);
	} // -> for T
}
