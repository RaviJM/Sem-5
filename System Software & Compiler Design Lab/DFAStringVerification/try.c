#include <stdio.h>
#include <string.h>

int main(){

    char st[50] = "abcde";

    for (int i=0;i<strlen(st);i++){
        printf("%d ",st[i] - 97);
    }
}