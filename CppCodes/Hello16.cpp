#include <bits/stdc++.h>

using namespace std;

int main(){
    
    for (int i {1}, j{5}; i<= 5; ++i,++j){
        cout << i << " * " << j << " : " << (i*j) << "\n";
    }

    //for (;;) cout << "Loop loopoti loop" << "\n"; 

    
    for (int i {10}; i > 0; --i) 
        cout << i << "\n";
    cout << "Liftoff liftoff" << "\n";

    for (int i = 0; i <=100; ++i)
        cout << i << ((i%10 == 0) ? "\n" : " ");

    vector <int> nums {10,20,30,40,50};
    for (unsigned int i = 0; i < nums.size(); ++i) cout << nums[i] << "\n";

    return 0;
}
