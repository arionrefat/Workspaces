#include <bits/stdc++.h>

using namespace std;

int main(){

    int random_number {};
    size_t count {10};
    int min {1};
    int max {6};

    cout << "RAND MAX on my system is: " << RAND_MAX << "\n";
    srand(time(nullptr));

    for (size_t i {1}; i <= count; ++i ){
        random_number = rand()%max + min;
        cout << random_number << "\n";
    }

    cout << "\n";
    return 0;
}
