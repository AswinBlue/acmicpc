#include <map>
#include <iostream>
#define DEBUG 0
using namespace std;

int main(void) {
	// initialize keyboard array
	map<char,pair<int,int>> qwerty;
	
	char row1[] = {'Q','W','E','R','T','Y','U','I','O','P'};
	char row2[] = {'A','S','D','F','G','H','J','K','L'};
	char row3[] = {'Z','X','C','V','B','N','M'};
	
	for (int i = 0; i < (int)sizeof(row1); i++) {
		qwerty.insert(make_pair(row1[i], make_pair(0, i)));
	}
	for (int i = 0; i < (int)sizeof(row2); i++) {
		qwerty.insert(make_pair(row2[i], make_pair(1, i)));
	}
	for (int i = 0; i < (int)sizeof(row3); i++) {
		qwerty.insert(make_pair(row3[i], make_pair(2, i)));
	}
	
#if DEBUG
	for (int i = 0; i < (int)sizeof(row1); i++) {
		cout << qwerty[row1[i]].first << " " << qwerty[row1[i]].second << " ";
	}
	cout << endl;
	for (int i = 0; i < (int)sizeof(row2); i++) {
		cout << qwerty[row2[i]].first << " " << qwerty[row2[i]].second << " ";
	}
	cout << endl;
	for (int i = 0; i < (int)sizeof(row3); i++) {
		cout << qwerty[row3[i]].first << " " << qwerty[row3[i]].second << " ";
	}
	cout << endl;
#endif
	
	// get input
	int T;
	char txt[110];
	cin >> T;
	
	for (int t = 0; t < T; t++) {
		cin >> txt;
	
		// calculate result
		int total_diff = 0;
		int pre_row = qwerty[txt[0]].first;
		int pre_col = qwerty[txt[0]].second;
		int idx = 1;
		
		while(txt[idx]) {
			int row = qwerty[txt[idx]].first;
			int col = qwerty[txt[idx]].second;
			
			int diff_row = abs(row - pre_row);
			int diff_col = abs(col - pre_col);
			
			// ↔ direction
			if (diff_row == 0) {
				total_diff += diff_col;
			}
			// ↕ direction
			else if (diff_col == 0) {
				total_diff += diff_row;
			}
			// ↙ direction
			else if (col < pre_col && row > pre_row) {
				total_diff += max(diff_row, diff_col);
			}
			// ↗ direction
			else if (col > pre_col && row < pre_row) {
				total_diff += max(diff_row, diff_col);
			}
			// ↘ direction
			else if (col > pre_col && row > pre_row) {
				total_diff += diff_row + diff_col;
			}
			// ↖ direction
			else {
				total_diff += diff_row + diff_col;
			}
# if DEBUG
			cout << "row: " << row << " col: " << col
				<< " diff_row: " << diff_row << " diff_col: " << diff_col
				<< " idx: " << idx << " total_diff: " << total_diff << endl;
# endif
			++idx;
			pre_row = row;
			pre_col = col;
		} // -> while
		
		// print result
		cout << idx + total_diff * 2 << endl;
	} // -> for
} // -> main
