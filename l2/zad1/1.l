%{
#include <stdio.h>
int yywrap();
int yylex();
int lines = 0;
int words = 0;
%}

%%
^[[:blank:]]*(\n)? ;        // usunięcie spacji/tabulatora na początku linii i ewentalne wystąpienie znaku nowej linii
([[:blank:]]+)$    ;        // usunięcie spacji/tabulatorów na końcu linii
[[:blank:]]+  {             // zamiana wszystkie wystąpienia ciągów tabolatorów i spacji na dokładnie jedną spację
    printf(" ");
}
\n  {
    printf("\n");
    lines++;
}
[a-zA-Z]+  {
    printf("%s", yytext);
    words++;
}

%%

int yywrap(){
    printf("\nLiczba linii %d, liczba slow %d" , lines, words);
    return 1;
}

int main() {    
    return yylex();
}
