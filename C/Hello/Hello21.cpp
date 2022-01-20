#include <bits/stdc++.h>

using namespace std;

int main(){
    string s1;
    string s2 {"Frank"};
    string s3 {s2};
    string s4 {"Frank",3};
    string s5 {s3,0,3};
    string s6 (3,'X'); // constructor style initialization
    
    s1 = "C++ Rocks! ";

    s2 = {"Hello"};
    s2 = s1;

    string part1 {"C++"};
    string part2 {"is a powerfull "};

    string sentence;

    sentence = part1 + " " + part2 + " language";
    
    //sentence = "C++ " + "is powerfull"; // illegal

    s1 = {"Frank"};

    for (int c : s1) cout << c << "\n"; 

    s1 = {"This is a test"};

    cout << s1.substr(0,4);
    cout << s1.substr(5,2);
    cout << s1.substr(10,4); //starts at 10 and include 4 character

    cout << s1.find("This"); //starts at index 0
    cout << s1.find("is"); //starts at index 2
    cout << s1.find("test"); //starts at index 10
    cout << s1.find('e'); // 'char' e found at 11
    cout << "\n";
    cout << s1.find("is",4); //want to find "is" but staring from index 4
    cout << "\n";
    cout << s1.find("XX"); //  string::npos

    s1 = {"Henlo this is metro"};
    
    cout << s1.erase(0,5); // is a test
    cout << s1.erase(5,4); // starts from 5 upto 4 characters
    //cout << s1.clear(); //unclear what happends here 

    s1 = {"Frank"};

    cout << s1.length() << "\n";

    s1 += "James";
    cout << s1 << "\n";

    cin >> s1; //enter HELLO THERE
    cout << s1 << "\n";

    getline(cin,s1); //Read entire line until \n
    cout << s1 << "\n";

    getline(cin,s1,'x'); //stop reading at x, x will be discarded
    cout << s1 << "\n";
    

    return 0;
}
