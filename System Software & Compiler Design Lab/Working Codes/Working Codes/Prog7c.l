%{
#include "Prog7c.tab.h" 
#include<stdio.h> 
extern int yylval;
%}
%%
[Tt] { return T; }
\+ { return PLUS; }
\n { return END; }
. { /* Ignore other characters */ }
%%
int yywrap() {
return 1;
}