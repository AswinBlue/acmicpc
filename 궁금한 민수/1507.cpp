//https://www.acmicpc.net/problem/1507

#include<iostream>

using namespace std;

int main()
{
	int num;
	cin >> num;

	int ** road = new int*[num];

	for (int i = 0; i < num; ++i) {
		road[i] = new int[num];
		for (int j = 0; j < num; ++j) {
			cin >> road[i][j];
		}
	}

	int sum = 0;
	for (int i = 0; i < num; ++i) {
		for (int j = i + 1; j < num; ++j) {
			for (int k = 0; k < num; ++k) {
				if (k != i && k != j) {
					if (road[i][j] > road[i][k] + road[k][j]) {
						cout << -1 << endl;
						return 0;
					}
					else if (road[i][j] == road[i][k] + road[k][j]){
						sum -= road[i][j];//road[i][j]�� üũ�ϸ� �޸𸮰� ���� ���. �ٷ� sum�� ������
						break;//�������� k�� ���� ����, �ѹ��̶� �����ϸ� �Ѿ��. 
					}
				}
			}
			sum += road[i][j];
		}
	}
	cout << sum << endl;
}