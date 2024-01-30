%option noyywrap
%{
#include <stdio.h>
int token_count = 0;
%}

%%
[ \t\n]+ { }

[0-9]+ {
    printf("Number: %s (Length: %d)\n", yytext, yyleng);
    token_count++;
    }

[a-zA-Z]+ {
    printf("Word: %s (Length: %d)\n", yytext, yyleng);
    token_count++;
    }

. {
    printf("Symbol: %s (Length: %d)\n", yytext, yyleng);
    token_count++;
    }
%%

int main() {
    yylex();
    printf("Total tokens: %d\n", token_count);
    return 0;
}