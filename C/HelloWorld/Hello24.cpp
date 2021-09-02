#include <bits/stdc++.h>

using namespace std;

int main(){
    double num;

    cout << "Enter a number(double): ";
    cin >> num;

    cout << "The sqrt of" << num << "is: " << sqrt(num) << "\n";
    cout << "The cubic root of " << num << "is: " << cbrt(num) << "\n";

    cout << "The sine of " << num << "is: " << sin(num) << "\n";
    cout << "The cosine of " << num << "is :" << cos(num) << "\n";

    cout << "The ceil of " << num << "is :" << ceil(num) << "\n";
    cout << "The floor of " << num << "is :" << floor(num) << "\n";
    cout << "The round of " << num << "is :" << round(num) << "\n";

    double power {};
    cout << "\nEnter a power to raise " << num << " to:";
    cin >> power;
    cout << num << " raised to the " << " power is: " << pow(num,power) << "\n";


    return 0;
}
