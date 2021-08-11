#include <bits/stdc++.h>

using namespace std;

int main(){
	bool equal_result{false};
	bool notEqualResult{false};

	int num1{},num2{};

	cout << noboolalpha;  //will display true/false instead of 1/0

	cout << "Enter numbers: " << "\n";
	cin >> num1 >> num2;
	equal_result = (num1 == num2);
	notEqualResult = (num1 != num2);

	cout << "Comparision result (equal) " << equal_result << "\n";
	cout << "Comparision result (not equal) " << notEqualResult << "\n";
	cout << "Hello there " << "\n";


	return 0;
}
