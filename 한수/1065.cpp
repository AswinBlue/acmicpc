//https://www.acmicpc.net/problem/1065

#include<iostream>

using namespace std;

int main() {
	int num;
	cin >> num;

	if (num > 999)
		num = 999;
	int a, b, c;
	a = num / 100;
	b = (num % 100) / 10;
	c = num % 10;

	int cnt = 0;


	if (num < 100) {
		cnt += num;
	}
	else {
		cnt += 99;
		//a00 ~ abc
		for (int i = 0; i < 5; ++i) {//i�� ������ �ϴ� ���������� ���� ���� �Ǻ�
									 //���� ����
			int A = a - i;
			if (A >= 0 && A == b) {
				A -= i;
				if (A >= 0 && A <= c) {
					cnt++;
				}
			}
			else if (A < b && A - i >= 0) {
				cnt++;
			}

			//�ߺ� ��� ����
			if (i == 0)
				continue;

			//��� ����
			A = a + i;
			if (A < 10 && A == b) {
				A += i;
				if (A < 10 && A <= c) {
					cnt++;
				}
			}
			else if (A < b && A + i < 10)
				cnt++;
		}

		//100 ~ a00 - 1
		for (int i = 1; i < a; ++i) {
			++cnt;//���� 0
			cnt += i / 2;//���� ����
			cnt += (9 - i) / 2;//��� ����
		}
	}
	cout << cnt << endl;
}