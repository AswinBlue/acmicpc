//https://www.acmicpc.net/problem/6684
//Hexagonal Routes
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

#define ARRSIZE 100

void factorial(int *arr, int x);

//axis x: ¢Ù
//axis y: ¢Ö
//axis z: ¡è
class Coordinate {
public:
	int x;
	int y;
	int z;
};

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	while (true) {
		int a, b;
		cin >> a >> b;

		if (a == 0 && b == 0)
			break;

		//make b bigger than a
		if (a > b) {
			int cnt = a;
			a = b;
			b = cnt;
		}

		// ¥Òi = p
		// 6 * p + 1 = 1,7,19, ... (cells under 'number 1' cell)
		// i_a will be distance from cell 1 to cell a
		// p_a will be biggest number cell which has same distance (from 1 to the cell) with a
		// i_b, p_b are same as above
		int i_a , p_a, p_b, i_b;
		for (p_a = 0, i_a = 0; 6 * p_a + 1 < a; ++i_a, p_a = p_a + i_a);
		for (p_b = 0, i_b = 0; 6 * p_b + 1 < b; ++i_b, p_b = p_b + i_b);
	
		p_a = 6 * p_a + 1;
		p_b = 6 * p_b + 1;

		//calculate coordination of a
		int diff = p_a - a;
		int cnt;
		//divide by 0 exception
		if (i_a != 0)
			cnt = diff / i_a;
		else
			cnt = 0;

		Coordinate A;
		A.x = 0;
		A.y = 0;
		A.z = -i_a;

		if (cnt == 0) {
			//divide by 0 exception
			if (i_a != 0)
				A.y += diff % i_a;
		}
		else if (cnt > 0) {
			A.y += i_a;
			cnt--;


			if (cnt == 0) {
				A.z += diff % i_a;
			}
			else if (cnt > 0) {
				A.z += i_a;
				cnt--;


				if (cnt == 0) {
					A.x -= diff % i_a;
				}
				else if (cnt > 0) {
					A.x -= i_a;
					cnt--;


					if (cnt == 0) {
						A.y -= diff % i_a;
					}
					else if (cnt > 0) {
						A.y -= i_a;
						cnt--;


						if (cnt == 0) {
							A.z -= diff % i_a;
						}
						else if (cnt > 0) {
							A.z -= i_a;
							cnt--;


							if (cnt == 0) {
								A.x += diff % i_a;
							}
						}
					}
				}
			}
		}

		//calculate coordination of b
		diff = p_b - b;

		//divide by 0 exception
		if (i_b != 0)
			cnt = diff / i_b;
		else
			cnt = 0;

		Coordinate B;
		B.x = 0;
		B.y = 0;
		B.z = -i_b;

		if (cnt == 0) {
			//divide by 0 exception
			if (i_b != 0)
				B.y += diff % i_b;
		}
		else if (cnt > 0) {
			B.y += i_b;
			cnt--;


			if (cnt == 0) {
				B.z += diff % i_b;
			}
			else if (cnt > 0) {
				B.z += i_b;
				cnt--;


				if (cnt == 0) {
					B.x -= diff % i_b;				}

				else if (cnt > 0) {
					B.x -= i_b;
					cnt--;


					if (cnt == 0) {
						B.y -= diff % i_b;
					}
					else if (cnt > 0) {
						B.y -= i_b;
						cnt--;


						if (cnt == 0) {
							B.z -= diff % i_b;
						}
						else if (cnt > 0) {
							B.z -= i_b;
							cnt--;


							if (cnt == 0) {
								B.x += diff % i_b;
							}
						}
					}
				}
			}
		}

		//calculate distance
		int X = A.x - B.x;
		int Y = A.y - B.y;
		int Z = A.z - B.z;

		//make sum of absolute X,Y,Z the smallest
		//use these rules
		//(-n,n,0) = (0,0,n)
		//(n,0,n) = (0,n,0)
		//(0,-n,-n) = (n,0,0)

		//(-n,n,0) = (0,0,n)
		if ((X < 0 && Y > 0) || (X > 0 && Y < 0)) {
			if (abs(X) > abs(Y)) {
				if (Y > 0)
					Z += abs(Y);
				else
					Z -= abs(Y);
				X += Y;
				Y = 0;
			}
			else {
				if (X < 0)
					Z += abs(X);
				else
					Z -= abs(X);
				Y += X;
				X = 0;
			}
		}

		//(n,0,n) = (0,n,0)
		if ((X > 0 && Z > 0) || (X < 0 && Z < 0)) {
			if (abs(X) > abs(Z)) {
				if (Z > 0)
					Y += abs(Z);
				else
					Y -= abs(Z);
				X -= Z;
				Z = 0;
			}
			else {
				if (X > 0)
					Y += abs(X);
				else
					Y -= abs(X);
				Z -= X;
				X = 0;
			}
		}

		//(0,n,-n) = (n,0,0)
		if ((Y > 0 && Z < 0) || (Y < 0 && Z > 0)) {
			if (abs(Y) > abs(Z)) {
				if (Z < 0)
					X += abs(Z);
				else
					X -= abs(Z);
				Y += Z;
				Z = 0;
			}
			else {
				if (Y > 0)
					X += abs(Y);
				else
					X -= abs(Y);
				Z += Y;
				Y = 0;
			}
		}

		X = abs(X);
		Y = abs(Y);
		Z = abs(Z);
		int length = X + Y + Z;

		//route = length ! / (X! * Y! * Z!)
		/*
		int route_arr[ARRSIZE] = { 1,0, };
		int denominator_arr[ARRSIZE] = { 1,0, };
		factorial(route_arr, length);
		factorial(denominator_arr, X);
		factorial(denominator_arr, Y);
		factorial(denominator_arr, Z);

		//find the top digit of route and denominator
		int r_top = ARRSIZE-1;
		int d_top = ARRSIZE-1;
		while (route_arr[r_top] == 0)--r_top;
		while (denominator_arr[d_top] == 0)--d_top;
		
		string denominator_str = "";
		for (int i = d_top; i >= 0; --i)
			denominator_str += to_string(denominator_arr[i]);
		double denominator = atof(denominator_str.c_str());

		//do modulation
		int top = r_top;
		int bottom = r_top - d_top;
		int result[ARRSIZE] = { 0, };
		string str = "";
		for (int i = r_top; i > r_top - d_top; --i)
			str += to_string(route_arr[i]);
		for (int ptr = r_top - d_top; ptr >= 0; --ptr) {
			str += route_arr[ptr];
			double tmp = atof(str.c_str());
			int div;
			if (div = tmp / denominator) {
				result[ptr] = div;
				str = to_string(tmp - div * denominator);
				
			}
		}
		int result_top = ARRSIZE-1;
		string final_route = "";
		while (result[result_top] == 0)--result_top;
		for (int i = result_top; i >= 0; --i)
			final_route += to_string(result[i]);
		cout << final_route.c_str();
		*/
		/////////////////////////////////////////////////////
		long double route = 1;
		long double denominator = 1;		

		for (int i = length; i > 1; --i) {
			route *= i;
		}
		for (int i = X; i > 1; --i) {
			denominator *= i;
		}
		for (int i = Y; i > 1; --i) {
			denominator *= i;
		}
		for (int i = Z; i > 1; --i) {
			denominator *= i;
		}

		route = route / denominator;

		cout.precision(0);
		cout.setf(ios_base::floatfield, ios_base::fixed);
		cout << "There is " << route << " route of the shortest length " << length << ".\n";
		
		////////////////////////////////////////////////////////
		/*
		int MAX, _MAX=0;
		if (X > Y && X > Z) {
			MAX = X;
			_MAX = 1;
		}
		if (Y > X && Y > Z) {
			MAX = Y;
			_MAX = 2;
		}
		if (Z > X && Z > X) {
			MAX = Z;
			_MAX = 3;
		}

		//route = length ! / (X! * Y! * Z!)

		for (double i = length; i > MAX; --i) {
			route *= i;
		}
		switch (_MAX) {
		case 1:
			for (double i = Y; i > 1; --i) {
				denominator *= i;
			}
			for (double i = Z; i > 1; --i) {
				denominator *= i;
			}
			break;
		case 2:
			for (double i = X; i > 1; --i) {
				denominator *= i;
			}
			for (double i = Z; i > 1; --i) {
				denominator *= i;
			}
			break;
		case 3:
			for (double i = X; i > 1; --i) {
				denominator *= i;
			}
			for (double i = Y; i > 1; --i) {
				denominator *= i;
			}
			break;
		}
		*/
		
	}
}

void factorial(int *arr, int x) {
	int n = 2;
	while (n <= x) {
		int tmp = 0, round = 0, i = 0;

		while (i < ARRSIZE) {
			tmp = arr[i] * n + round;
			round = tmp / 10;
			arr[i] = tmp % 10;
			++i;
		}
		++n;
	}
}