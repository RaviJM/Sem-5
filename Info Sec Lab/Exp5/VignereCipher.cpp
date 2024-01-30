//In this program, spaces are truncated and characters are converted to lowercase

#include <bits/stdc++.h>

using namespace std;

string encrypt(string plainText, string key){
    string encryptedText;
    string keyword;
    
    int len = plainText.length();

    //make keyword from key (make it the same length as the plainText)
    int repeat = ceil(double(len)/double(key.length()));

    for (int i=0;i<repeat;i++){
        for (int j=0;j<key.length();j++){
            if (keyword.length() < len){
                keyword += key[j];
            }
        }
    }

    //making encryptedText (by adding key and plainText)
    for (int i=0;i<len;i++){
        int ch = (((plainText[i] - 'a') + (keyword[i] - 'a'))%26) + 'a';
        encryptedText += char(ch);
    }

    return encryptedText;
}


string decrypt(string encryptedText, string key){
    string decryptedText;
    string keyword;

    int len = encryptedText.length();

    //make keyword from key (make it the same length as the encryptedText)
    int repeat = ceil(double(len)/double(key.length()));

    for (int i=0;i<repeat;i++){
        for (int j=0;j<key.length();j++){
            if (keyword.length() < len){
                keyword += key[j];
            }
        }
    }


    //making decryptedText (by subtracting key from encryptedText)
    for (int i=0;i<len;i++){
        int ch = (((encryptedText[i] - 'a') - (keyword[i] - 'a') + 26)%26) + 'a';
        decryptedText += char(ch);
    }

    return decryptedText;
}



int main(){
    
    string plainText0 = "mynameisravi";
    string key0 = "pdeu";

    string plainText;
    string key;


    //truncate spaces from key and plainText, and convert to lowercase
    for (int i=0;i<plainText0.length();i++){
        if (plainText0[i] != ' '){
            plainText += tolower(plainText0[i]);
        }
    }

    for (int i=0;i<key0.length();i++){
        if (key0[i] != ' '){
            key += tolower(key0[i]);
        }
    }





    cout<<"Plain Text: "<<plainText;
    cout<<"\nKey: "<<key;

    string encryptedText = encrypt(plainText, key);
    cout<<"\nEncrypted Text: "<<encryptedText;

    string decryptedText = decrypt(encryptedText, key);
    cout<<"\nDecrypted Text: "<<decryptedText;

    return 0;
}