#include <bits/stdc++.h>

using namespace std;

string cipher(string P, int key){

    string C;

    // converting original text to lowercase
    for (int i=0;i<P.length();i++){
        P[i] = tolower(P[i]);
    }

    // converting to cipher text
    for (int i=0;i<P.length();i++){
        char ch;
        if (P[i] != ' '){
            ch = (int(P[i]) + (key % 26) - 97) % 26 + 97;
        }
        else{
            ch = ' ';
        }
        C += ch;
        
    }
    return C;
}

string decipher(string P, int key){

    string C;

    // converting original text to lowercase
    for (int i=0;i<P.length();i++){
        P[i] = tolower(P[i]);
    }

    // converting to cipher text
    for (int i=0;i<P.length();i++){
        char ch;
        if (P[i] != ' '){
            ch = (int(P[i]) - (key % 26) - 97 + 26) % 26 + 97;
        }
        else{
            ch = ' ';
        }
        C += ch;
        
    }
    return C;
}

int main(){

    string plainText = "i study in college";
    int key = 3;
    
    string cipherText = cipher(plainText, key);
    cout<<"Encrypted Text: "<<cipherText;

    cout<<"\n";

    string decyp = decipher(cipherText, key);
    cout<<"Decrypted Text: "<<decyp;

    return 0;
}