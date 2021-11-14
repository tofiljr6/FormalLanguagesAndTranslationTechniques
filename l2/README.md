# Lista 2

## 👆 Zadanie 1

Napisz we FLEX-ie program która czyta dowolny plik tekstowy, usuwa w nim wszystkie białe znaki na końcu i na początku wiersza, zmienia wszystkie wsytąpienia ciągów tabulatorów i spacji n adokładnie jedną spację, likwiduję puste linie, oraz na końcu dopiusje liczbę linii i słów (ciągi znaków odzielone białbymi znakami).

Skrypt ```zad1.sh``` kompiluje kod flexem, następnie kompiluje gcc, żeby na końcu uruchomić plik wynikowy flexa. Program przyjmuje na wejściu argument w postaci pliku z rozszerzeniem .l do skompilowania. N astandartowym wejściu podajemy plik do obróbki, na standartowym wyjściu dostajemy obrobiony tekst. Przykad wywołania znajduje się poniżej.

```bash
bash ./zad1.sh 1.l < in.txt > out.txt
```

W celu porównania plików, czy faktycznie są poprawne co do znaków, możemy wykorzystać `diff` lub `sha1sum`.