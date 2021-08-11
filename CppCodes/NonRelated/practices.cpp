#include <bits/stdc++.h>

using namespace std;

int main() {
  /* ios::sync_with_stdio(0);
  cin.tie(0); */

  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);


  int x, y{0};
  cin >> x >> y;

  pair<int, int> z;
  z.first = x;
  z.second = y;

  pair<int, int> w;
  w.first = 1;
  w.second = 2;

  swap(w, z);

  pair<int, string> s;
  s.first = 1;
  s.second = "abc";

  cout << s.first << "\n";
  cout << s.second << "\n";

  pair<int, string> p = make_pair(3, "abc");

  vector<int> lx(5, -1);

  for (int i : lx)
    cout << lx[i];

  return 0;
}
