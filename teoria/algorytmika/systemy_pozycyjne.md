# Systemy pozycyjne
___

### System dziesiętny 
pozycyjny system liczbowy, który składa się z cyfr [0 - 9] 
i którego podstawą jest 10. 
Używamy go w codziennych obliczeniach i jest "naturalny" dla człowieka.

> 645 = 6 * 10^2 + 4 * 10^1 + 5 * 10^0

### System dwójkowy
pozycyjny system liczbowy, który składa się z cyfr 0, 1 i którego podstawą jest 2. 
Cyfry 0,1 są również zwane bitami. System binarny jest "naturalny" dla komputera. 

Obliczenia w słupku w systemie dwójkowym działają tak samo jak te z dziesiętnego.

> 10101001 = 1⋅2^7 + 0⋅2^6 + 1⋅2^5 + 0⋅2^4 + 1⋅2^3 + 0⋅2^2 + 0⋅2^1 + 1⋅2^0 = 169

### System czwórkowy
pozycyjny system liczbowy, który składa się z cyfr [0 - 3] i którego podstawą jest 4.

> 30102 = 3⋅4^4 + 0⋅4^ 3 + 1⋅4^2 + 0⋅4^1 + 2⋅4^0 = 786

### System ósemkowy 
pozycyjny system liczbowy, który składa się z cyfr [0 - 7] i którego podstawą jest 8.

> 17730 = 1⋅8^4 + 7⋅8^3 + 7⋅8^2 + 3⋅8^1 + 0⋅8^0 = 8152

### System szesnastkowy 
pozycyjny system liczbowy, który składa się z cyfr [0 - 9], [A - F] i którego podstawą jest 16.

> 30102 = 3⋅16^4 + 0⋅16^3 + 1⋅16^2 + 0⋅16^1 + 2⋅16^0 = 196866

> A0F8 = A⋅16^3 + 0⋅16^2 + F⋅16^1 + 8⋅16^0 = 41208

> A = 10

> F = 15
 

## Konwersja
___

### Dwójkowy na dziesiętny

Konwersja polega na mnożeniu kolejnych bitów (zaczynając od najmłodszego bitu i kończąc na najstarszym bicie) przez wagę pozycji, czyli kolejne potęgi liczby 2 (zaczynając od potęgi zerowej). 
Po zsumowaniu iloczynów częściowych otrzymamy wynik – liczbę zapisaną w systemie dziesiętnym.

> 10101001 = 1⋅2^7 + 0⋅2^6 + 1⋅2^5 + 0⋅2^4 + 1⋅2^3 + 0⋅2^2 + 0⋅2^1 + 1⋅2^0 = 169

> 10000 = 1⋅2^4 + 0⋅2^3 + 0⋅2^2 + 0⋅2^1 + 0⋅2^0 = 16
 
> 1111 = 1⋅2^4 + 1⋅2^3 + 1⋅2^2 + 1⋅2^1 + 1⋅2^0 = 31


### Dziesiętny na dwójkowy

1. Zapisz resztę z dzielenia n przez 2. 
2. Podziel n przez 2 i zaokrąglij w dół.
3. Jeśli n ≠ 0 to powróć do kroku 1 zapisując resztę z prawej strony.
4. Liczba odczytana wspak jest liczbą n zapisaną w systemie dwójkowym.

Przykład:

n = 23

23 % 2 = 1

23//2 = 11 reszty = [1, ]

11 % 2 = 1

11//2 = 5 reszty = [1, 1,]

5 % 2 = 1

5//2 = 2 reszty = [1, 1, 1,]

2 % 2 = 0

2//2 = 1 reszty = [1, 1, 1, 0,]

1 % 2 = 1

1//2 = 0 reszty = [1, 1, 1, 0, 1]

23 w dwojkowym = 00010111

### Dziesiętny na czwórkowy

1. Oblicz resztę z dzielenia n przez 4 używając algorytmu do dzielenia z resztą.
2. Podziel n przez 4 i zaokrąglij w dół do liczby całkowitej.
3. Jeśli n=0, to reszty odczytane wspak tworzą odpowiednik n10 w systemie czwórkowym.
4. Jeśli n>0 to powróć do pierwszego kroku.


### Dziesiętny na ósemkowy

1. Oblicz resztę z dzielenia n przez 8 używając algorytmu do dzielenia z resztą.
2. Podziel n przez 8 i zaokrąglij w dół do liczby całkowitej.
3. Jeśli n=0, to reszty odczytane wspak tworzą odpowiednik n10 w systemie ósemkowym.
4. Jeśli n>0 to powróć do pierwszego kroku.


### Dziesiętny na szesnastkowy

1. Oblicz resztę z dzielenia n przez 16 używając algorytmu do dzielenia z resztą. Reszta będzie liczbą pomiędzy 0 a 15, dlatego zmień liczbę na jej odpowiednik w systemie szesnastkowym. 
Tzn. 10→A, 11→B, ..., 15→F
2. Podziel n przez 16 i zaokrąglij w dół do liczby całkowitej.
3. Jeśli n=0, to reszty odczytane wspak tworzą odpowiednik n10 w systemie szesnastkowym.
4. Jeśli n>0 to powróć do pierwszego kroku.

