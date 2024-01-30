%{
#include <stdio.h>
#include <math.h>
int yylex(void);
void yyerror(char *s);
%}
%token NAME NUMBER
%left '-' '+'
%left '*' '/'
%right '^'
%nonassoc UMINUS

%%
statement: expression { printf("Result: %d\n", $1); }
| statement expression { printf("Result: %d\n", $2); }
;
expression: expression '+' expression { $$ = $1 + $3; }
| expression '-' expression { $$ = $1 - $3; }
| expression '*' expression { $$ = $1 * $3; }
| expression '/' expression { $$ = $1 / $3; }
| expression '^' expression { $$ = pow($1, $3); }
| '-' expression %prec UMINUS { $$ = -$2; }  // Corrected '-' to '-' (minus sign)
| '(' expression ')' { $$ = $2; }
| NUMBER { $$ = $1; }
;
%%

int main(){
    yyparse();
    return 0;  // Add return statement
}
