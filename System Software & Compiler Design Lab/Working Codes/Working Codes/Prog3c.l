%{
#include <stdio.h>
%}

%%
[0-9]+   {
            int num = atoi(yytext);
            if (num % 7 == 0) {
                printf("The number is divisable by 7 so after adding 5: %d\n", num + 5);
            } else {
                printf("The number is not divisable by 7: %d\n", num);
            }
         }
.|\n     { printf("%s", yytext); }
%%

int main() {
    printf("Enter a number: ");
    yylex();
    return 0;
}
int yywrap()
{
    return 1;
}
