// https://www.acmicpc.net/problem/1620

// this source code timeout
#include<iostream>
#include<unordered_map>
#include<string>

#define MAX_N_M 100000
#define MAX_NAME 20

using namespace std;

typedef unordered_map<string, int> Pocketmon;

int main(void) {
    int N, M;
    cin >> N >> M;

    Pocketmon map_str;
    string map_int[MAX_N_M + 1];
    
    for (int i = 1; i <= N; i++) {
        string tmp;
        cin >> tmp;
        map_int[i] = tmp;
        map_str.insert(Pocketmon::value_type(tmp, i));
    }

    for (int i = 0; i < M; i++) {
        string question;
        int flag = 0;
        cin >> question;

        if (question[0] >= '0' && question[0] <= '9') {
            int num = stoi(question);
            cout << map_int[num] << endl;
        }
        else {
            cout << map_str[question] << endl;
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
