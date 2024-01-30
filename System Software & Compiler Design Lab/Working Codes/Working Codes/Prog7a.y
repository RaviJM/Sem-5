%{
#include<stdio.h>
int yylex(void);
void yyerror();
%}

%token NAME NUMBER
%%
statement: NAME '=' expression
| expression {printf("= %d\n", $1);}
;
expression: expression '+' NUMBER {$$ = $1 + $3;}
| expression '-' NUMBER {$$ = $1 - $3;}
| expression '*' expression { $$ = $1 * $3; }
| expression '/' expression { $$ = $1 / $3; }
| NUMBER {$$ = $1;}
;
%%
void main(){ printf("\n Enter Expression: "); yyparse();
}
void yyerror(){ printf("\n Entered arithmetic Expression is Invalid\n\n");
}