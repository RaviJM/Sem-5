%{
#include <stdio.h>
#include <string.h>
int nl= 0;
int ns = 0;
int nc = 0;
int nw = 0;
int nn = 0;
%}
%option noyywrap
%%
[/n] {
    nl++;
}
[ /+] {
    ns++;
}
[a-zA-Z]+ {
    nw++,nc+=yyleng ;
    }
[0-9]+(.[0-9]+)?(E([=\-])?[0-9]+)? {
    nn++;
}
. {
    nc+=yyleng;
}
%%
int main() {
    yylex();
    printf("Number of Lines : ",nl);
    printf("Number of Spaces : ",ns);
    printf("Number of Characters : ",nc);
    printf("Number of Words : ",nw);
    printf("Number of Numbers : ",nn);
    return 0;
}