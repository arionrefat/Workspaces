#include <bits/stdc++.h>

using namespace std;

int main(){

    char first_name[20] {};
    char last_name[20] {};
    char full_name[50] {};
    char temp[50] {};

    cout << first_name << "\n";
    cout << "Enter your first name " << "\n";
    cin >> first_name;
    cout << "Enter your last name " << "\n";
    cin >> last_name;

    cout << "------------------------------" << "\n";

    cout << "Hello " << first_name << " your first name has total "<<
        strlen(first_name) << " characters" << "\n";
    cout << "and YE " << last_name << " your last name has total " <<
        strlen(last_name) << " characters" << "\n";

    cout << "------------------------------" << "\n";

    strcpy(full_name,first_name); //copy first name to full name
    strcat(full_name," "); // concatanate 
    strcat(full_name,last_name);
    cout << "Your full name is " << full_name << "\n";

    cout << "------------------------------------" << "\n";

    //this is complies only first name 
    //cout << "Enter your full name again" << "\n";
    //cin >> full_name;
    //cout << "Namaioa " << full_name;
    //cout << "________________________________________" << "\n";
    
    cout << "Enter your name " << "\n";
    cin.getline(full_name,50);
    cout << "Your full name is " << full_name << "\n";
    
    cout << "---------------------------------------------" << "\n";
    
    strcpy(temp,full_name);
    if(strcmp(temp,full_name)==0) cout << temp << " and " << full_name << " are the same " << "\n";
    else cout << "No, they are not the same " << "\n";

    cout << "---------------------------------------------" << "\n";
    
    for (size_t i{0} ; i < strlen(full_name);++i){
        if(isalpha(full_name[i])) full_name[i] = toupper(full_name[i]);
    }
    
    cout << "Your full name is " << full_name << "\n";
    
    cout << "----------------------------------------------" << "\n";

    if(strcmp(temp,full_name) ==0) cout << temp << " and " << full_name << " are the same " << "\n";
    else cout << "They are different " << "\n";

    cout << "------------------------------------" << "\n";

    cout << "Result of comparing " << temp << " and " << full_name << ": " << strcmp(temp,full_name) << "\n";
    cout << "Result of comparing " << temp << " and " << temp << ": " << strcmp(full_name,temp) << "\n";

    cout << "----------------------------------------" << "\n";

    return 0;
}
