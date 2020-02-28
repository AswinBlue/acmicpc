#include<iostream>
#include<set>
#define MAX 100000000000000
using namespace std;

// slide all 'P' and 'Q' to one click right
void moveRight(int* left, int* right, int* p, int* q, int* start) {
	*left += *p; // +(start+p) -start
	*right += *q; // +(start+p+q) -(start+p)
	(*start)++;
}
// expand 'P'
void expandP(int* left, int* right, int* p, int* q, int* start) {
	*left += *start + *p;
	*right += *q;
	(*p)++;
}
//TODO : 음수의 경우를 추가로 생각해 주어야 한다
set<int> doSum(int p, int q, int start, set<int> result) {

	//left-hand side, sum of 'p' numbers
	int left = p * (p + 1) / 2 + (start - 1) * p;
	// left = Σ(start ~ p)

	//right-hand side, sum of 'q' numbers
	int right = q * (q + 1) / 2 + q * p;
	// right = Σ(p ~ p+q)

	// P = [start:start+p-1], Q = [start+p:start+p+q-1]

	// check if the 'p' meets the condition
	if (left == right) {
		result.insert(p);
		//moveRight(&left, &right, &p, &q, &start);

	}
	else if(left < right){
		//expandP(&left, &right, &p, &q, &start);
		set<int> s;
		s = doSum(p + 1, q, start, result);
		result.insert(s.begin(), s.end());
		//moveRight(&left, &right, &p, &q, &start);
		s = doSum(p, q, start + 1, result);
		result.insert(s.begin(), s.end());
	}
	return result;
}
int main()
{
	while (true) {
		int q;
		cin >> q;
		
		if (q == 0)
			break;

		int p = q + 1;
		// 'start' is the first number of 'P'
		int start = 1;
		set<int> r;
		int result = doSum(p, q, start, r).size();
		cout << result << endl;
	}
}
/*
< 2차시도>
// x-p ... x-q ... x-3 x-2 x-1 x x+1 x+2 ... x+q-1
// x = { Σ(q-1) + Σ(p) } / (p-q)

int sum = 0, result = 0;
// P = Σ(p),  Q = Σ(q)
int Q = 0, P = 0;

for (int i = 1; i < q; ++i) {
P += i;
Q += i;
}
P += q;
// at this moment, P = Q + q

//find 'p' from q+1
for (int i = q + 1; true; ++i) {
P += i;
double X = (P + Q) / (i - q);

// find X until
// i * X - P > Q + q * X
if (X < 0) break;
int x = X;
if (X == x)
result++;
}
*/

/*
<1차 시도>
for (int i = q + 1; true; ++i) {
sum += i;
if (sum / (i - q) < 1) {
break;
}
else if (sum % (i - q) == 0) {
result++;
cout << "'" << sum / (i - q) << "' ";
}
}
*/