#include <bits/stdc++.h>

using namespace std;

int main() {
    
    string alphabet {"[ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"};
    string key  {" [XZNLWEBGJHQDYVTKFUOMPCIASRxznlwebgjhqdyvtkfuompciasr"};
    

    string encrypted {};
    string decrypted {};
    string word {};
    cout << "Enter your secrect message: " << "\n";
    getline(cin,word);
    cout << "\n";

    cout << "Encrypting message ......." << "\n";
    cout << "\n";
    
    // need to work with replace method
    // result = word.replace()
    
    for (char c:word){
        size_t position = alphabet.find(c);
        if(position != string::npos){
            char new_char {key.at(position)};
            encrypted += new_char;
        }
        else encrypted += c;    
    }

    cout << "Encrypted message: " << encrypted << "\n";

    cout << "\nDecrypting message ....." << "\n";

    for (char c: encrypted) {
        size_t position = key.find(c);
        if(position != string::npos){
            char new_char {alphabet.at(position)};
            decrypted += new_char;
        }
        else decrypted += c;
    }

    cout << "Decrypted message: " << decrypted << "\n";

    return 0;
}
