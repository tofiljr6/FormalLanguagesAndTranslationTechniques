%option noyywrap
%option yylineno
%{
#include "cal.tab.hpp"

int yylex();
%}

%%
^#(.|\\\n)*\n   ;
\\\n            ;
[[:blank:]]+ 	;
[0-9]+	        { yylval = atoi(yytext); return NUM; }
"+"             { return PLUS; }
"-"             { return MINUS; }
"*"             { return MULT; }
"/"             { return DIV; }
"^"             { return POW; }
\(              { return LBRACKET; }
\)              { return RBRACKET; }
\n              { return END; }
.               { return ERROR; }
%%