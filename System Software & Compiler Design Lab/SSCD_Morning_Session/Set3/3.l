%{
#include <stdio.h>
#include <string.h>
%}

%%
Yagga {
    int length = strlen(yytext);
    for (int i = 0; i < length; i++) {
        printf("%.*s\n", length - i, yytext + i);
    }
}
.|\n ;   // Match any character or newline

%%
int yywrap(){}

int main() {
    yy_scan_string("Yagga");  // Set input string
    yylex();
    return 0;
}
