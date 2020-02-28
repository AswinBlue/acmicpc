#include <iostream>

using namespace std;
int main(void) {
	int N;
	cin >> N;
	long long D[31] = {1, 0, 3, 0};
	for (int i = 4; i <= 30; i += 2) {
		D[i] = D[i - 2] * 3;
		for(int j = i; j >= 4; j -= 2) {
			D[i] += D[j - 4] * 2;
		}
	}

	if (N % 2 == 0) {
		cout << D[N] << endl;
	}
	else {
		cout << 0 << endl;
	}

}

