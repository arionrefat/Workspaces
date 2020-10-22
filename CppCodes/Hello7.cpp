#include <bits/stdc++.h>

using namespace std;

int main(){
	vector <int> vector1 ;
	vector <int> vector2 ;
	
	vector1.push_back(10);
	vector1.push_back(20);
	
	cout << "The size of vector1 is about " << vector1.size() << "\n";
	cout << vector1.at(0) << "\n";
	cout << vector1.at(1) << "\n";
	
	vector2.push_back(100);
	vector2.push_back(200);
	
	cout << "The size of vector2 is about " << vector2.size() << "\n";
	cout << vector2.at(0) << "\n";
	cout << vector2.at(1) << "\n";
	
	vector <vector<int>> vector_2d ;
	
	vector_2d.push_back(vector1);
	vector_2d.push_back(vector2);
	
	cout << "The elements in the two dimentional array" << "\n";
	cout << vector_2d.at(0).at(0) << "\n";
	cout << vector_2d.at(0).at(1) << "\n";
	cout << vector_2d.at(1).at(0) << "\n";
	cout << vector_2d.at(1).at(1) << "\n";
	
	cout << "The elements in the two dimentional array" << "\n";
	
	vector1.at(0) = 1000;
	
	cout << vector_2d.at(0).at(0) << "\n";
	cout << vector_2d.at(0).at(1) << "\n";
	cout << vector_2d.at(1).at(0) << "\n";
	cout << vector_2d.at(1).at(1) << "\n";
	
	cout << "The elements in vector1 array" << "\n";
	
	for (int i = 0; i < vector1.size(); i++){
		cout << vector1.at(i) << "\n";
	}
	return 0;
}
