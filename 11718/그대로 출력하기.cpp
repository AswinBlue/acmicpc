//https://www.acmicpc.net/problem/11718
//�״�� ����ϱ�
#include<iostream>
#include<string>

using namespace std;

int main()
{
	string in;
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	
	//�ȵǴ� �ڵ�
	/*while (!cin.eof()) {
		cin.getline(in, 100);
		cout << in << "\n";
	}*/

	//input.open("in.txt");

	while (getline(cin, in)) {
		cout << in << "\n";
	}
}