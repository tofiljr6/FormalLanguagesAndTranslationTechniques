%{
#include <stdio.h>
#include <stdbool.h>
int yywrap();
int yylex();

char* concat(const char* str1, const char* str2) {
    char* result = malloc(strlen(str1) + strlen(str2) + 1);
    strcpy(result, str1);
    strcat(result, str2);
    return result;
}

char* str = "";
bool err = false;

%}

%x COMMENT
%x COMMENT_DATA
%x VARIABLE

open \<!--
close --\>
commentdataopen \<!\[CDATA\[
commentdataclose \]\]\>

%%

{open}               BEGIN(COMMENT);
<COMMENT>.|\n        str = concat(str, yytext);
<COMMENT>{open}|--   {
    err = true;
    str = concat(str, yytext);
};
<COMMENT>{close}     {
    if (err) {
        printf("<!--%s-->", str);
    }
    str = "";
    err = false;
    BEGIN(INITIAL);
};

{commentdataopen}         {
    printf("%s", yytext);
    BEGIN(COMMENT_DATA); 
};
<COMMENT_DATA>{commentdataclose} {
    ECHO;
    BEGIN(INITIAL);
};

\"                   {
    printf("%s", yytext);
    BEGIN(VARIABLE);
}
<VARIABLE>\"        {
    printf("%s", yytext);
    BEGIN(INITIAL);
}

%%


int yywrap(){
    return 1;
}

int main() {    
    return yylex();
}
