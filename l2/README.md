# 🐵 Lista 2

## 👆 Zadanie 1

Napisz we FLEX-ie program która czyta dowolny plik tekstowy, usuwa w nim wszystkie białe znaki na końcu i na początku wiersza, zmienia wszystkie wsytąpienia ciągów tabulatorów i spacji n adokładnie jedną spację, likwiduję puste linie, oraz na końcu dopiusje liczbę linii i słów (ciągi znaków odzielone białbymi znakami).

### Rozwiązanie - uruchomienie

Skrypt ```zad1.sh``` kompiluje kod flexem, następnie kompiluje gcc, żeby na końcu uruchomić plik wynikowy flexa. Program przyjmuje na wejściu argument w postaci pliku z rozszerzeniem .l do skompilowania. N astandartowym wejściu podajemy plik do obróbki, na standartowym wyjściu dostajemy obrobiony tekst. Przykad wywołania znajduje się poniżej.

```bash
bash ./zad1.sh 1.l < in.txt > out.txt
```

W celu porównania plików, czy faktycznie są poprawne co do znaków, możemy wykorzystać `diff` lub `sha1sum`.

## ✌️ Zadanie 2 

Napisz w FLEX-ie program który uswa wszystkie komentarze w plikach źródłowych XML.

### Rozwiązanie - uruchomienie

Podobnie jak w zadaniu 1, dołączam skrypt ```zad2.sh```, który działa w podobny sposób jak w zadaniu pierwszym (patrz zadanie 1).

Jak możemy zaobserwowoać, wprowadzenie kodów w języku markdown language, nie jest odporne na "fałszywe" komentarze. Mimo, że jest nie prawidłowy komentraz, interpretator uważa go za komentarz.

## 🤟 Zadanie 3

Napisz w FLEX-ie program który usuwa wszystkie komentarze w programach naisanych w języku C++, a po włączeniu odpowiedniej opcji pozostawia komentarze dokumentacyjne (wg. Doxygen-a co najmniej następujące /**, /*!, /// i //!) i usuwa pozostałe.

### Rozwiązanie - uruchomienie

Podobnie jak w zadaniu 1, dołączam skrypt ```zad3.sh```, który działa w podobny sposób jak w zadaniu pierwszym (patrz zadanie 1).

## 🖖 Zadanie 4

Używając FLEX-a zaimplementuj prosty kalkulator postfiksowy (odwrotna notacja polska) dla liczb całkowitych wykonujących operacje dodawania (+), odejmowania (-), mnożenia(*), dzielenia całkowitoliczbowego (/), potęgowania(^) i modulu (%). Wyrażenie do policzenia powinno być napisane w jednej linii. Program powinnien wyświetlać dla każdej liniiw yniki albo komunikat o błedzie (naj najbardziej szczegółowy).

### Rozwiązanie - uruchomienie

Podobnie jak w zadaniu 1, dołączam skrypt ```zad4.sh```, który działa w podobny sposób jak w zadaniu pierwszym (patrz zadanie 1).