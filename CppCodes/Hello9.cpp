#include <bits/stdc++.h>

using namespace std;

int main(){
	int total_amount {100};
	int total_number {8};
	double average {0.0};

	average = total_amount / total_number;
	cout << average << "\n";

	average = static_cast<double>(total_amount) / total_number;
	cout << average << "\n";   // now it will show 12.5

	int total {};
	int num1 {}, num2 {}, num3 {};
	const int count {3};
	
	cin >> num1 >> num2 >> num3;

	total = num1+num2+num3;

	// (new style) average = static_cast<double>(total) / count ;
	//(old style)average = (double) total /count ; 

	cout << average << "\n";
	
	return 0;
}
