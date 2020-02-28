//https://www.acmicpc.net/problem/4963

#include<iostream>
#define STACK_SIZE 1000
using namespace std;

int** map;
int width, height;
int cnt;

void search(int x, int y) {
	if (map[x][y] != 1)
		return;

	//mark node as visited
	map[x][y] = 2;

	if (x > 0) {
		//N
		if (map[x - 1][y] == 1) {
			search(x - 1, y);
		}
		if (y > 0) {
			//NW
			if (map[x - 1][y - 1] == 1) {
				search(x - 1, y - 1);
			}
		}
		if (y < width - 1) {
			//NE
			if (map[x - 1][y + 1] == 1) {
				search(x - 1, y + 1);
			}
		}
	}
	if (x < height - 1) {
		//S
		if (map[x + 1][y] == 1) {
			search(x + 1, y);
		}
		if (y > 0) {
			//SW
			if (map[x + 1][y - 1] == 1) {
				search(x + 1, y - 1);
			}
		}
		if (y < width - 1) {
			//SE
			if (map[x + 1][y + 1] == 1) {
				search(x + 1, y + 1);
			}
		}
	}

	if (y > 0) {
		//W
		if (map[x][y - 1] == 1) {
			search(x, y - 1);
		}
	}
	if (y < width - 1) {
		//E
		if (map[x][y + 1] == 1) {
			search(x, y + 1);
		}
	}
}
int main()
{
	while (true)
	{
		cin >> width >> height;

		if (width == 0 && height == 0)
			break;

		cnt = 0;

		//create map
		map = new int*[height];
		for (int t = 0; t < height; ++t) {
			map[t] = new int[width]();
		}

		for (int i = 0; i < height; ++i) {
			for (int j = 0; j < width; ++j) {
				cin >> map[i][j];
			}
		}

		for (int i = 0; i < height; ++i) {
			for (int j = 0; j < width; ++j) {
				if (map[i][j]==1) {
					search(i, j);
					cnt++;
				}
			}
		}

		cout << cnt << endl;

		//release map
		for (int t = 0; t < height; ++t) {
			delete map[t];
		}
		delete map;
		
	}
}