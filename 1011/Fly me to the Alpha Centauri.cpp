//https://www.acmicpc.net/problem/1011
//Fly me to the Alpha Centauri

#include<iostream>

using namespace std;

int permutation(int x);
int main()
{
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int n, start, finish;
	cin >> n;
	while (n > 0) {
		--n;
		cin >> start >> finish;
		int result;
		int dist = finish - start;
		int half_dist = (finish - start) / 2;

		int i, p;
		for (i = 1, p = 0; p <= half_dist; p += i, ++i) {
			int leftover = dist - 2 * p;
			if (leftover <= 2 * i) {
				if (leftover > i) {
					result = 2 * i;
					break;
				}
				else {
					//if (dist - 2 * p <= (i + 1))
					result = 2 * i - 1;
					break;
				}
			}
		}
		cout << result << "\n";
	}

}