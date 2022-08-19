#include <bits/stdc++.h>
#include <iostream>

using namespace std;

// ifstream f("in.txt");
// ofstream g("out.txt");

int main() {
  int n, m, a = {0};
  int arr[n] = {};
  cin >> n >> m;

  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  int k = arr[m - 1];

  for (long long i = 0; i < n; i++) {
    if (k != 0) {
      if (arr[i] >= k) {
        a++;
      }
    }
  }

  cout << a << endl;

  return 0;
}
