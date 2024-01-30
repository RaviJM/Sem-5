%option noyywrap
%{
#include <stdio.h>
#include <string.h>
int keywordCount = 0;
int numberCount = 0;
int identifierCount = 0;
int otherCount = 0;
%}
%%
"auto"|"break"|"case"|"char"|"const"|"continue"|"default"|"do"|"double"|"else"|"int"|"float"|"for"|"if"|"long"|"register"|"return"|"short"|"signed"|"sizeof"|"static"|"struct"|"switch"|"typedef"|"union"|"unsigned"|"void"|"volatile" {
    printf("Keyword: %s\n", yytext);
    keywordCount++;
}
[0-9]+(\.[0-9]+)? {
    printf("Number: %s\n", yytext);
    numberCount++;
}
[a-zA-Z][a-zA-Z0-9]* {
    printf("Identifier: %s\n", yytext);
    identifierCount++;
}
. {
    printf("Other: %s\n", yytext);
    otherCount++;
}
[ \t\n] { }
%%
int main() {
    yylex();
    printf("Keywords: %d\n", keywordCount);
    printf("Numbers: %d\n", numberCount);
    printf("Identifiers: %d\n", identifierCount);
    printf("Other: %d\n", otherCount);
    return 0;
}