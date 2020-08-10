#include<iostream>
#include<map>
#include<string>
#include<algorithm>
#include<vector>
#include<cstdio>

using namespace std;

int main(void) {
    int N;
    scanf("%d ", &N);

    map<string, bool> status;
    vector<string> result;

    for (int i = 0; i < N; i++) {
        string name, where;
        getline(cin, name, ' ');
        getline(cin, where);
        if (where == "enter") {
            status[name] = true;
        }
        else {
            status[name] = false;
        }
    }


    map<string, bool>::reverse_iterator it; // auto it = status.begin()
    for (it = status.rbegin(); it != status.rend(); it++) {
        if (it->second) {
            cout << it->first << "\n";
        }
    }

    return 0;
}
