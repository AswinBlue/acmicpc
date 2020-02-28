//https://www.acmicpc.net/problem/2292
//¹úÁý
#include<iostream>

using namespace std;

class Coordinate {
public:
	int x;
	int y;
	int z;
};

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int a;
	cin >> a;

	// ¥Òi = p
	// hexagon '6 * p + 1'is the top number block 
	// the distance from itself to block '1' is same as the block 'a'
	int i, p;
	for (p = 1, i = 2; 6 * p + 1 < a; p += i, ++i);

	if (a == 1)
		i = 1;

	cout << i;
}