#include <bits/stdc++.h>

using namespace std;

vector <char> vowels {'a','e','i','o','u'};
vector <int> test_scores (3);//can't initialize twice 
vector <double> hi_temp (360,80.0);//there are 360 doubles and all tare assigned 80.00

int main(){
	cout << vowels.at(1) << "\n";
	cout << "There are total " << hi_temp.size() << " vectors\n";
	
	cout << "Enter 3 test scores " << "\n";
	cin >> test_scores.at(0) >> test_scores.at(1) >> test_scores.at(2);
	 
	
	test_scores.push_back(50);
	test_scores.push_back(90);
	
	cout << test_scores[4] << "\n";
	
	vector <vector<int>> movie_ratings 
	{
		{1,2,3,4},
		{1,2,3,4},
		{1,2,3,4}
	};
	
	cout << "\nHere are the movie rating for reviewer #1 using array syntex :" << "\n";
	
	cout << movie_ratings[0][2] << "\n";
	cout << movie_ratings[1][3] << "\n";
	cout << movie_ratings[2][3] << "\n";
	cout << movie_ratings.at(2).at(2) << "\n";
	
	cout << "################################" << "\n";
	
}
