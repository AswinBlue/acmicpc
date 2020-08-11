// https://www.acmicpc.net/problem/1431

#include <iostream>
#include <string.h>
#include <algorithm>

#define MAX_N 1000
#define MAX_LEN 51
#define DEBUG 1

using namespace std;

int N;

void quickSort(int left, int right, char** guitar);
int rule1(char* A, char* B);
int rule2(char* A, char* B);
int rule3(char* A, char* B);

// short length first
int rule1(char* A, char* B) {
# if DEBUG
    cout << "rule1 " << A << " " << B << endl;
# endif
    int LA = strlen(A), LB = strlen(B);
    // can not distinguish with rule1
    if (LA == LB) {
        return rule2(A, B);
    }
# if DEBUG
    cout << (LA < LB) << endl;
# endif
    return LA < LB;
}

// smaller sum first
int rule2(char* A, char* B) {
# if DEBUG
    cout << "rule2 " << A << " " << B << endl;
# endif
    int sumA = 0, sumB = 0;

    for (int i = 0; i < strlen(A); i++) {
        if (A[i] >= '0' && A[i] <= '9'){
            sumA += A[i] - '0';
        }
    }

    for (int i = 0; i < strlen(B); i++) {
        if (B[i] >= '0' && B[i] <= '9'){
            sumB += B[i] - '0';
        }
    }
# if DEBUG
    cout << "sumA : " << sumA << " sumb " << sumB << endl;
# endif
    
    if (sumA == sumB) {
        return rule3(A, B);
    }
    return sumA < sumB;
}

// dictionary order
int rule3(char* A, char* B) {
# if DEBUG
    cout << "rule3 " << A << " " << B << endl;
# endif
    int result = strcmp(A, B);
# if DEBUG
    cout << result << endl;
# endif
    return result < 0;
    // result == 0 is impossible case, becuase of input restriction 'no same serial number is allowed'
}

int main (void) {
    char* guitar[MAX_N];
    for (int i = 0; i < MAX_N; i++) {
        guitar[i] = new char[MAX_LEN];
    }

    cin >> N;
    
    for (int i = 0; i < N; i++) {
        cin >> guitar[i];
    }

    sort(guitar, guitar + N, rule1);

    for (int i = 0; i < N; i++) {
        cout << guitar[i] << endl;
    }
    return 0;
}
