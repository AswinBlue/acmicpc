#include <stdio.h>
#define DEBUG 1


int map[510][510] = {};
int visit[510][510] = {};
int M, N;

typedef struct saveMap{
	int x;
	int y;
}saveMap;

saveMap make_saveMap(int x, int y){
	saveMap temp;
	temp.x = x; temp.y = y;
	return temp;
}

int serch(int x, int y){

	int vect_x[5] = { 0, 1, 0, -1, 0 };
	int vect_y[5] = { 0, 0, 1, 0, -1 };

	if (x == N && y == M)
		return 1;
	if (visit[x][y]) return visit[x][y];
	for (int i = 1; i <= 4; i++){
		int nextX = x + vect_x[i];
		int nextY = y + vect_y[i];
		if (map[nextX][nextY] < map[x][y] && nextX>0 && nextX <= N && nextY>0 && nextY <= M){
			visit[x][y] += serch(nextX,nextY);
		}
	}
#if DEBUG
	printf("%d %d\n",x,y);
	for (int a = 1; a <= M; a++) {
		for (int b = 1; b <= N; b++) {
			printf("%d ",visit[a][b]);
		}
		printf("\n");
	}
	printf("\n");
#endif

	return visit[x][y];
}
int main(void){

	scanf("%d %d", &M, &N);

	for (int i = 1; i <= M; i++)
		for (int j = 1; j <= N; j++)
			scanf("%d", &map[i][j]);


	printf("%d\n", serch(1,1));
	return 0;
}


