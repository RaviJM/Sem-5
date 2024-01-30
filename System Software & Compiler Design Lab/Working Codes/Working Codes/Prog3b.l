%option noyywrap
%{
#include <stdio.h>
int charCount = 0;
int wordCount = 0;
int lineCount = 0;
%}

%%
.    { charCount++; }
\n    { charCount++; lineCount++; }
[a-zA-Z]+    { wordCount++; }
%%

int main() {
    yyin = fopen("Prog2.c", "r");
    yylex();
    printf("Character count: %d\n", charCount);
    printf("Word count: %d\n", wordCount);
    printf("Line count: %d\n", lineCount);
    return 0;
}