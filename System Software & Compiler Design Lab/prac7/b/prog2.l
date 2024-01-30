%option noyywrap
%{
    #include "prog2.tab.h"
    #include <stdio.h>
    extern int yylval;
%}

%%

[0-9]+ { yylval = atoi(yytext); return NUMBER; }
["\t"] ; 
["\n"] return 0;
. return yytext[0];

%%

void yyerror(char *s)
{
    printf("%d: %s at %s\n", yylineno, s, yytext);
}