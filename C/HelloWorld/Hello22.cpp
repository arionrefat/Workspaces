#include <bits/stdc++.h>

using namespace std;

int main() {

  string s0;
  string s1{"Apple"};
  string s2{"Banana"};
  string s3{"Kiwi"};
  string s4{"apple"};
  string s5{s1};
  string s6{s1, 0, 3};
  string s7(10, 'X'); // constructor style initialization

  cout << s0 << "\n";
  cout << s0.length() << "\n";

  cout << "\nComparison"
       << "\n---------------------------"
       << "\n";
  cout << boolalpha;
  cout << s1 << "==" << s5 << ": " << (s1 == s5) << "\n";
  cout << s1 << "==" << s2 << ": " << (s1 == s2) << "\n";
  cout << s1 << "!=" << s2 << ": " << (s1 != s2) << "\n";
  cout << s1 << "<" << s2 << ": " << (s1 < s2) << "\n";
  cout << s2 << ">" << s1 << ": " << (s1 > s2) << "\n";
  cout << s1 << "==" << s5 << ": " << (s1 == s5) << "\n";
  cout << "\nAll according to ASCII table"
       << "\n";

  cout << "\nConcatanation"
       << "\n";
  s3 = s5 + " and " + s2 + " juice";
  cout << "s3 is now" << s3 << "\n";

  // s3 = "nice" + "juice" + s5 + "cold"; //compiler error

  cout << "\nErase"
       << "\n";

  s1 = "This is a test";

  cout << s1.substr(0, 4);
  cout << s1.substr(5, 2);
  cout << s1.substr(10, 4);

  // if you want to find a string

  cout << s1.find("This");
  cout << s2.find("is");

  s1.erase(0, 5); // starting from 0 up to 5 character
  cout << "S1 now" << s1 << "\n";
  cout << "\nFind"
       << "\n";

  s1 = "The secrect word is Boo";
  string word;
  cout << "Enter the word to find";
  cin >> word;

  size_t position = s1.find(word);

  if (position != string::npos)
    cout << "Found " << word << " at position" << position << "\n";
  else
    cout << "Sorry " << word << " not found"
         << "\n";

  getline(cin, s1);
  cout << s1 << "\n";

  return 0;
}
