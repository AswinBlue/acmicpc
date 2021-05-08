#include <iostream>
#include <vector>
#include <set>

#define MAX_V 33554432
#define MAX_LEN_V 25
#define DEBUG 0

using namespace std;

struct tree {
	int value = 0;
	struct tree* left = nullptr;
	struct tree* right = nullptr;
};

// 모든 S에 대해 s ^ v 값이 최소인 값 출력
void find_min(struct tree& S, int v) {
	int ideal = v;
	int result = 0;
	int cmp = 1 << (MAX_LEN_V - 1);
	struct tree* ptr = &S;
#if DEBUG
		cout << "find_min\n" << "v: " << v << " ideal: " << ideal << "\n";
#endif
	while (cmp > 0) {
#if DEBUG
		cout << "ptr : " << ptr->value << " " << ptr->left << " " << ptr->right << " cmp : " << cmp << " result : " << result << "\n";
#endif
		// right child
		if ((ideal & cmp) > 0) {
			if (ptr->right != nullptr && ptr->right->value > 0) {
				ptr = ptr->right;
				result = result | cmp;
			}
			else 
				ptr = ptr->left;
		}
		// left child
		else {
			if (ptr->left != nullptr && ptr->left->value > 0)
				ptr = ptr->left;
			else {
				ptr = ptr->right;
				result = result | cmp;
			}
		}
#if DEBUG
			cout << "next : " << ptr << " " << ptr->value << "\n";
#endif
		cmp = cmp >> 1;
	} // -> while
	cout << (result ^ v) << "\n";
}

// 모든 S에 대해 s ^ v 값이 최대인 값 출력
void find_max(struct tree& S, int v) {
	int ideal = v ^ ((1 << MAX_LEN_V) - 1); // xor with 'v'
	int result = 0;
	int cmp = 1 << (MAX_LEN_V - 1);
	struct tree* ptr = &S;
#if DEBUG
		cout << "find_max\n" << "v: " << v << " ideal: " << ideal << "\n";
#endif
	while (cmp > 0) {
#if DEBUG
		cout << "ptr : " << ptr->value << " " << ptr->left << " " << ptr->right << " cmp : " << cmp << " result : " << result << "\n";
#endif
			// right child
			if ((ideal & cmp) > 0) {
				if (ptr->right != nullptr && ptr->right->value > 0) {
					ptr = ptr->right;
					result = result | cmp;
				}
				else 
					ptr = ptr->left;
			}
			// left child
			else {
				if (ptr->left != nullptr && ptr->left->value > 0)
					ptr = ptr->left;
				else {
					ptr = ptr->right;
					result = result | cmp;
				}
			}
#if DEBUG
			cout << "next : " << ptr << " " << ptr->value << "\n";
#endif
			cmp = cmp >> 1;
		} // -> while
		cout << (result ^ v) << "\n";
}
// S에 v 값을 추가하고 중복되지않는 S의 원소 개수 출력
void add(struct tree& S, int v, set<int>& check) {
#if DEBUG
		cout << "add\n" << "v: " << v << "\n";
#endif
	// 초기 입력값 받을때와 동일한 로직
	int cmp = 1 << (MAX_LEN_V - 1);
	struct tree* ptr = &S;
	
	// 중복이면 수행안함
	if (check.find(v) != check.end()) {
		goto EXIT;
	}
	check.insert(v);
	
	while (cmp >= 0) {
#if DEBUG
		cout << "ptr : " << ptr->value << " " << ptr->left << " " << ptr->right << " cmp : " << cmp << "\n";
#endif
		// update value
		++(ptr->value);
		if (cmp == 0) break;
		// right child
		if ((v & cmp) > 0) {
			// create child if not exist
			if (ptr->right == nullptr) {
				ptr->right = new struct tree({0, nullptr, nullptr});
			}
			// move ptr
			ptr = ptr->right;
		}
		// left child
		else {
			if (ptr->left == nullptr) {
				ptr->left = new struct tree({0, nullptr, nullptr});
			}
			// move ptr
			ptr = ptr->left;
		}
#if DEBUG
		cout << "next : " << ptr << " " << ptr->value << "\n";
#endif
		cmp = cmp >> 1;
	} // -> while
	
EXIT:
	cout << S.value << "\n";
}

// S중 가장 작은 값 출력 후 삭제
void remove_min(struct tree& S, set<int>& check) {
#if DEBUG
		cout << "remove_min\n";
#endif
	// 0을 우선으로 선택(left child 우선)
	int result = 0;
	int cmp = 1 << (MAX_LEN_V - 1);
	struct tree* ptr = &S;
	while (cmp >= 0) {
#if DEBUG
		cout << "ptr : " << ptr->value << " " << ptr->left << " " << ptr->right << " cmp : " << cmp << " result : " << result << "\n";
#endif
		// update value
		--(ptr->value);
		if (cmp == 0) break;
		if (ptr->left != nullptr && ptr->left->value > 0)
			ptr = ptr->left;
		else {
			ptr = ptr->right;
			result = result | cmp;
		}
		cmp = cmp >> 1;
#if DEBUG
		cout << "next : " << ptr << " " << ptr->value << "\n";
#endif
	} // -> while
	cout << result << "\n";
	check.erase(result);
}

// S중 가장 큰 값 출력 후 삭제
void remove_max(struct tree& S, set<int>& check) {
#if DEBUG
		cout << "remove_max\n";
#endif
	// 1을 우선으로 선택(right child 우선)
	int result = 0;
	int cmp = 1 << (MAX_LEN_V - 1);
	struct tree* ptr = &S;
	while (cmp >= 0) {
#if DEBUG
		cout << "ptr : " << ptr->value << " " << ptr->left << " " << ptr->right << " cmp : " << cmp << " result : " << result << "\n";
#endif
		--(ptr->value);
		if (cmp == 0) break;
		if (ptr->right != nullptr && ptr->right->value > 0) {
			ptr = ptr->right;
			result = result | cmp;
		}
		else
			ptr = ptr->left;
		cmp = cmp >> 1;
#if DEBUG
		cout << "next : " << ptr << " " << ptr->value << "\n";
#endif
	} // -> while
	cout << result << "\n";	
	check.erase(result);
}
int main(void) {
 	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		int N, Q;
		cin >> N >> Q;
		set<int> check;
		struct tree S = {0, nullptr, nullptr};
		/* 연산에 사용되는 value값이 2^25 미만이므로, 
		 * 2진수로 표현한 value의 길이는 최대 25자리 수이다. 
		 * value의 중복 여부는 연산에 영향을 주지 않으므로 있다 없다만 체크하면 된다. 
		 * level 25의 tree를 생성해 "level = 2진수 자리의 숫자" 가 되도록 한다. 
		 * leaf node에 다다를때 완성된 value가 S에 있으면 1, 없으면 0을 가지도록 한다. 
		 * non-leaf node에는 하위 tree의 값의 합을 갖도록 한다.  
		 * complete binary tree를 사용하기에는 2^26 크기의 메모리를 사용해야 하므로 메모리가 부족하다. 
		 * array가 아닌 link를 이용한 tree를 구현하자.
		 */
		
#if DEBUG
		cout << "N, Q: " << N << " " << Q << "\n";
#endif
		for (int n = 0; n < N; ++n) {
			int tmp;
			int cmp = 1 << (MAX_LEN_V - 1);
			cin >> tmp;
			
			// set에 넣고 중복 관리
			if (check.find(tmp) != check.end()) {
				continue;
			}
			check.insert(tmp);
			
			struct tree* ptr = &S;
			while (cmp >= 0) {
				// update value
				++(ptr->value);
				// break condition
				if (cmp == 0) break;
				// right child
				if ((tmp & cmp) > 0) {
#if DEBUG
		cout << "right child :: tmp : " << tmp << " cmp: " << cmp << "\n";
#endif
					// create child if not exist
					if (ptr->right == nullptr)
						ptr->right = new struct tree({0, nullptr, nullptr});
					// move ptr
					ptr = ptr->right;
				}
				// left child
				else {
#if DEBUG
		cout << "left child :: tmp : " << tmp << " cmp: " << cmp << "\n";
#endif
					if (ptr->left == nullptr)
						ptr->left = new struct tree({0, nullptr, nullptr});
					// move ptr
					ptr = ptr->left;
				}
				cmp = cmp >> 1;
			} // -> while
		} // -> for n
#if DEBUG
		cout << "initialization finished\n";
#endif
		for (int q = 0; q < Q; ++q) {
			int func, v;
			cin >> func;
			switch (func) {
				case 1:
					cin >> v;
					find_min(S, v);
					break;
				case 2:
					cin >> v;
					find_max(S, v);
					break;
				case 3:
					cin >> v;
					add(S, v, check);
					break;
				case 4:
					remove_min(S, check);
					break;
				case 5:
					remove_max(S, check);
					break;
				default:
					// do nothing
					break;
			} // -> switch
		} // -> for q
	} // -> for t
} // -> main
