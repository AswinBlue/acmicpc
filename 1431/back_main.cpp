// https://www.acmicpc.net/problem/1431

#include <iostream>
#include <string.h>

#define MAX_N 1000
#define MAX_LEN 51
#define DEBUG 1

using namespace std;

int N;

int changeAB(char** A, char** B);
void quickSort(int left, int right, char** guitar);
int rule1(char** A, char** B);
int rule2(char** A, char** B);
int rule3(char** A, char** B);

int changeAB(char** A, char** B) {
    char* tmp = *A;
    *A = *B;
    *B = tmp;
# if DEBUG
    cout << "change '" << *A << "' with '" << *B << "'" << endl;
#endif
    return 0;
}

// quick sort
void quickSort(int left, int right, char** guitar) {
# if DEBUG
    cout << "quickSort() left : " << left << " right : " << right << endl;
#endif
    if (left < 0 || right >= N || left >= right) return;
    int start = left;
    int end = right;
    int pivot = (left + right) / 2;
    changeAB(&(guitar[left]), &(guitar[pivot]));
    pivot = left++;
    do {
        while (left <= end && rule1(&(guitar[pivot]), &(guitar[left]))) left++;
        while (right >= start && rule1(&(guitar[right]), &(guitar[pivot]))) right--;
# if DEBUG
    cout << "left : " << left << " right : " << right << endl;
# endif
        if (left <= right) {
            changeAB(&(guitar[left]), &(guitar[right]));
        }
    } while (left < right);

    changeAB(&(guitar[pivot]), &(guitar[right]));
# if DEBUG
    cout << "left : " << left << " right : " << right << endl;
    for (int i = 0; i < N;i++) {
        cout << guitar[i] << endl;
    }
#endif

    quickSort(start, right - 1, guitar);
    quickSort(right + 1, end, guitar);
}

// bubble sort -->timeout
void bubbleSort(int N, char** guitar) {
    for (int i = 0; i < N - 1; i++) {
        for(int j = 0; j < N - 1; j++) {
            if(rule1(&(guitar[j]), &(guitar[j+1]))) {
                changeAB(&(guitar[j]), &(guitar[j+1]));
            }
        }
    }
}

// short length first
int rule1(char** A, char** B) {
# if DEBUG
    cout << "rule1" << endl;
# endif
    int LA = strlen(*A), LB = strlen(*B);
    // can not distinguish with rule1
    if (LA == LB) {
        return rule2(A, B);
    }
    return LA < LB ? 0 : 1;
}

// smaller sum first
int rule2(char** A, char** B) {
# if DEBUG
    cout << "rule2" << endl;
# endif
    int sumA = 0, sumB = 0;

    for (int i = 0; (*A)[i] != '\0'; i++) {
        if ((*A)[i] >= '0' && (*A)[i] <= '9'){
            sumA += (*A)[i];
        }
    }

    for (int i = 0; (*B)[i] != '\0'; i++) {
        if ((*B)[i] >= '0' && (*B)[i] <= '9'){
            sumB += (*B)[i];
        }
    }
    
    if (sumA == sumB) {
        return rule3(A, B);
    }
    return sumA < sumB ? 0 : 1;
}

// dictionary order
int rule3(char** A, char** B) {
# if DEBUG
    cout << "rule3" << endl;
# endif
    int result = strcmp(*A, *B);
    if (result < 0) {
        return 0;
    }
    if (result > 0) {
        return 1;
    }
    else {
        // impossible case, becuase of input restriction 'no same serial number is allowed'
    }
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

    quickSort(0, N - 1, guitar);

    for (int i = 0; i < N; i++) {
        cout << guitar[i] << endl;
    }
    return 0;
}
