#include<iostream>
#include<map>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N;
    cin >> N;

    map<string, bool> status;
    vector<string> result;

    for (int i = 0; i < N; i++) {
        string name, where;
        cin >> name >> where;
        if (where == "enter") {
            status[name] = true;
        }
        else {
            status[name] = false;
        }
    }


    map<string, bool>::iterator it; // auto it = status.begin()
    for (it = status.begin(); it != status.end(); it++) {
        if (it->second) {
            result.push_back(it->first);
        }
    }

    sort(result.begin(), result.end(), greater<string>());

    vector<string>::iterator iter;
    for (iter = result.begin(); iter != result.end(); iter++) {
        cout << *iter << endl;
    }
    return 0;
}
