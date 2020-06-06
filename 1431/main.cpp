#include <iostream>
#include <string.h>

#define MAX_N 1000
#define MAX_LEN 51
#define DEBUG 1

using namespace std;

int changeAB(char** A, char** B);
int arrange(int N, char** guitar);
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

// bubble sort
int arrange(int N, char** guitar) {
    for (int i = 0; i < N-1; i++) {
        for(int j = 0; j < N-1; j++) {
            if(rule1(&(guitar[j]), &(guitar[j+1]))) {
                changeAB(&(guitar[j]), &(guitar[j+1]));
            }
        }
    }
}

// short length first
int rule1(char** A, char** B) {
    int LA = strlen(*A), LB = strlen(*B);
    // can not distinguish with rule1
    if (LA == LB) {
        if (rule2(A, B)) {
            changeAB(A, B);
        }
        return 0;
    }
    else {
        return LA < LB ? 0 : 1;
    }
}

// smaller sum first
int rule2(char** A, char** B) {
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

    if (sumA < sumB) {
        return 0;
    }
    else if (sumA == sumB) {
        if (rule3(A,B)) {
            changeAB(A, B);
        }
        return 0;
    }
    return 1;
}

// dictionary order
int rule3(char** A, char** B) {
    int result = strcmp(*A, *B);
    if (result < 0) {
        return 0;
    }
    else if(result > 0) {
        changeAB(A, B);
        return 0;
    }
    else {
        // impossible case, becuase of input restriction 'no same serial number is allowed'
    }
}

int main(void) {
    int N;
    char* guitar[MAX_N];
    for (int i = 0; i < MAX_N; i++) {
        guitar[i] = new char[MAX_LEN];
    }

    cin >> N;
    
    for (int i = 0; i < N; i++) {
        cin >> guitar[i];
    }

    arrange(N, guitar);

    for (int i = 0; i < N; i++) {
        cout << guitar[i] << endl;
    }
    return 0;
}
