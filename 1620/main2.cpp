// https://www.acmicpc.net/problem/1620
#include<iostream>
#include<vector>
#include<string>

#define MAX_N_M 100000
#define MAX_NAME 20

#define DEBUG 0

using namespace std;

typedef struct Pocketmon {
    string str;
    int num;
}Pocketmon;

void qSort(Pocketmon* p, int start, int end) {
   int left = start;
   int right = end;
   int pivot = left++;
   if (start >= end) return;
   do {
       while (left <= end && p[left].str < p[pivot].str) left++;
       while (right >= start && p[right].str > p[pivot].str) right--;
       if (left <= right) {
           Pocketmon tmp = p[left];
           p[left] = p[right];
           p[right] = tmp;
       }
   }while (left < right);

   Pocketmon tmp = p[pivot];
   p[pivot] = p[right];
   p[right] = tmp;

   qSort(p, start, right - 1);
   qSort(p, right + 1, end);
}

int search(Pocketmon* p, int start, int end, string q) {
    if (start > end) return -1;

    int mid = (start + end) / 2;
    if (p[mid].str == q) {
        return p[mid].num;
    }
    else if (p[mid].str > q) {
        return search(p, start, mid - 1, q);
    }
    else {
        return search(p, mid + 1, end, q);
    }

    return -1;
}

int main(void) {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N >> M;

    Pocketmon map_str[MAX_N_M + 1];
    string map_int[MAX_N_M + 1];
    
    for (int i = 1; i <= N; i++) {
        string tmp;
        cin >> tmp;
        map_int[i] = tmp;
        map_str[i].str = tmp;
        map_str[i].num = i;
    }

#if DEBUG
    cout << "<<before qsort>>" << endl;
    for (int i = 1; i <= N; i++) {
        cout << i + " " + map_str[i].str << endl;
    }
#endif

    // sort array
    qSort(map_str, 1, N);

#if DEBUG
    cout << "<<after qsort>>" << endl;
    for (int i = 1; i <= N; i++) {
        cout << i + " " + map_str[i].str << endl;
    }
#endif

    for (int i = 0; i < M; i++) {
        string question;
        int flag = 0;
        cin >> question;

        // if number came
        if (question[0] >= '0' && question[0] <= '9') {
            int num = stoi(question);
            cout << map_int[num] << endl;
        }
        // if string came
        else {
            cout << search(map_str, 1, N, question) << endl;
        }
            
        /*
        for (int j = 0; j < question.length(); j++) {
            if (!isdigit(question[j])){ // not digit
                flag = 1;
                break;
            }
        }

        if (flag) {
            cout << map_str[question] << endl;
        }
        else {
            int num = stoi(question);
            cout << map_int[num] << endl;
        }
        */
    }
    return 0;
}
