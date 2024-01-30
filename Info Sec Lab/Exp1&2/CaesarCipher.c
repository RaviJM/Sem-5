#include <stdio.h>
#include <string.h>
#include <ctype.h>

char* cipher(char P[], int key){
    // char* C;

    //converting original string to lowercase
    for (int i=0;i<strlen(P);i++){
        char ch = tolower(P[i]);
        P[i] = ch;
    }
    return P;
}

int main(){

    char st1[50] = "abcd";
    int key = 1;

    char* cipherText[] =  cipher(st1, key);;

    printf("hii");

    printf("%s", cipherText);

    printf("hii");

    return 0;
}