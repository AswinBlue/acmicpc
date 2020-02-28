//https://www.acmicpc.net/problem/5567

#include<iostream>

using namespace std;

class Friend {
public:
	Friend(int me, int you) {
		this->me = me;
		this->you = you;
		this->next = NULL;
	}
	int me;
	int you;
	Friend* next;
};

int main()
{
	int n, num;

	cin >> n >> num;

	//init linked list
	Friend** F = new Friend*[n + 1];
	Friend** endp = new Friend*[n + 1];
	for (int i = 1; i <= n; ++i) {
		F[i] = new Friend(i,i);
		F[i]->next = NULL;
		endp[i] = F[i];
	}

	//make friend graph with linked list
	for (int i = 0; i < num; ++i) {
		int me, you;
		cin >> me >> you;
		Friend* tmp;
		tmp = new Friend(me, you);
		endp[me]->next = tmp;
		endp[me] = tmp;

		tmp = new Friend(you, me);
		endp[you]->next = tmp;
		endp[you] = tmp;
	}

	//count friends to invite
	int cnt = 0;
	Friend* ptr = F[1]->next;
	bool* invite = new bool[n + 1]();
	invite[1] = true;
	bool* friend_of_1 = new bool[n+1]();

	while (ptr) {
		friend_of_1[ptr->you] = true;
		invite[ptr->you] = true;
		cnt++;
		ptr = ptr->next;
	}

	for (int i = 2; i <= n; ++i) {
		if (friend_of_1[i]) {
			ptr = F[i]->next;
			while (ptr) {
				if (!invite[ptr->you]) {
					cnt++;
					invite[ptr->you] = true;
				}
				ptr = ptr->next;
			}
		}
	}

	cout << cnt << endl;
}