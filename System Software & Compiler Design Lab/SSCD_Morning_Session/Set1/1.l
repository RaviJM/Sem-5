%{
#include <stdio.h>
#include <stdlib.h>
int valid = 1; // Flag to track the validity of the expression
%}

%option noyywrap

%%
[ \t\n]+        ; // Ignore whitespace
[0-9]+          { printf("Number: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]* { printf("Identifier: %s\n", yytext); }
[-+*/=]         { printf("Operator: %s\n", yytext); }
\(              { printf("Left Parenthesis\n"); }
\)              { printf("Right Parenthesis\n"); }
.               { printf("Invalid character: %s\n", yytext); valid = 0; }
%%

int main() {
    printf("Enter an arithmetic expression: \n");
    yylex();

    if (valid) {
        printf("The expression is valid.\n");
    } else {
        printf("The expression is not valid.\n");
    }

    return 0;
}
