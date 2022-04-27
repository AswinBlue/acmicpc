// https://www.acmicpc.net/problem/15997
// 승부예측

#include <iostream>
#include <map>
#include <algorithm>

#define DEBUG 0

using namespace std;

int main(void) {
    map<string, int> name;
    string tmp;

#if DEBUG
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
#endif
    
    // get input

    for (int i = 0; i < 4; i++) {
        cin >> tmp;
        // name[tmp] = i;
        name.insert({tmp, i});
    }

    // save game score and chance
    double res1[730][5] = {{0,0,0,0,1},};
    double res2[730][5] = {{0,0,0,0,1},};
    int size = 1; // used memory size
    bool flag = 0; // for memory switching

    for (int i = 0; i < 6; i++, size *= 3, flag = !flag) {
        int A, B;
        cin >> tmp;
        A = name[tmp];
        cin >> tmp;
        B = name[tmp];
        double W, L, D;
        cin >> W >> D >> L;
#if DEBUG
        cout << "  \t>>input" << i << ":" << A << " " << B << " " << W << " " << D << " " << L << "\n";
#endif
        // calculate chance for all case
        for (int j = 0; j < size; j++) {
            int current = j * 3;
            if (flag) {
# if DEBUG
                if (res2[j][4] == 0.0)
                    cout << "zero1:" ;
                else
                    cout << "\t";

                cout << j << ":" << res2[j][0] << " " << res2[j][1] << " " << res2[j][2] << " " << res2[j][3] << " " << res2[j][4] <<"\n";
#endif
                memcpy(res1[current], res2[j], sizeof(double) * 5); // copy data
                memcpy(res1[current+1], res2[j], sizeof(double) * 5); // copy data
                memcpy(res1[current+2], res2[j], sizeof(double) * 5); // copy data
                if (res2[j][4] == 0.0) continue;

                // A win
                res1[current][A] += 3;
                res1[current][4] *= W;
                // B win
                res1[current + 1][B] += 3;
                res1[current + 1][4] *= L;
                // tie
                res1[current + 2][A] += 1;
                res1[current + 2][B] += 1;
                res1[current + 2][4] *= D;
            } else {
#if DEBUG
                if (res1[j][4] == 0.0) 
                    cout << "zero2:";
                else
                    cout << "\t\t";
                cout << j << ":" << res1[j][0] << " " << res1[j][1] << " " << res1[j][2] << " " << res1[j][3] << " "  << res1[j][4] << "\n";
#endif
                memcpy(res2[current], res1[j], sizeof(double) * 5); // copy data
                memcpy(res2[current+1], res1[j], sizeof(double) * 5); // copy data
                memcpy(res2[current+2], res1[j], sizeof(double) * 5); // copy data
                if (res1[j][4] == 0.0) continue;

                // A win
                res2[current][A] += 3;
                res2[current][4] *= W;
                // B win
                res2[current + 1][B] += 3;
                res2[current + 1][4] *= L;
                // tie
                res2[current + 2][A] += 1;
                res2[current + 2][B] += 1;
                res2[current + 2][4] *= D;
            }
        } // -> for j
    }

#if DEBUG
    cout << "finding all case done-----------------------------------\n";
    for (int j = 0; j < 729; j++)
        cout << j << ":" << res1[j][0] << " " << res1[j][1] << " " << res1[j][2] << " " << res1[j][3] << " "  << res1[j][4] << "\n";
#endif

    // by calculated game result, we can get final chance
    double chance[4] = {0,};

    // final result is in 'res1', because 6 is even
    for (int i = 0; i < 729; i++) {
        // get 2 team with highest score
        // if there is team with same score, draw lots fairly

        // skip with 0 chance
        if (res1[i][4] == 0) continue;
        
        int score[4] = {0,};
        int idx[4] {0, 1, 2, 3};
        // possible score : 9 7 6 5 4 3 1
        for (int j = 0; j < 4; j++) {
            score[j] = (int)res1[i][j];
        }
        // sort
        stable_sort(idx, idx + 4, [&score](int a, int b) {return score[a] > score[b];});
        stable_sort(score, score + 4, [](int a, int b) {return a > b;});
#if DEBUG
        cout << "\n" << i << ":";
        for (int j = 0; j < 5; j++) {
            cout << res1[i][j] << " ";
        }
        cout << "\n";
        cout << idx[0] << " " << idx[1] << " " << idx[2] << " " << idx[3] << " / " << score[0] << " " << score[1] << " " << score[2] << " " << score[3] << "\n";
#endif
        // check even score until find 2 most highest score
        int ranked = 0;
        int even = 1;
        for (int j = 1; j < 4; j++) {

            if (score[j] == score[j - 1]) {
                // memorize even score member
                even++;
            }
            else {
                // update ranker value
                ranked += even;
                even = 1;
            }
            
            if (ranked >= 2) break; // no need to do more
        } // for j

        if (ranked == 0) {
            // random select 2 from 4
            chance[0] += res1[i][4] / 2;
            chance[1] += res1[i][4] / 2;
            chance[2] += res1[i][4] / 2;
            chance[3] += res1[i][4] / 2;
        } else if (ranked == 1) {
            chance[idx[0]] += res1[i][4];
            // random select 1 from 3
            chance[idx[1]] += res1[i][4] / 3;
            chance[idx[2]] += res1[i][4] / 3;
            chance[idx[3]] += res1[i][4] / 3;
        } else if (ranked == 2) {
            // just pick
            chance[idx[0]] += res1[i][4];
            chance[idx[1]] += res1[i][4];
        } else if (ranked == 3) {
            if (score[0] > score[1]) {
                chance[idx[0]] += res1[i][4];
                // random select 1 from 2
                chance[idx[1]] += res1[i][4] / 2;
                chance[idx[2]] += res1[i][4] / 2;
            } else {
                // random select 2 from 3
                chance[idx[0]] += res1[i][4] * 2 / 3;
                chance[idx[1]] += res1[i][4] * 2 / 3;
                chance[idx[2]] += res1[i][4] * 2 / 3;
            }
        } else if (ranked >= 4) {
            // infeasible case
        }
#if DEBUG
        cout << "ranked : " << ranked << "\n";
        for (int k = 0; k < 4; k++) {
            cout << chance[k] << " ";
        }
        cout << "\n";
#endif
    } // -> for i

#if DEBUG
    cout << "chance adding done-----------------------------------\n";
#endif

    for (int i = 0; i < 4; i++) {
        cout << chance[i] << "\n";
    }

}
