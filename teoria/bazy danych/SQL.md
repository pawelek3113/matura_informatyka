### SELECT 
```SQL
SELECT Imie, Nazwisko
FROM  Uczniowie
```

### SELECT DISTINCT
```SQL
SELECT DISTINCT Klasa
FROM Uczniowie
```

### WHERE
- równy =
- nierówny <>
- większy >
- większy lub równy >=
- mniejszy <
- mniejszy lub równy <=

```SQL
SELECT imie, nazwisko
FROM uczniowie
WHERE srednia_ocen > 4.75
```

#### OPERATORY LOGICZNE
- AND - zwraca prawdę, jeżeli oba warunki są prawdziwe
- OR - zwraca prawdę, jeżeli co najmniej jeden warunek jest prawdziwy
- NOT - zwraca prawdę, jeżeli warunek nie jest prawdziwy

### LIKE
```SQL
SELECT * FROM Klienci
WHERE Imie LIKE "%a";
```

> % reprezentuje parę znaków
> _ reprezentuje jeden znak

> "%a" - kończy się na literę "a"
> "a%" - zaczyna się literą "a"

> W MS Access LIKE to ALIKE (ANSI 92 SQL syntax)

##### Liczenie wszystkich rekordów w MS Access
- tworzymy query
- wybieramy widok arkusza danych
- narzędzia główne > rekordy > sumy
- pojawia się dodatkowy wiersz na dole wynikowej tabeli
- klikamy na pole, wybieramy Liczba z rozwijanej listy

### ORDER BY
```SQL
SELECT imie, nazwisko, srednia_ocen, klasa FROM uczniowie 
ORDER BY srednia_ocen ASC
```

Sortowanie tablicy wynikowej.
> ASC - rosnąco
> DESC - malejąco

#### LIMIT
```SQL
SELECT imie, nazwisko, srednia_ocen, klasa FROM uczniowie 
ORDER BY srednia_ocen ASC LIMIT 2
```

Pozwala na wyświetlenie konkretnej liczby wierszy.
Używane z ORDER BY.

> W MS Access zamiast LIMIT używa się SELECT TOP 2 * FROM customers

### NULL
```SQL
SELECT *  FROM uczniowie 
WHERE drugie_imie IS NULL
```

W przypadku, gdy w tabeli pojawiają się puste komórki.

> IS NULL - zwraca prawde, gdy wartość jest równa NULL
> IS NOT NULL - zwraca prawde, gdy wartość nie jest równa NULL

### CASE
```SQL
SELECT imie, nazwisko, 
CASE 
WHEN srednia_ocen > 4.75 THEN 'czerwony pasek' 
ELSE 'brak czerwonego paska' 
END 
FROM uczniowie 
ORDER BY nazwisko
```

CASE jest traktowane jako osobna kolumna, z tego powodu potrzebny jest przecinek.

```SQL
CASE
	WHEN condition1 THEN result1
	WHEN condition2 THEN result2
	WHEN condition3 THEN result3
	ELSE result
END
```

Przechodzi przez każdy warunek i zwraca wynik kiedy pierwszy z nich jest spełniony.
Jeśli żaden warunek nie jest prawdziwy, zwraca wartość z ELSE.
Jeśli nie ma ELSE, CASE zwraca NULL.

#### AS
Alias sprawia, że możemy nazywać kolumny lub tabele.

```SQL
SELECT imie, nazwisko, 
CASE 
WHEN srednia_ocen > 4.75 THEN 'czerwony pasek' 
ELSE 'brak czerwonego paska' 
END AS pasek 
FROM uczniowie 
ORDER BY nazwisko
```

### JOIN
```SQL
SELECT transakcje.id, transakcje.kwota, transakcje.klientid, klienci.imie, klienci.nazwisko 
FROM transakcje 
JOIN klienci ON transakcje.klientid = klienci.klientid 
ORDER BY transkacje.kwota ASC 
LIMIT 1
```

Łączenie rekordów z dwóch lub więcej tabel.

- określenie kolumn, jakie chcemy umieścić w tabeli wynikowej
- w poleceniu FROM określamy pierwszą tabelę
- w klauzuli JOIN dopisujemy drugą tabelę
- po słowie kluczowym ON piszemy warunek złączenia

### RODZAJE JOINÓW

#### INNER JOIN
zwraca wiersze z obu tabel które spełnią warunek złączenia
![inner_join.png](/imgs/inner_join.png)

#### LEFT JOIN
zwraca wszystkie wiersze z "lewej" tabeli (tj. tabeli którą wpisujemy po FROM) i wiersze z prawej tabeli które spełnią warunek złączenia (tj. tabeli którą wpisujemy po JOIN)
![left_join.png](/imgs/left_join.png)

#### RIGHT JOIN
zwraca wszystkie wiersze z "prawej" tabeli i wiersze z lewej tabeli które spełnią warunek złączenia
![right_join.png](/imgs/right_join.png)

#### FULL OUTER JOIN
zwraca wszystkie wiersze z obu tabel
![full_outer_join.png](/imgs/full_outer_join.png)

### GROUP BY
Grupuje rekordy z takimi samymi wartościami
Tworzy grupy
```sql
SELECT rok FROM uczniowie 
GROUP BY rok
```

> Używając GROUP BY, w poleceniu SELECT możemy wyświetlać tylko kolumny po których grupujemy.

### Funkcje agregujące
- COUNT(), 
- MAX(),
- MIN(),
- SUM(),
- AVG()

### HAVING
Używane z funkcjami agregującymi

```SQL
SELECT data, SUM(kwota) AS SUMA, COUNT(*) AS ILOSC FROM transakcje 
GROUP BY data 
ORDER BY ILOSC ASC 
HAVING COUNT(kwota) < 4
```

Pozwala określić warunek, który każda grupa musi spełnić, aby mogła się pojawić w tablicy wynikowej.

##### RÓŻNICA MIĘDZY WHERE A HAVING
> Otóż **WHERE filtruje dane przed pogrupowaniem, a HAVING wybiera już pogrupowane dane.**

### COUNT DISTINCT
Zlicza rekordy o różnych wartościach
```SQL
SELECT COUNT(DISTINCT kwota) AS ILOSC 
FROM transakcje
```

### FUNKCJE TEKSTOWE
- LEFT(string, n) - zwraca n znaków od lewej strony z podanego stringa
- RIGHT(string, n) - zwraca n znaków od prawej strony z podanego stringa
- UPPER(string), LOWER(string) - zmienia wszystkie litery w stringu na wielkie (UPPER) lub małe (LOWER) litery
- LENGTH(string) - zwraca długość podanego ciągu znaków
- SUBSTRING(string, start, n) - zwraca fragment podanego ciągu znaków ("string"). Początkowy indeks zwracanego fragmentu określamy parametrem "start", a długość fragmentu atrybutem "n".
- "+" - operator + użyty na ciągach znaków łączy dwa stringi

> W MS Access LENGTH() to Len()

### CAST
Zamiana typu danej wartości
```sql
CAST(wartosc AS typ_danych)
```

##### Typy danych
> VARCHAR(x), BIG_INT, INT, DOUBLE, FLOAT, CHARACTER, DATE.

Aby zamienić wartość w tekst (VARCHAR) musimy podać limit znaków 

```sql
CAST(liczba AS VARCHAR(20))
```

### DATY
**Daty w zapytaniach SQL piszemy w formacie 'YYYY-MM-DD'.**
- YEAR(data) - zwraca rok z podanej daty
- MONTH(data) - zwraca miesiąc z podanej daty
- DAY(data) - zwraca dzień z podanej daty
- DAYNAME(data) - zwraca nazwę dnia tygodnia podanej daty
- HOUR(data) - zwraca godzinę z podanej daty.
- MINUTE(data) - zwraca minute z podanej daty.
- DATEDIFF(typ, data1, data2) - zwraca różnice między datami
- DATEADD(typ, ilosc, data) - dodawanie jednostki czasu do daty

#### JEDNOSTKI CZASU
- yyyy - rok
- q - kwartał
- m - miesiąc
- y - dzień roku
- d - dzień
- w - dzień tygodnia
- ww - tydzień
- h - godzina
- n - minuta
- s - sekunda

### IN
```SQL
SELECT Name FROM Employees
WHERE Name IN ("Natalia", "Beata", "Andrzej")
```

### BETWEEN
```SQL
SELECT Birthday FROM Users
WHERE Birthday BETWEEN 2004-10-23 AND 2005-04-30 
```

### ZAOKRĄGLANIE WARTOŚCI
- ROUND(liczba, dokładność) - dokładność to ilość miejsc po przecinku
- FLOOR(liczba) - zaokrąglanie w dół
- CEILING(liczba) - zaokrąglanie w górę

### FUNKCJE MATEMATYCZNE
- POWER(liczba, potęga) - potęgowanie liczby
- SQRT(liczba) - pierwiastek kwadratowy z liczby
- ABS(liczba) - wartość bezwzględna z liczby
- MOD(x, y) - reszta z dzielenia liczby x przez y

> ^ to potęgowanie
> Pierwiastek kwadratowy w MS Access to SQR()

### SUBQUERIES
___
Chcemy zwrócić imię i nazwisko użytkownika, który wypłacił najwięcej pieniędzy.
Zamiast JOIN można użyć podzapytania.

To zapytanie zwraca ID użytkownika, który wypłacił najwięcej pieniędzy. (kwota ujemna)
```SQL
SELECT klientid 
FROM transakcje 
ORDER BY kwota ASC 
LIMIT 1
```

Zapytanie korzystające z powyższego zapytania.
```SQL
SELECT imie, nazwisko 
FROM klienci 
WHERE klientid = ( 
SELECT klientid 
FROM transakcje 
ORDER BY kwota ASC 
LIMIT 1)
```

Jeśli subquery zwraca więcej recordów to nie możemy użyć =.
Zamiast tego, używamy IN.

```SQL
SELECT imie, nazwisko 
FROM klienci 
WHERE klientid IN ( 
SELECT klientid 
FROM transakcje 
WHERE kwota < -1000)
```

#### Podzapytania poza klauzulą WHERE
```SQL
SELECT MAX(LENGTH(imie)), imie
FROM(
SELECT imie
FROM klienci
WHERE plec = 'K')
```

```sql
SELECT imie, nazwisko, data, kwota
FROM klienci JOIN transakcje ON 
klienci.klientid = transakcje.id,
(SELECT data AS data2, MIN(kwota) as mini
FROM transakcje
GROUP BY data)
WHERE data = data2 AND kwota = mini
```


### ANY I ALL
> ALL - zwraca prawdę, gdy **wszystkie** wiersze spełniają warunek
> ANY - zwraca prawdę, gdy **jakikolwiek** wiersz spełnia warunek

```sql
SELECT imie, nazwisko 
FROM klienci 
WHERE klientid = ANY 
( SELECT klientid 
FROM transakcje 
WHERE data = '05.01.2020' )
```

### CREATE TABLE
Tworzenie tabeli
```SQL
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
```

### DELETE
Usuwanie rekordów z tabeli.
```SQL
DELETE FROM table_name WHERE condition;
```

### DROP TABLE
Usuwanie tabeli.
```SQL
DROP TABLE table_name;
```
Często używane w atakach SQL INJECTION.

### INSERT INTO
```SQL
INSERT INTO table_name (column1, column2, column3) 
VALUES(val1, val2, val3)
```
Wstawianie jednego rekordu do tabeli.

```sql
INSERT INTO table_name2 (col1, col2, col3)
SELECT col1, col2, col3 FROM table1
WHERE condition
```
Wstawianie wyniku zapytania do tabeli.

### UPDATE
```SQL
UPDATE table_name SET col1 = val1, col2 = val2 
WHERE condition;
```
Aktualizacja rekordów.

