#include <bits/stdc++.h>

using namespace std;
int main() {
    long long i, n, x;
    cin >> n >> x;

    long long counter = 0, lower = 1, higher = n, midnum;
    while (lower < higher) {
        midnum = (lower + higher) / 2;

        if (x > midnum)
            lower = midnum + 1;
        else
            higher = midnum;
        counter++;
    }
    cout << counter << "\n";
}