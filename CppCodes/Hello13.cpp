#include <bits/stdc++.h>

using namespace std;

int main(){
	char letter_grade{};
	cout << "Enter the letter grade you expected on the exam: ";
	cin >> letter_grade;

	switch(letter_grade){
		case 'a':
		case 'A':
			cout << "You need a 90 or above " << "\n";
			break;
		case 'b':
		case 'B':
			cout << "Go, fucking study! " << "\n";
			break;
		case 'f':
		case 'F':{
				char confirm {};
                cout << "Are you sure (y/N)";
                cin >> confirm;
                if(confirm == 'y' || confirm == 'Y')
                    cout << "OK, I guess you didn't study " << "\n";
                else if(confirm == 'n' || confirm == 'N') 
                    cout << "Good, got study" << "\n";
                else cout << "Illigal choice " << "\n";
                break;
			 }
		default:
			cout << "Put it again " << "\n";
			cin >> letter_grade;
	}
	return 0;

}
