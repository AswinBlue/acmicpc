//1로 만들기
//https://www.acmicpc.net/problem/1463

#include<iostream>
#include<algorithm>

#define NUMBER 1000001
int calc_time[NUMBER];

//int prev_calc[NUMBER];

using namespace std;

void doCalculate(int num) {
	int next = num-1;
	if (num == 1)
		return;

//find smalles value from three cases
	//get calc_time[num-1] if not exist
	if (calc_time[num - 1] == 0) {
		doCalculate(num - 1);
	}

	if (num % 2 == 0) {
		//get calc_time[num/2] if not exist
		if (calc_time[num / 2] == 0) {
			doCalculate(num / 2);
		}
		calc_time[num/2] < calc_time[num-1] ? next = num/2 : next = num-1;
	}

	if (num % 3 == 0) {
		//get calc_time[num/3] if not exist
		if (calc_time[num / 3] == 0) {
			doCalculate(num / 3);
		}
		calc_time[num / 3] < calc_time[next] ? next = num/3 : NULL;
	}

	calc_time[num] = calc_time[next] + 1;
	
}

int main() {
	int num;
	cin >> num;

	doCalculate(num);

	for (int i = 1; i < num; ++i)
		cout << calc_time[i] << " ";

	cout << calc_time[num] << endl;
}