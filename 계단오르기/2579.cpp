//https://www.acmicpc.net/problem/2579

#include<iostream>

#define MAX_VAL 300
using namespace std;


int weight[MAX_VAL + 1];
//bool check[MAX_VAL + 1]; // no need
int sum[MAX_VAL + 1];//** important, max value for stairs

int main() {
	int num;

	cin >> num;
	for (int i=1; i <= num; ++i) {
		cin >> weight[i];
	}

	sum[1] = weight[1];
	sum[2] = weight[1] + weight[2];
	int t1, t2;
	t1 = weight[1] + weight[3];
	t2 = weight[2] + weight[3];
	t1 > t2 ? sum[3] = t1 : sum[3] = t2;

	for (int i = 2; i <= num; ++i) {
		/* wrong approach
		if (check[i - 2] == true) {
			if (weight[i] > weight[i - 1]) {
				sum[i] += weight[i];
				check[i] = true;
				check[i + 1] = false;
			}
			else {
				sum[i] += weight[i - 1];
				check[i] = false;
				check[i + 1] = true;
			}
			++i;
		}
		else {

		}
		*/


		//마지막을 포함하는 경우의 수 두 가지
		t1 = weight[i] + weight[i - 1] + sum[i - 3];
		t2 = weight[i] + sum[i - 2];
		t1 > t2 ? sum[i] = t1 : sum[i] = t2;
	}

	cout << sum[num] << endl;
}