#include <bits/stdc++.h>

using namespace std;

int main(){
    char selection {};
    vector <int> nums {};

    do{
        cout << "--------------------" << "\n";
        cout << "P - Print numbers" << "\n";
        cout << "A - Add a number " << "\n";
        cout << "M - Display mean of the numbers" << "\n";
        cout << "S - Display the smalest number" << "\n";
        cout << "L - Display the largest number" << "\n";
        cout << "V - adVanced Options" << "\n";
        cout << "Q - So you want to quit huh?" << "\n";
        cout << "--------------------" << "\n";
        cin >> selection;

        if (selection == 'P' || selection == 'p'){

            if(nums.size() == 0) cout << "[] - the list is empty" << "\n";
            
            else{
                cout << "[ ";
                for (auto var : nums ) cout << var << " ";
                cout << " ]";
                cout << "\n";
            }
        }
        else if (selection == 'A' || selection == 'a'){
                cout << "Are you sure? (y/N)" << "\n";
                char yesno {};
                cin >> yesno;
                if (yesno == 'y' || yesno == 'Y'){
                    int a {};
                    cout << "Enter your number then " << "\n";
                    cin >> a;
                    nums.push_back(a);
                    cout << "Okay " << a << " is added" << "\n";
                }
                else cout << "Your wish" << "\n";
        }

        else if (selection == 'M' || selection == 'm'){

            if(nums.size() == 0) cout << "Unable to calculate the mean - no data" << "\n";

            else {
                int sum {};
                for (auto var: nums) sum += var;
                cout << "The mean is: "<< static_cast<double> (sum)/nums.size() << "\n";
            }
        }

        else if (selection == 's' || selection == 'S'){

            if (nums.size() == 0) cout << "Unable to determine smallest number because life is empty " << "\n";

            else {
                sort(nums.begin(),nums.end());
                cout << "The smallest number is " << nums[0] << "\n";
            }
        }

        else if (selection == 'l' || selection == 'L'){

            if (nums.size() == 0) cout << "Unable to determine largest number because life is empty " << "\n";

            else{
                sort(nums.begin(),nums.end());
            cout << "The largest number is " << nums.back() << "\n";
            }
        }

        //Need to solve this!
        
        /*
        if(selection == 'V' || selection == 'v'){
            do{
                cout << "A - search for a number in the list and if found display the number of times it occurs in the list" << "\n";
                cout << "B - clearing out the list (make it empty again) (Hint: the vector class has a .clear() method)" << "\n";
                cout << "C - don't allow duplicate entries" << "\n";
                cout << "D - come up with your own ideas!" << "\n";
                cout << "Q - quit from here! " << "\n";
            }while (selection != 'Q' || selection != 'q');
        }
        */

        else if (selection == 'q' || selection == 'Q') cout << "Bye Bye coward" << "\n";

        else cout << "Unknown selection, Please try again " << "\n";


    }while(selection != 'q' && selection != 'Q');

    return 0;
}
