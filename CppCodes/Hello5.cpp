#include <bits/stdc++.h>
//array
using namespace std;

int main(){
	char vowel[] {'a','e','i','o','u'};
	cout << "\nThe first vowel is " << vowel[0] << "\n";
	cout << "The last vowel is " << vowel[4] << "\n";
	
	double hi_temps [] {90.0,56.2,696.3,45,69.5,56.0};
	cout << hi_temps[5] << "\n";
	
	hi_temps[0] = 100.7;
	
	cout << hi_temps[0] << "\n";
	
	int test_scores [5] {0,0,0,100};
	
	cout << test_scores[3] << "\n";
	cout << test_scores[4] << "\n";
	
}
