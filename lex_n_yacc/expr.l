%{
#include <stdio.h>
%}

%option noyywrap

%%
^aa(b|d)c*(a|b|d)*b+(ac)$    { printf("Accepted.\n"); }
\n                          { /* ignore newline */ }
.                           { printf("Rejected.\n"); }
%%

int main(void) {
    printf("Enter a string to test (Ctrl + D to stop):\n");
    yylex();
    return 0;
}
