#include <iostream>
#include <bits/stdc++.h>

using namespace std;

ifstream f ("in.txt");
ofstream g ("out.txt");

int main(){
    int a, b, sum {0};

    f >> a >> b;
    sum = a+b;
    g << sum;
}
