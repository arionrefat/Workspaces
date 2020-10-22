#include <bits/stdc++.h>

using namespace std;

int main(){
	const double usd_per_eur {1.19};
	
	cout << "Welcome to the Eur to USD converter" << "\n";
	cout << "Enter the value in EUR: " ;
	
	double euros {0.0};
	double dollars {0.0};
	
	cin >> euros;
	dollars = euros*usd_per_eur;
	
	cout << euros << "euros is equivalent to" << dollars <<"\n";
	
	return 0;
}
