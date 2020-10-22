#include <bits/stdc++.h>

using namespace std;

int main(){
	string str = "";
	cin >> str;
    	char checkCharacter {};
    	int count = 0;
	for (int j= 0; j < str.size();j++){
		checkCharacter = str[j];
    		for (int i = 0; i < str.size(); i++){
        		if (str[i] ==  checkCharacter){
            			++ count;
        		}
    		}
		if(count==1){
			cout << str[j] << "\n";
			break;
		}

	}
	return 0;
}
