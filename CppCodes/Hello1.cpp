#include <iostream>

using namespace std;

int main(){
	int length {0};
	int width {0};
	cout << "Enter the width and length of the room" << "\n";
	cin >> width >> length;
	cout << "The area is :" << length*width << " sq feet" << "\n";
	return 0;
}
