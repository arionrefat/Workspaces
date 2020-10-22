#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long int n {0};
    //cin >> n;
    scanf("%d", &n);
    long long int sum = n*(n+1)/2;

    // do not use for loop to sum that is slow as F
    //cout << sum << "\n";
    printf("%d\n", n);
    
    //getting whole line from input
    string s;
    getline(cin, s);

}
