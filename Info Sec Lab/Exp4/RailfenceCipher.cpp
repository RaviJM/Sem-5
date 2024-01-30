//Note: in railfence cipher, spaces ARE considered, so do not truncate them.

#include <bits/stdc++.h>

using namespace std;


//logic: make a matrix of rail * length(plainText) dimensions, and traverse the string and fill the matrix
string encrypt(string plainText, int rail){
    string encryptedText;

    int len = plainText.length();

    char matrix[rail][len];

    //filling the matrix with '-'
    for (int i=0;i<rail;i++){
        for (int j=0;j<len;j++){
            matrix[i][j] = '-';
        }
    }
    
    int flag = 1;   //flag = 1 means increment the value of  rows, flag = 0 means decrement the value of rows. {after this iteration}[Initially set to 1]
    int row = 0;
    for (int i=0;i<len;i++){    // traversing the plainText. [value of i will be the column number]

        //setting the flag (to choose whether to increment or decrement)
        if (row == 0){
            flag = 1;
        }
        else if (row == (rail-1)){
            flag = 0;
        }
        else{
            //do nothing
        }
        
        //push the value
        matrix[row][i] = plainText[i];

        //choosing the next row value in the matrix [update value of row]
        if (flag == 1){
            row++;
        }
        else{
            row--;
        }
    }

    // //printing the matrix
    // cout<<"\nMatrix:\n";
    // for (int i=0;i<rail;i++){
    //     for (int j=0;j<len;j++){
    //         cout<<matrix[i][j]<<" ";
    //     }
    //     cout<<"\n";
    // }

    //making the encrypted text
    for (int i=0;i<rail;i++){
        for (int j=0;j<len;j++){
            if (matrix[i][j] != '-'){
                encryptedText += matrix[i][j];
            }
        }
    }

    return encryptedText;
}



















//logic: make the matrix and fill the places (where the encrypted text characters will be placed) with * and then traverse the matrix again and fill it with ciphertext wherever there are *
string decrypt(string encryptedText, int rail){
    string decryptedText;

    int len = encryptedText.length();
    char matrix[rail][len];


    //filling the matrix with '-'
    for (int i=0;i<rail;i++){
        for (int j=0;j<len;j++){
            matrix[i][j] = '-';
        }
    }

    //filling the places in the matrix with '*' wherever the encrypted text characters need to be put (same way as done in encryption)
    int flag = 1;
    int row = 0;
    for (int i=0;i<len;i++){
        if (row == 0){
            flag = 1;
        }
        else if (row == rail-1){
            flag = 0;
        }
        else{
            //do nothing
        }

        matrix[row][i] = '*';


        if (flag == 1){
            row++;
        }
        else{
            row--;
        }
    }

    // //printing the matrix
    // cout<<"\nMatrix:\n";
    // for (int i=0;i<rail;i++){
    //     for (int j=0;j<len;j++){
    //         cout<<matrix[i][j]<<" ";
    //     }
    //     cout<<"\n";
    // }


    //traversing through the matrix and filling it with the encrypted text wherever there is a '*'
    int stringPointer = 0;
    for (int i=0;i<rail;i++){
        for (int j=0;j<len;j++){
            if (matrix[i][j] == '*'){
                matrix[i][j] = encryptedText[stringPointer++];
            }
        }
    }

    //forming the decrypted text the same way we put the '*' (traversing method is same) [this is the same way encryption was done, but now we're reading it instead of writing it]
    flag = 1;
    row = 0;
    for (int i=0;i<len;i++){
        if (row == 0){
            flag = 1;
        }
        else if (row == rail-1){
            flag = 0;
        }
        else{
            //do nothing
        }

        decryptedText += matrix[row][i];


        if (flag == 1){
            row++;
        }
        else{
            row--;
        }
    }

    return decryptedText;
}



















int main(){
    
    string plainText = "My name is Ravi and I study in PDEU";
    int rail = 4;
    cout<<"Plain Text: "<<plainText;
    cout<<"\nRail: "<<rail;

    string encryptedText = encrypt(plainText, rail);
    cout<<"\nEncrypted Text: "<<encryptedText;

    string decryptedText = decrypt(encryptedText, rail);
    cout<<"\nDecrypted Text: "<<decryptedText;

    return 0;
}