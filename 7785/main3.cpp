#include<iostream>
#include<set>
#include<string>
#include<cstdio>

using namespace std;

int main(void) {
    int N;
    scanf("%d ", &N);

    set<string> status;

    for (int i = 0; i < N; i++) {
        string input;
        getline(cin, input);
        size_t pos = input.find("enter");
        if (pos != string::npos) {
            status.insert(input.substr(0, pos - 1));
        }
        else {
            pos = input.find("leave");
            if (pos != string::npos) {
                status.erase(input.substr(0, pos - 1));
            }
        }
    }


    set<string>::reverse_iterator it; // auto it = status.begin()
    for (it = status.rbegin(); it != status.rend(); it++) {
        cout << *it << "\n";
    }
    return 0;
}
