# Lista 1 🔍

Analiza i implementacja algorytmów wyszukiwania wzorca z wykorzystaniem **automatów skońocznych** i **Knutha-Morrisa-Pratta**

## ☝️ Szukanie wzorca z wykorzystaniem automatów skończonych (FAMatcher)

Programik szuka na podanego patternu w pliku wejściowym. W celu uruchomienia programu należy wpisać w konsoli:

```termical
python3 farun.py <pattern>
```

Program na wyjściu pokazuje, na którym indeksie w tablicy wejściowej (pliku) pojawia się początek szukanego przez nas wzorca `pattern`.

## ✌️ Szukanie wzorca - algorytm Knutka-Morrisa-Pratta (KMPMatcher)

Programik szuka na podanego patternu w pliku wejściowym. W celu uruchomienia programu należy wpisać w konsoli:

```termical
python3 kmprunrun.py <pattern>
```

## 📈 Porównanie algorytmów 

1)  Złożoność obliczeniowa `FAMatcher()` jest uzależniona od długośći pliku wejściowego, n - długość stringa. Wtedy złożność wynosi 𝛩(n). Ponieważ musimy również wyliczyć funckje przejśc delta, `computeTransitionFunction()` , to algorytm odpowiedzialny za tą część, ma złożoność obliczeniową O(m^3|sigma|), gdzie m to długość patternu, a sigma to wielkość słownika. Pomijam złożoność obliczeniową tworzenia słownika ze względu, że jest to zwyczajne przejście po wsystkich elementach.

2)  Złożoność obliczeniowa `ComputePrefixFunction()` to 𝛩(m), a `KMPMatcher()` to 𝛩(n).

## Podsumowanie

Do implementacji algorytmów wykorzytsałem książką: Introduction to algorithms - Cormen


