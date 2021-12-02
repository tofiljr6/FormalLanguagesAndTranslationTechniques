bison -d cal.ypp
flex cal.l
g++ -o calculator cal.tab.cpp lex.yy.c
./calculator