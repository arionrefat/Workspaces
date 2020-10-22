#include <bits/stdc++.h>

using namespace std;

int main(){
    int num {0}, factors {0};
    cin >> num;

    for (int i = 1; i < num; i++){
       if (num%i==0)
           factors = i;
       // need to make sure "i" is prime then if prime then it goes to factor variable
    }
    
    cout << "The Largest Prime factor is " << factors << "\n";

    return 0;
}
