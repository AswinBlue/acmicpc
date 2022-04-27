// https://www.acmicpc.net/problem/2178

#include <iostream>
#include <vector>
#include <queue>

#define DEBUG 0
#define MAX 999999999
using namespace std;

typedef struct coord {
    int x;
    int y;
    int step;
    int next_dir;
}coord;

int dx[4] = {0, -1, 0, 1};
int dy[4] = {1, 0, -1, 0};

void print_map(char(*map)[110], int N, int M) {
    for (int i = 0; i <= N+1; i++) {
        cout << "| ";
        for (int j = 0; j <= M+1; j++) {
            cout << (int)map[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void BFS(char (*map)[110], int N, int M) {
    queue<coord> Q;
    Q.push({1, 1, 1, 0}); // 'next_dir' is not used
    map[1][1] = 2;
    /*
     * BFS 동작
     * 1. 방문했던 경로를 체크해야 recursion이 발생하지 않는다.
     * 2. 현재 node에서 방문할 수 있는 모든 node들을 queue에 넣으면서 진행한다. 
     * 3. 이미 방문한 node들은 검사하지 않는다. (이미 방문되었다는 뜻은 더 짧은 경로가 있다는 뜻)
     * 4. 한번만 목적지를 찾으면 된다. 처음 나온 값이 최단 경로이다.
     */

    while(!Q.empty()) {
        int x = Q.front().x;
        int y = Q.front().y;
        int step = Q.front().step;
        Q.pop();

#if DEBUG
        cout << x << " " << y << " " << step << endl;
        print_map(map, N, M);
#endif

        for (int i = 0; i < 4; i++) {
            int next_x = x + dx[i];
            int next_y = y + dy[i];
            
            if (map[next_x][next_y] == 1) {
                map[next_x][next_y] = 2; // check visited
                // fastest route found
                if (next_x == N && next_y == M) {
                    cout << step + 1 << endl;
                    return;
                }
                Q.push({next_x, next_y, step+1, 0});
            }
        }
    }

}

void DFS(char (*map)[110], int N, int M) {
    // solve with DFS
    vector<coord> stack;
    stack.push_back({1, 1, 1, 0});
    int min_step = MAX;
    // bool finish = false;
    // while (!stack.empty() && !finish) {

    /* 보통 stack을 사용한 DFS는 
     * (1) stack에서 pop, 
     * (2) 가능한 다음 경로를 stack에 저장
     * 방식으로 동작하고, visit 배열을 따로 관리한다. 
     * 하지만, visit 배열 없이 map을 변경해가며 동작하도록 하였다. 
     * (1) stack에세 top 값을 가져오고 stack에서 pop, 현재 위치는 이동 불가로 표기
     * (2) 다음 경로가 있으면 현재 node에서 다음 탐색 위치를 설정해 stack에 추가, 다음 node도 stack에 추가
     * (3) 경로가 없으면 현재 위치를 이동 가능으로 복구
     */

    /*
     * DFS 동작
     * 1. 방문했던 경로를 체크해야 recursion이 발생하지 않는다.
     * 2. 더이상 갈 곳이 없으면 복귀한다
     * 3. 최종 목적지에 도달한 경우를 모아 결과값을 비교한다.
     */

    // map == 0 : blocked
    // map == 1 : can go
    // map == 2 : already visited
    while (!stack.empty()) {
        int x = stack.back().x;
        int y = stack.back().y;
        int step = stack.back().step;
        int next = stack.back().next_dir;
        stack.pop_back();

        bool found = false;

        if (next >= 4) {
            map[x][y] = 1; // restore the 'map'
            continue;
        }
        // huristic to save time
        if (step >= min_step) {
            map[x][y] = 1; // restore the 'map'
            continue;
        }
        
        map[x][y] = 2; // now searching
        
#if DEBUG
        cout << x << " " << y << " " << step << " " << next << endl;
        print_map(map, N, M);
#endif
        // check 4 directions to find way
        for (int i = next; i < 4; i++) {
            int next_x = x + dx[i];
            int next_y = y + dy[i];


            // go if (1) there is a way, and (2) not already visited
            if (map[next_x][next_y] == 1) {
                found = true;
                stack.push_back({x, y, step, i + 1}); // update direction and push into satck again
                // reach the end
                if (next_x == N && next_y == M) {
                    min_step = min(min_step, step + 1);
#if DEBUG
                    cout << "min:" << min_step << endl;
#endif
                    // finish = true;
                    // break;
                }

                // push to stack
                stack.push_back({next_x, next_y, step + 1, 0});
                break;
            }
        } // -> for 'i'

        // if no way more, restore the map
        if (!found) {
            map[x][y] = 1; // restore the 'map'
        }

    } // -> while

    cout << min_step << endl;
}

int main(void) {

    char map[110][110] = {0,};
    int N, M;

#if DEBUG
    freopen("in2.txt", "r", stdin);
#endif

    // get map size
    cin >> N >> M;

    // get inputs for map
    // set bordet as 0, get input from 1 ~ N, 1 ~ M
    for (int i = 1; i <= N; i++) {
        cin >> &(map[i][1]);
        for (int j = 1; j <= M; j++) {
            map[i][j] -= '0';
        }
    }
#if DEBUG
    cout << "map:" << N << " "  <<  M << endl;;
    print_map(map, N, M);
#endif

    BFS(map, N, M);
}