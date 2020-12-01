#include <bits/stdc++.h>

using namespace std;

int main(){
	vector <int> nums {};
	int numtot {0};
	int target {0};
	cin >> numtot >> target;

	for (int i= 1; i <= numtot;i++){
		nums.push_back(i);	
	}
	int left,right,mid {0};
	int flag {1};

	sort(nums.begin(),nums.end());
	left = nums.at(0);
	right = nums.at(numtot-1);
	
	while (left <= right){
		mid = left +(right-left)/2;
		if (mid == target) {
			break;
		}
		else if (mid < target){ 
			left = mid;
			flag++;
		}
		else{ 
			right = mid;
			flag++;
		}
	}
	cout << flag << "\n";
	return 0;
}
