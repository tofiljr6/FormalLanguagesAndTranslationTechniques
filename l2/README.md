# 馃惖 Lista 2

## 馃憜 Zadanie 1

Napisz we FLEX-ie program kt贸ra czyta dowolny plik tekstowy, usuwa w nim wszystkie bia艂e znaki na ko艅cu i na pocz膮tku wiersza, zmienia wszystkie wsyt膮pienia ci膮g贸w tabulator贸w i spacji n adok艂adnie jedn膮 spacj臋, likwiduj臋 puste linie, oraz na ko艅cu dopiusje liczb臋 linii i s艂贸w (ci膮gi znak贸w odzielone bia艂bymi znakami).

### Rozwi膮zanie - uruchomienie

Skrypt ```zad1.sh``` kompiluje kod flexem, nast臋pnie kompiluje gcc, 偶eby na ko艅cu uruchomi膰 plik wynikowy flexa. Program przyjmuje na wej艣ciu argument w postaci pliku z rozszerzeniem .l do skompilowania. N astandartowym wej艣ciu podajemy plik do obr贸bki, na standartowym wyj艣ciu dostajemy obrobiony tekst. Przykad wywo艂ania znajduje si臋 poni偶ej.

```bash
bash ./zad1.sh 1.l < in.txt > out.txt
```

W celu por贸wnania plik贸w, czy faktycznie s膮 poprawne co do znak贸w, mo偶emy wykorzysta膰 `diff` lub `sha1sum`.

## 鉁岋笍 Zadanie 2 

Napisz w FLEX-ie program kt贸ry uswa wszystkie komentarze w plikach 藕r贸d艂owych XML.

### Rozwi膮zanie - uruchomienie

Podobnie jak w zadaniu 1, do艂膮czam skrypt ```zad2.sh```, kt贸ry dzia艂a w podobny spos贸b jak w zadaniu pierwszym (patrz zadanie 1).

Jak mo偶emy zaobserwowoa膰, wprowadzenie kod贸w w j臋zyku markdown language, nie jest odporne na "fa艂szywe" komentarze. Mimo, 偶e jest nie prawid艂owy komentraz, interpretator uwa偶a go za komentarz.

## 馃 Zadanie 3

Napisz w FLEX-ie program kt贸ry usuwa wszystkie komentarze w programach naisanych w j臋zyku C++, a po w艂膮czeniu odpowiedniej opcji pozostawia komentarze dokumentacyjne (wg. Doxygen-a co najmniej nast臋puj膮ce /**, /*!, /// i //!) i usuwa pozosta艂e.

### Rozwi膮zanie - uruchomienie

Podobnie jak w zadaniu 1, do艂膮czam skrypt ```zad3.sh```, kt贸ry dzia艂a w podobny spos贸b jak w zadaniu pierwszym (patrz zadanie 1).

## 馃枛 Zadanie 4

U偶ywaj膮c FLEX-a zaimplementuj prosty kalkulator postfiksowy (odwrotna notacja polska) dla liczb ca艂kowitych wykonuj膮cych operacje dodawania (+), odejmowania (-), mno偶enia(*), dzielenia ca艂kowitoliczbowego (/), pot臋gowania(^) i modulu (%). Wyra偶enie do policzenia powinno by膰 napisane w jednej linii. Program powinnien wy艣wietla膰 dla ka偶dej liniiw yniki albo komunikat o b艂edzie (naj najbardziej szczeg贸艂owy).

### Rozwi膮zanie - uruchomienie

Podobnie jak w zadaniu 1, do艂膮czam skrypt ```zad4.sh```, kt贸ry dzia艂a w podobny spos贸b jak w zadaniu pierwszym (patrz zadanie 1).