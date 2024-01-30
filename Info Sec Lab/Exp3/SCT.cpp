#include <bits/stdc++.h>

using namespace std;

string encrypt(string plainText, string keyword){
    string EncryptedText;
    
    double columns = keyword.length();
    double rows = ceil(plainText.length() / columns);

    

    char matrix[int(rows)][int(columns)];

    int stringIndexPointer = 0;

    //inserting characters into the table(row-wise)
    for (int i=0;i<rows;i++){
        for (int j=0;j<columns;j++){
            if (stringIndexPointer < plainText.length()){
                matrix[i][j] = plainText[stringIndexPointer];
                stringIndexPointer++;
            }

            //when plaingText traversal is over but table is still left to fill
            //fill it with '_'
            else{
                matrix[i][j] = '_';
            }
        }
    }

    // //for printing the table
    // cout<<endl;
    // for (int i=0;i<rows;i++){
    //     for (int j=0;j<columns;j++){
    //         cout<<matrix[i][j]<<" ";
    //     }
    //     cout<<"\n";
    // }
    // cout<<endl;


    //finding the index of highest ASCII value character in the keyword (used later)
    int highestASCIIValueindex = 0;
    for(int i=0;i<keyword.length();i++){
        if (keyword[i] >= keyword[highestASCIIValueindex]){
            highestASCIIValueindex = i;
        }
    }

    //for deciding order of reading the columns//
    //order will be stored in the below array
    int orderArr[keyword.length()];

    //for keeping track whether character is traversed or not
    int hashArr[keyword.length()] = {0};

    //for inserting into the orderArr
    int pointerForInsert = 0;

    //finding smallest ascii value in the keyword and storing its index in the orderArr each time.
    for (int i=0;i<keyword.length();i++){
        int smallestASCIIValueIndex = highestASCIIValueindex;
        for (int j=0;j<keyword.length();j++){
            if (keyword[j] <= keyword[smallestASCIIValueIndex] && hashArr[j] == 0){
                smallestASCIIValueIndex = j;
            }
        }
        orderArr[pointerForInsert++] = smallestASCIIValueIndex;
        hashArr[smallestASCIIValueIndex] = 1;
    }

    //forming the decryptedText
    for (int i=0;i<keyword.length();i++){
        int columnNumber = orderArr[i];
        for (int j=0;j<rows;j++){
            if(matrix[j][columnNumber] != '_'){
                EncryptedText += matrix[j][columnNumber];
            }
        }
    }

    return EncryptedText;
}








string decrypt(string encryptedText, string keyword){
    string decryptedText;

    double columns = keyword.length();
    double rows = ceil(encryptedText.length() / columns);

    
    char matrix[int(rows)][int(columns)];

    //inserting characters into the table (column-wise)
    int stringIndexPointer = 0;
    for (int i=0;i<columns;i++){
        for (int j=0;j<rows;j++){
            if (stringIndexPointer < encryptedText.length()){
                matrix[j][i] = encryptedText[stringIndexPointer];
                stringIndexPointer++;
            }

            //when plaingText traversal is over but table is still left to fill
            //fill it with '_'
            else{
                matrix[j][i] = '_';
            }
        }
    }

    // //for printing the table
    // cout<<endl;
    // for (int i=0;i<rows;i++){
    //     for (int j=0;j<columns;j++){
    //         cout<<matrix[i][j]<<" ";
    //     }
    //     cout<<"\n";
    // }
    // cout<<endl;


    //finding the index of highest ASCII value character in the keyword (used later)
    int highestASCIIValueindex = 0;
    for(int i=0;i<keyword.length();i++){
        if (keyword[i] >= keyword[highestASCIIValueindex]){
            highestASCIIValueindex = i;
        }
    }


    //for deciding order of reading the columns//
    //order will be stored in the below array
    int orderArr[keyword.length()];

    //for keeping track whether character is traversed or not
    int hashArr[keyword.length()] = {0};

    //for inserting into the orderArr
    int pointerForInsert = 0;

    //finding smallest ascii value in the keyword and storing its index in the orderArr each time.
    for (int i=0;i<keyword.length();i++){
        int smallestASCIIValueIndex = highestASCIIValueindex;
        for (int j=0;j<keyword.length();j++){
            if (keyword[j] <= keyword[smallestASCIIValueIndex] && hashArr[j] == 0){
                smallestASCIIValueIndex = j;
            }
        }
        orderArr[pointerForInsert++] = smallestASCIIValueIndex;
        hashArr[smallestASCIIValueIndex] = 1;
    }

    

    //but since reading order (for decryption) will be different, actual order will be different
    //finding actual order

    int actualOrder[keyword.length()];
    int pointer = 0;
    for(int i=0;i<keyword.length();i++){
        //finding i in orderArr, and appending its index to actualOrder
        for(int j=0;j<keyword.length();j++){
            if (i == orderArr[j]){
                // j will give the actual order
                actualOrder[pointer++] = j;
            }
        }
    }
    


    //forming the decryptedText
    for (int i=0;i<rows;i++){
        for (int j=0;j<keyword.length();j++){
            int columnNumber = actualOrder[j];
            if (matrix[i][columnNumber] != '_'){
                decryptedText += matrix[i][columnNumber];
            }
        }
    }


    return decryptedText;
}


int main(){

    string plainText = "My name is Ravi";
    string keyword = "PDEU";
    cout<<"Plain Text: "<<plainText;
    cout<<"\nKeyword: "<<keyword;

    string encryptedText = encrypt(plainText, keyword);
    cout<<"\nEncrypted Text: "<<encryptedText;

    string decryptedText = decrypt(encryptedText, keyword);
    cout<<"\nDecrypted Text: "<<decryptedText;

    return 0;
}