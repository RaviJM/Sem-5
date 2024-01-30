%{
#include "Prog7a.tab.h" 
#include<stdio.h> 
extern int yylval;
%}

%%
[0-9]+ {yylval = atoi(yytext); return NUMBER;}
[ \t]; /*Ignore white space*/
\n return 0; /*Logical EOF*/
. return yytext[0]; /*to not return any symbol to the parser*/
%%

int yywrap(){ return 1;
}