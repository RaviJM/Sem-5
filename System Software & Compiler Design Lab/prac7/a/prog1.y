%{
#include <stdio.h>
#include <math.h>
%}

%token NUMBER
%%

statement: expression      { printf("Result: %d\n", $1); }
         | statement expression { printf("Result: %d\n", $2); }
         ;

expression: expression '+' expression { $$ = $1 + $3; }
          | expression '-' expression { $$ = $1 - $3; }
          | expression '*' expression { $$ = $1 * $3; }
          | expression '/' expression { $$ = $1 / $3; }
          | expression '^' expression { $$ = pow($1, $3); }
          | '(' expression ')'       { $$ = $2; }
          | NUMBER                  { $$ = $1; }
          ;

%%

int main(){
    yyparse;
}