// https://www.acmicpc.net/problem/1074

#include<iostream>

#define DEBUG 1

using namespace std;

int arr[2][2] = {{0, 1}, {2, 3}};

int square(int n) {
    if (n <= 0) return 1;

    int res = 1;
    for (int i = 0; i < n; i++) {
        res *= 4;
    }
    return res;
}

int solve(int N, int row, int col) {
    if (N < 1) {
        return 0;
    }
    int mask = 1 << (N - 1);
    int r = (row & mask) > 0 ? 1 : 0;
    int c = (col & mask) > 0 ? 1 : 0;
    int result = solve(N - 1, row, col) + (arr[r][c] * square(N - 1));
#if DEBUG
    cout << "N : " << N << "\nrow : " << row << "\ncol : " << col << "\nr : " << r << "\nc : " << c << "\nsquare : " << square(N-1) << "\narr[r][c] : " << arr[r][c] << "\nresult : " << result << endl;
#endif
    return result;
}

int main(void) {
    int N, r, c; // N <= 15; 0 <= r,c < 2^N-1;
    cin >> N >> r >> c;

    cout << solve(N, r, c) << endl;

    return 0;
}
