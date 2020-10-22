#include <bits/stdc++.h>

using namespace std;

int main(){
    enum Direction{
        left,right,up,down
    };

    Direction heading {left};

    switch(heading){
        case left:
            cout << "Going left" << "\n";
            break;
        case right:
            cout << "Going right" << "\n";
            break;
        default:
            cout << "OK" << "\n";
    }
    return 0;
}

