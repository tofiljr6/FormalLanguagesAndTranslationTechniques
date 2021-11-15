%{
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#define STACKSIZE 16
int yywrap();
int yylex();

int stack[STACKSIZE];
int top = 0;
bool err = false;

void push(int val) {
    if (top < STACKSIZE) {
        stack[top] = val;
        top++;
    } else {
        printf("Stack Overflow");
        err = true;
    }
}

int pop() {
    top--;
    if (top < 0 ) {
        printf("Za mała liczba argumentów\n");
        err = true;
        return 0;
    }
    return stack[top];
}

%}

%x ERROR

%%

-?[[:digit:]]+          {
    push(atoi(yytext));
    if (err) {
        BEGIN(ERROR);
    }
}

"+"                     {
    push(pop() + pop());
    if (err) {
        BEGIN(ERROR);
    }
}

"-"                     {
    int val = pop();
    push(pop() - val);
    if (err) {
        BEGIN(ERROR);
    }
}

"*"                     {
    push(pop() * pop());
    if (err) {
        BEGIN(ERROR);
    }
}

"/"                     {
    int val = pop();
    if (val == 0) {
        printf("Nie dziel przez 0...\n");
        BEGIN(ERROR);
    } else {
        push(pop() / val);
    }
    if (err) {
        BEGIN(ERROR);
    }
}

"^"                     {
    int val = pop();
    if (val < 0) {
        printf("Ujemne potęgowanie\n");
        BEGIN(ERROR);
    } else {
        int result = (int) pow( (double) pop(), (double) val) ;
        push(result);
    }
    if (err) {
        BEGIN(ERROR);
    }
}

"%"                     {
    int val = pop();
    if (val == 0) {
        printf("Nie dzielimy przez zero...");
        BEGIN(ERROR);
    } else {
        push(pop() % val);
    }
    if (err) {
        BEGIN(ERROR);
    }
}

\n                      {
    if (top == 1) {
        printf("%d\n", pop());
    } else if (top > 1) {
        printf("za mała liczba operatorów");
        top = 0;
    }
}

[[:blank:]]             ;

[^[:blank:]]            {
    printf("Zły symbol %s", yytext);
    BEGIN(ERROR);
}

<ERROR>.*               ;
<ERROR>\n               {
    top = 0;
    err = false;
    BEGIN(INITIAL);
}
%%

int yywrap(){
    return 1;
}

int main() {    
    return yylex();
}
