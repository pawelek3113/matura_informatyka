# Szukanie przybliżonej wartości pierwiastka kwadratowego liczby
___

### Metoda babilońska
1. Ustal x0 = S, gdzie S to liczba, z której pierwiastka szukamy.
2. Niech xn+1 bedzie średnią arytmetyczną xn oraz S/xn.
3. Powtarzaj 2. krok do osiągnięcia pożądanej dokładności.

```python
x = S
while abs(x-S/x) > eps:
	x = (x + S/x)/2
print(x)
```

### Metoda równego podziału

1. Ustal początek przedziału na 0 a koniec na S (S - liczba, z której pierwiastka szukamy)
2. Wyznacz środek przedziału i sprawdź, czy jego kwadrat jest mniejszy czy większy od pierwiastka i odpowiednio weź prawą bądź lewą połówkę.
3. Powtarzaj krok 2 aż długość przedziału będzie mniejsza niż zadana dokładność. Jako ostateczny wynik weź średnią arytmetyczną z końców przedziału po ostatniej iteracji.

```python
start = 0
end = S 

while abs(start - end) > eps:
    mid = (start + end)/2
    
    if mid**2 <= S:
        start = mid
    else:
        end = mid

print((start + end)/2)
```

---
[Metody obliczania pierwiastka kwadratowego - wiki](https://pl.wikipedia.org/wiki/Metody_obliczania_pierwiastka_kwadratowego)