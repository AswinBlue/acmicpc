#include <iostream>

using namespace std;

int main(void) {
    int T;
    cin >> T;
    int price2017[101] = {0, 500, 300, 200, 50, 30, 10,};
    int price2018[65] = {0, 512, 256, 128, 64, 32,};

    for (int t = 0; t < T; t++) {
        int A, B;
        cin >> A >> B;

        cout << price2017[A] + price2018[B] << endl;
    } // -> for t 
}