//https://www.acmicpc.net/problem/1182

#include<iostream>

using namespace std;

int result = 0, num, S, *arr;
void findSet(int cur, int group_size, int selected, int sum) {
	//check sum
	if (sum == S && group_size == selected)
		result++;
	//finish condition
	if (selected >= group_size || cur >= num)
		return;

	findSet(cur + 1, group_size, selected + 1, sum + arr[cur]);
	findSet(cur + 1, group_size, selected, sum);

}
int main()
{
	cin >> num >> S;

	arr = new int[num];
	for (int i = 0; i < num; ++i)
		cin >> arr[i];

	for (int i = 1; i <= num; ++i)
		findSet(0, i, 0, 0);

	cout << result << endl;
}
