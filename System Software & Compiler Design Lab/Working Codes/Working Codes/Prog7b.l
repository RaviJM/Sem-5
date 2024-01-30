%option noyywrap
%{
#include "Prog7b.tab.h"
#include <stdio.h>
#include <stdlib.h>
extern int yylval;
int yylineno = 1;  // Add this line to declare and initialize yylineno
%}

%%
[0-9]+ { yylval = atoi(yytext); return NUMBER; }
"\t" ; 
"\n" { yylineno++; }  // Increment yylineno on newline
. return yytext[0];
%%

void yyerror(char *s)
{
    printf("%d: %s at %s\n", yylineno, s, yytext);
}
