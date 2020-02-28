//https://www.acmicpc.net/problem/1022
//소용돌이 예쁘게 출력하기

#include<iostream>

using namespace std;

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int r1, r2, c1, c2;
	cin >> r1 >> c1 >> r2 >> c2;

	int row = r2 - r1, col = c2 - c1;
	int** arr = new int*[row+1];
	for (int i = 0; i <= row; ++i)
		arr[i] = new int[col+1];

	int max_i;
	for (int p = 0, i = 1; true; p += i, ++i)
	{
		if (i >= abs(r1) && i >= abs(r2) && i >= abs(c1) && i >= abs(c2)) {
			max_i = i;
			break;
		}
	}

	//fill the arr
	int val = 1;
	int cur_x, cur_y;

	//move the coordinate
	r2 -= r1;
	c2 -= c1;

	cur_x = -r1;
	cur_y = -c1;

	for (int i = 0; i <= max_i; ++i) {

		if (i == 0) {
			if (0 <= cur_x && cur_x <= r2 && 0 <= cur_y && cur_y <= c2)
				arr[cur_x][cur_y] = 1;//1
			++cur_y;
		}
		else if (i == 1) {
			if (0 <= cur_x && cur_x <= r2 && 0 <= cur_y && cur_y <= c2) {
				arr[cur_x][cur_y] = 2;//2
			}
			--cur_x;
			if (0 <= cur_x && cur_x <= r2 && 0 <= cur_y && cur_y <= c2){
				arr[cur_x][cur_y] = 3;//3
			}
			--cur_y;
			if (0 <= cur_x && cur_x <= r2 && 0 <= cur_y && cur_y <= c2) {
				arr[cur_x][cur_y] = 4;//4
			}
			--cur_y;
			if (0 <= cur_x && cur_x <= r2 && 0 <= cur_y && cur_y <= c2) {
				arr[cur_x][cur_y] = 5;//5
			}
			++cur_x;
			if (0 <= cur_x && cur_x <= r2 && 0 <= cur_y && cur_y <= c2) {
				arr[cur_x][cur_y] = 6;//6
			}
			++cur_x;
			if (0 <= cur_x && cur_x <= r2 && 0 <= cur_y && cur_y <= c2) {
				arr[cur_x][cur_y] = 7;//7
			}
			++cur_y;
			if (0 <= cur_x && cur_x <= r2 && 0 <= cur_y && cur_y <= c2) {
				arr[cur_x][cur_y] = 8;//8
			}
			++cur_y;
			if (0 <= cur_x && cur_x <= r2 && 0 <= cur_y && cur_y <= c2) {
				arr[cur_x][cur_y] = 9;//9
			}
			++cur_y;
			val = 10;
		}
		else {
			//↑ 
			//do untill k < 2i-1
			// !! different with the others below !!
			
			for (int k = 0; k < 2*i-1; ++k) {
				if (0 <= cur_x && cur_x <= r2 && 0 <= cur_y && cur_y <= c2)
					arr[cur_x][cur_y] = val;
				++val;
				--cur_x;
			}
			//←
			for (int k = 0; k < 2*i; ++k) {
				if (0 <= cur_x && cur_x <= r2 && 0 <= cur_y && cur_y <= c2)
					arr[cur_x][cur_y] = val;
				++val;
				--cur_y;
			}
			//↓
			for (int k = 0; k < 2*i; ++k) {
				if (0 <= cur_x && cur_x <= r2 && 0 <= cur_y && cur_y <= c2)
					arr[cur_x][cur_y] = val;
				++val;
				++cur_x;
			}
			//→
			//do until k <= 2*i
			// !! different with the others above !!
			for (int k = 0; k <= 2*i; ++k) {
				if (0 <= cur_x && cur_x <= r2 && 0 <= cur_y && cur_y <= c2)
					arr[cur_x][cur_y] = val;
				++val;
				++cur_y;
			}
		}
	}

	//find max number
	int max_num = arr[0][0];
	if (max_num < arr[0][col])
		max_num = arr[0][col];
	if (max_num < arr[row][0])
		max_num = arr[row][0];
	if (max_num < arr[row][col])
		max_num = arr[row][col];

	int digit;
	for (digit = 0; max_num > 0; max_num /= 10, ++digit);

	for (int i = 0; i <= row; ++i) {
		for (int j = 0; j <= col; ++j) {
			int space, tmp = arr[i][j];
			for (space = digit; tmp > 0; tmp /= 10, --space) {
				int tm = 0;
			}
			for(int k=0;k<space;++k)
				cout << " ";
			cout << arr[i][j];
			if (j != col)
				cout << " ";
		}
		cout << "\n";
	}

}