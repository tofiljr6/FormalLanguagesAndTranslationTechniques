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
bool docs = true;

%}

singleline      \/[\\\n]*\/
singlelineDoc   \/[\\\n]*\/(\/|!)
multiline       \/[\\\n]*\*
multilineDoc    \/[\\\n]*\*[\\\n]*(\*|!)
multilineEnd    \*[\\\n]*\/

%x INCLUDE
%x STRING
%x SINGLELINE
%x MULTILINE

%%
{singlelineDoc}             {
    if (docs) printf("%s", yytext);
    else BEGIN(SINGLELINE);
};

{singleline}                BEGIN(SINGLELINE);
<SINGLELINE>.*\\\n          ;
<SINGLELINE>.               ;
<SINGLELINE>[^\\]\n         BEGIN(INITIAL);

{multilineDoc}              {
    if (docs) ECHO;
    else BEGIN(MULTILINE); 
};
{multiline}                 BEGIN(MULTILINE);
<MULTILINE>.|\n             ;
<MULTILINE>{multilineEnd}   BEGIN(INITIAL);

\"                          {
    ECHO;
    BEGIN(STRING);
};
<STRING>\"                  {
    ECHO;
    BEGIN(INITIAL);
};

#include[[:blank:]]*\<      {
    ECHO;
    BEGIN(INCLUDE);
};
<INCLUDE>\>                 {
    ECHO;
    BEGIN(INITIAL);
};
<INCLUDE>.|\n               ECHO;

%%

int yywrap(){
    
    return 1;
}

int main() {    
    return yylex();
}