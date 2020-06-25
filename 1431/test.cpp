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
        while (rule1(&(guitar[left]), &(guitar[pivot]))) left++;
        while (rule1(&(guitar[right]), &(guitar[pivot]))) right--;
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

int rule1(char** A, char** B) {
    int result = strcmp(*A, *B);
    if (result > 0) {
        return 0;
    }
    else if (result < 0) {
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
