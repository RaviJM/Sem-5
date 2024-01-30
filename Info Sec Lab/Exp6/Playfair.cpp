#include <bits/stdc++.h>

using namespace std;








string encrypt(string plainText, string key){
    string encryptedText;

    //make a matrix of 5*5 and fill it with '-'
    char matrix[5][5];
    for (int i=0;i<5;i++){
        for (int j=0;j<5;j++){
            matrix[i][j] = '-';
        }
    }

    //make a hash array for all alphabets
    int hashArray[26] = {0};


    //mark j in hash array, as we will not use it. (we use i instead of j)
    int temp = 'j' - 'a';
    hashArray[temp] = 1;


    //fill the matrix with key
    //when filling a character, mark it in the hash array so that we don't insert it again afterwards
    int keyPointer = 0;
    for (int i=0;i<5;i++){
        for (int j=0;j<5;j++){
            //to stop filling once whole key is inserted, we put condition
            while (keyPointer < key.length()){
                //check if key is repeated or not
                if (hashArray[int(key[keyPointer]) - int('a')] == 0){   
                    matrix[i][j] = key[keyPointer];
                    hashArray[int(key[keyPointer]) - int('a')] = 1;
                    keyPointer++;
                    break;  //means break current iteration and do next one
                }
                else{
                    keyPointer++;
                }
            }
        }
    }

    
    //filling the rest of the matrix alphabet wise, with no character repeat
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    int alphabetPointer = 0;

    for (int i=0;i<5;i++){
        for (int j=0;j<5;j++){
            //to reach the unfilled values
            if (matrix[i][j] == '-'){
                while (alphabetPointer < alphabet.length()){
                    if (hashArray[int(alphabet[alphabetPointer]) - int('a')] == 0){
                        matrix[i][j] = alphabet[alphabetPointer];
                        hashArray[int(alphabet[alphabetPointer]) - int('a')] = 1;
                        alphabetPointer++;
                        break;
                    }
                    else{
                        alphabetPointer++;
                    }
                }
            }
        }
    }

    // //printing the matrix
    // cout<<"\n";
    // for (int i=0;i<5;i++){
    //     for (int j=0;j<5;j++){
    //         cout<<matrix[i][j]<<" ";
    //     }
    //     cout<<"\n";
    // }
    // cout<<"\n";



    //replacing all 'j' in plainText by 'i'
    for (int i=0;i<plainText.length();i++){
        if (plainText[i] == 'j'){
            plainText[i] = 'i';
        }
    }

    
    //making the plainText (adding the bogus letter 'x' wherever two letters are same in pair)
    string actualText;

    int noOfxAdded = 0;     //used later

    int plainTextPointer = 0;
    while ((plainTextPointer+1) < plainText.length()){
        if (plainText[plainTextPointer] != plainText[plainTextPointer+1]){
            actualText += plainText[plainTextPointer];
            actualText += plainText[plainTextPointer+1];
            plainTextPointer = plainTextPointer+2;
        }
        else{
            actualText += plainText[plainTextPointer];
            actualText += 'x';
            noOfxAdded++;
            plainTextPointer++;
        }
    }
    
    //checking if last character needs to be added or not (cuz it is not added in the above steps sometimes, due to range issuess)
    if ((plainText.length() + noOfxAdded) != actualText.length()){
        actualText += plainText[plainText.length()-1];
    }

    //adding a bogus 'z' if length is odd
    if (actualText.length() % 2 != 0){
        actualText += 'z';
    }
    //plainText is updated and ready to be encrypted


    //form the encrypted text by finding pairs in matrix and replacing them
    for (int i=0;i<actualText.length();i=i+2){
        char a = actualText[i];
        char b = actualText[i+1];

        //position of actual plain text characters
        int row_a=0;
        int col_a=0;
        int row_b=0;
        int col_b=0;

        //encrypted characters
        char ch1;
        char ch2;

        for (int j=0;j<5;j++){
            for (int k=0;k<5;k++){
                if (matrix[j][k] == a){
                    row_a = j;
                    col_a = k;
                }
                else if (matrix[j][k] == b){
                    row_b = j;
                    col_b = k;
                }
            }
        }

        //if both characters are in same row
        if (row_a == row_b){
            col_a = (col_a + 1)%5;
            col_b = (col_b + 1)%5;
        }

        //if both characters are in same column
        else if (col_a == col_b){
            row_a = (row_a + 1)%5;
            row_b = (row_b + 1)%5;
        }

        //if both are in different rows and columns
        else{
            //just interchange the col values
            int tempCol = col_a;
            col_a = col_b;
            col_b = tempCol;
        }
        
        ch1 = matrix[row_a][col_a];
        ch2 = matrix[row_b][col_b];
        encryptedText += ch1;
        encryptedText += ch2;
    }
    
    return encryptedText;
}



















//similar but just opposite of encryption method.
//form the key matrix which will be the same.
//difference is only in forming the decryptedText.
string decrypt(string encryptedText, string key){
    string decryptedText;

    //make a matrix of 5*5 and fill it with '-'
    char matrix[5][5];
    for (int i=0;i<5;i++){
        for (int j=0;j<5;j++){
            matrix[i][j] = '-';
        }
    }

    //make a hash array for all alphabets
    int hashArray[26] = {0};


    //mark j in hash array, as we will not use it. (we use i instead of j)
    int temp = 'j' - 'a';
    hashArray[temp] = 1;


    //fill the matrix with key
    //when filling a character, mark it in the hash array so that we don't insert it again afterwards
    int keyPointer = 0;
    for (int i=0;i<5;i++){
        for (int j=0;j<5;j++){
            //to stop filling once whole key is inserted, we put condition
            while (keyPointer < key.length()){
                //check if key is repeated or not
                if (hashArray[int(key[keyPointer]) - int('a')] == 0){   
                    matrix[i][j] = key[keyPointer];
                    hashArray[int(key[keyPointer]) - int('a')] = 1;
                    keyPointer++;
                    break;  //means break current iteration and do next one
                }
                else{
                    keyPointer++;
                }
            }
        }
    }

    
    //filling the rest of the matrix alphabet wise, with no character repeat
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    int alphabetPointer = 0;

    for (int i=0;i<5;i++){
        for (int j=0;j<5;j++){
            //to reach the unfilled values
            if (matrix[i][j] == '-'){
                while (alphabetPointer < alphabet.length()){
                    if (hashArray[int(alphabet[alphabetPointer]) - int('a')] == 0){
                        matrix[i][j] = alphabet[alphabetPointer];
                        hashArray[int(alphabet[alphabetPointer]) - int('a')] = 1;
                        alphabetPointer++;
                        break;
                    }
                    else{
                        alphabetPointer++;
                    }
                }
            }
        }
    }

    //length of encryptedText (cipher text) is always even
    
    
    //form the decrypted text by finding pairs in matrix and replacing them
    for (int i=0;i<encryptedText.length();i=i+2){
        char a = encryptedText[i];
        char b = encryptedText[i+1];

        //position of encryptedText characters
        int row_a=0;
        int col_a=0;
        int row_b=0;
        int col_b=0;

        //decrypted characters
        char ch1;
        char ch2;

        for (int j=0;j<5;j++){
            for (int k=0;k<5;k++){
                if (matrix[j][k] == a){
                    row_a = j;
                    col_a = k;
                }
                else if (matrix[j][k] == b){
                    row_b = j;
                    col_b = k;
                }
            }
        }

        //if both characters are in same row
        if (row_a == row_b){
            col_a = (col_a - 1 +5)%5;
            col_b = (col_b - 1 +5)%5;
        }

        //if both characters are in same column
        else if (col_a == col_b){
            row_a = (row_a - 1 +5)%5;
            row_b = (row_b - 1 +5)%5;
        }

        //if both are in different rows and columns
        else{
            //just interchange the col values
            int tempCol = col_a;
            col_a = col_b;
            col_b = tempCol;
        }
        
        ch1 = matrix[row_a][col_a];
        ch2 = matrix[row_b][col_b];
        decryptedText += ch1;
        decryptedText += ch2;
    }





    return decryptedText;
}



















int main(){
    
    string plainText0 = "mynameisravi";
    string keyword0 = "pdeu";

    string plainText;
    string keyword;


    //truncate spaces from key and plainText, and convert to lowercase
    for (int i=0;i<plainText0.length();i++){
        if (plainText0[i] != ' '){
            plainText += tolower(plainText0[i]);
        }
    }

    for (int i=0;i<keyword0.length();i++){
        if (keyword0[i] != ' '){
            keyword += tolower(keyword0[i]);
        }
    }

    //replacing 'j' in keyword with 'i'
    for (int i=0;i<keyword.length();i++){
        if (keyword[i] == 'j'){
            keyword[i] = 'i';
        }
    }


    cout<<"Plain Text: "<<plainText;
    cout<<"\nKeyword: "<<keyword;

    string encryptedText = encrypt(plainText, keyword);
    cout<<"\nEncrypted Text: "<<encryptedText;

    string decryptedText = decrypt(encryptedText, keyword);
    cout<<"\nDecrypted Text: "<<decryptedText;

    return 0;
}
