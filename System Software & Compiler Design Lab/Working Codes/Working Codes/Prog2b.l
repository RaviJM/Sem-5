%option noyywrap
%{
#include <stdio.h>
%}

%%
int|float|if|else|for|while|return    { printf("Keyword: %s\n", yytext); }
[a-zA-Z][a-zA-Z0-9]*    { printf("Identifier: %s\n", yytext); }
[0-9]+    { printf("Number: %s\n", yytext); }
.|\n    { printf("Other: %s\n", yytext); }
%%

int main() {
    yyin = fopen("Prog2.c", "r");
    yylex();
    return 0;
}