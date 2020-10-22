#include <bits/stdc++.h>

using namespace std;

int main(){
    int number;

    while(number >= 100){
        cout << "Enter an integer is less than 100" << "\n";
        cin >> number;
    }
    cout << "Thanks man " << "\n";
    
    char selection {};

    do {
        double width {}, height {};
        cout << "Enter W and H " << "\n";
        cin >> width >> height;

        double area {width*height};
        cout << "The area is " << area << "\n";

        cout << "Want to calculate another? (Y/N) : ";
        cin >> selection;
    } while (selection == 'Y' || selection == 'y');
    cout << "Thank you for playin g" << "\n";
    
    do {
        cout << "\n ........................ " << "\n";
        cout << "1. Do this " << "\n";
        cout << "2. Do that " << "\n";
        cout << "3. Do something else " << "\n";
        cout << "Q. Quit okay? " << "\n";
        cout << "Enter your selection " << "\n";

        cin >> selection;

        if(selection == '1') cout << "OKay 1 nice " << "\n";
        else if (selection == '2') cout << "OKay 2 naisu" << "\n";
        else if (selection == '3') cout << "Okay 3 naisa" << "\n";
        else if (selection == 'Q' || selection == 'q') cout << "So what you want to quit now , you little shit " << "\n";
        else cout << "unknown option ... try again " << "\n";
        } while (selection != 'q' && selection != 'Q');

    return 0;
}
