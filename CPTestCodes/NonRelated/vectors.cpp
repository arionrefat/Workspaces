#include<bits/stdc++.h>

using namespace std;

int main(){
    vector<int> v{10,20,60,70,50};

    auto ite = v.begin();
    printf("Need to use * before iterator\n");
    printf("%d\n", *ite);
    printf("if we want to find the next value in the vector\n");
    ite = v.begin()+1;
    printf("%d\n",*ite);

    //Let's find the last element
    int index = v.size() -1;
    printf("The size is %d\n", index);
    ite = v.begin()+index;
    printf("The last element\n");
    printf("%d\n",*ite);

    //finding the last value another way
    ite = v.end() -1;
    printf("The last value using end \n");
    printf("%d\n",*ite);
    
    vector<int> v{10, 20, 30, 40, 50};
    ///vector<int>::iterator it = v.begin();
    auto it = v.begin()+1;
    cout<<*it<<endl;


    it = find(v.begin(), v.end(), 35);
    int pos = it - v.begin();
    cout<<pos<<endl;
}
