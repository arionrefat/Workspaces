#include <bits/stdc++.h>

using namespace std;

int main(){
    int scores[] {10,20,30,40,50};

    for (int score : scores) cout << score << "\n";
    
    //auto mode; doesn't need any declation of a variable
    for (auto score : scores) cout << score << "\n";
    
    vector <double> temps {87.2, 77.1, 80.0, 72.5};

    double average_temp {};
    double total {};

    for (auto temp : temps) total += temp;

    if(temps.size() != 0) average_temp = total / temps.size();
    cout << fixed << setprecision(1);
    cout << "The average temperature is" << average_temp << "\n";
    
    for (auto val : {1,2,4,5,6}) cout << val << "\n";

    for (auto c : "This is a test") 
        if(c == ' ')
            cout << "\t";
        else
            cout << c;

    for (auto a: "Frank") cout << a << "\n";

    return 0;
}
