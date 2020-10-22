#include<bits/stdc++.h>

using namespace std;

void pass_by_value1 (int num);
void pass_by_value2 (string s);
void pass_by_value3 (vector <string> v);
void print_vector (vector <string> v);

void pass_by_value1(int num){
	num = 100;
}

void pass_by_value2(string s){
	s = "Changed";
}

void pass_by_value3(vector <string> v){
	for (auto s: v) cout << s << "\n";
	cout << "\n";
}

int main(){
	int num {10};
	int another_num {20};

	cout << "num before calling pass_by_value1: " << num << "\n";
	pass_by_value1(num);
	cout << "num after calling pass_by_value1: " << num << "\n";
	
	cout << "\nanother_num after calling pass_by_value1: " << another_num << "\n";
	pass_by_value1(another_num);
	cout << "another_num after calling pass_by_value1: " << another_num << "\n";

	string name{"Frank"};
	cout << "\nname before calling pass_by_value2: " << "\n";
	pass_by_value2(name);

	// Hot take by default it makes copy of the global value in ta fuction

}
