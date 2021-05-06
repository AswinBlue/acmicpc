#include <iostream>
#include <cstring>
#define DEBUG 0

using namespace std;

int main(void) {
	int T = 0;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		// 1. get inputs
		char card[20] = {0,};
		cin >> card;
		int card_len = strlen(card);
# if DEBUG
		cout << "len : " << card_len << endl;
# endif
		int number[10] = {0,};
		for (char c : card) {
			number[c - '0'] += 1;
		}
		// change all '6' into '9'
		number[9] += number[6];
		number[6] = 0;
		
		// 2. divide into two number
		int idx = 9;
		bool flag = false;
		// find max number
		while (number[idx] == 0) idx--;
		number[idx] -= 1;
		unsigned long long num1 = idx;
		unsigned long long num2 = 0;
		int l = 1;
		while (l < card_len) {
			while (number[idx] == 0) idx--;
			number[idx] -= 1;
			unsigned long long cmp1 = (num1 * 10 + idx) * num2;
			unsigned long long cmp2 = (num2 * 10 + idx) * num1;
			if (cmp1 > cmp2) {
				num1 = num1 * 10 + idx;
			}
			else {
				num2 = num2 * 10 + idx;
			}
			++l;
			
			/*
			// num1 : max, max-3, max-4, max-7, max-8 ...
			// num2 : max-1, max-2, max-5, max-6, ...
			for (int i = 0; i < 2; ++i) {
				while (number[idx] == 0) idx--;
				number[idx] -= 1;
				if (flag) {
					num1 = num1 * 10 + idx;
				}
				else {
					num2 = num2 * 10 + idx;
				}
# if DEBUG
				cout << l << " / num : " << num1 << " " << num2 << endl;
# endif
				// check condition
				l += 1;
				if (l >= card_len) break;
			} // -> for i
			flag = !flag;
			*/
		} // -> while card_len
		cout << num1 * num2 << endl;
	} // -> for T
}
