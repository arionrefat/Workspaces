#include <bits/stdc++.h>

using namespace std;

int main(){
    int a{10},b{20};
    int score{92};
    int result {};

    result = (a > b) ? a : b;
    result = (a < b) ? (b-a) : (a-b);
    //result = (b != 0) ? (a/b) : 0;

    cout << result << "\n";
    cout << ((score > 90) ? "Execellent" : "Good ") << "\n";

    cout << a << " is " << ((a%2==0) ? "EVen" : "odd")  << "\n";

    return 0;
}
