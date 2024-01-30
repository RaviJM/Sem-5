%option noyywrap 
%{
#include <stdio.h>
%}

%%
[a-zA-Z]+   {printf("Token: %s, Length: %d\n", yytext, yyleng);}
[0-9]+  {printf("Token: %s, Length: %d\n", yytext, yyleng); }
.|\n    {printf("Ignoring: %s\n", yytext); }
%%

int main()
{
    yyin = fopen("Prog2.c", "r");
    yylex();
    return 0;
}
