%{
#include <stdio.h>
int vowel_count = 0;
%}

%%
^i.* {   
    printf("Line: %s\n", yytext);
    vowel_count = 0;
    for (int i = 0; i < yyleng; i++) {
        if (yytext[i] == 'a' || yytext[i] == 'e' || yytext[i] == 'i' || yytext[i] == 'o' || yytext[i] == 'u' ||
            yytext[i] == 'A' || yytext[i] == 'E' || yytext[i] == 'I' || yytext[i] == 'O' || yytext[i] == 'U') {
            vowel_count++;
        }
    }
    printf("Vowel count: %d\n", vowel_count);
}

.|\n ; 

%%

int yywrap(){}

int main() {
    yyin = fopen("input.txt", "r"); 
    yylex();
    fclose(yyin);
    return 0;
}
