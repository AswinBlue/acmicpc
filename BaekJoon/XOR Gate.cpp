//XOR Gates
//https://www.acmicpc.net/problem/8087

#include<iostream>
#include<fstream>
#include<string>

using namespace std;

class tree {
public:
	tree * left;
	tree* right;
	int output;
};


int calculateSystem(tree *current, tree *system);

int main(void)
{
	int gate_numbers;
	int input_numbers;
	int output_gate;
	
	ifstream input;
	input.open("in.txt");
	input >> input_numbers >> gate_numbers >> output_gate;

	tree *input_lines = new tree[input_numbers];
	tree *system = new tree[gate_numbers];

	//get inputs for network
	//
	for (int i = 0; i < gate_numbers; ++i) {
		int tmp;
		input >> tmp;
		//left-side input
		if (tmp > 0)
			system[i].left = &system[tmp - 1];
		else
			system[i].left = &input_lines[abs(tmp) - 1];
		//right-side input
		input >> tmp;
		if (tmp > 0)
			system[i].right = &system[tmp - 1];
		else
			system[i].right = &input_lines[abs(tmp) - 1];
		//output
		system[i].output = -1;
	}

	//get inputs for calculate
	// 
	int result = 0;

	char *low_limit_s = new char[input_numbers];
	char *top_limit_s = new char[input_numbers];

	input >> low_limit_s >> top_limit_s;
	long low_limit = strtol(low_limit_s, NULL, 2);
	long top_limit = strtol(top_limit_s, NULL, 2);

	int *testset = new int[input_numbers];

	for (int ptr = low_limit; ptr <= top_limit; ++ptr) {
		//convert ptr to binary string
		//put them in the 'testset'
		
		for (int i = ptr, j = input_numbers-1; i > 0; i /= 2, --j)
			testset[j] = i % 2;
		//set 0 the upper digits
		for (int j = 0; true ; ++j) {
			if (testset[j] != 1)
				testset[j] = 0;
			else
				break;
		}

		for (int i = 0; i < input_numbers; ++i) {
			input_lines[i].left = NULL;
			input_lines[i].right = NULL;
			input_lines[i].output = testset[i];
		}

		calculateSystem(&system[output_gate - 1], system);

		if (system[output_gate - 1].output == 1)
			++result;

		//reset system->output
		for (int i = 0; i < gate_numbers; ++i)
			system[i].output = -1;
	}

	cout << result << endl;

	input.close();
	delete input_lines;
	delete system;
}

int calculateSystem(tree* current, tree *system)
{
	if (current->left->output < 0)
		calculateSystem(current->left, system);
	if (current->right->output < 0)
		calculateSystem(current->right, system);

	current->output = current->left->output ^ current->right->output;
	return 0;
}
