#include<bits/stdc++.h>

using namespace std;

int main(){
    long long int n {0};
    cin >> n;

    long long int sum = n*(n+1)/2;

    long long int two = 1;

    while (two <= n){
        sum -= 2*two;
        two *= 2;
    }

    cout << sum << "\n";

}
