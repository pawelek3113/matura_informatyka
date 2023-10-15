"""
Binary search
-----
Check whether the number from the sequence B is in the non-decreasing sequence A. 

Set the initial and last index of the searched interval.
Based on these indexes, determine the index of the middle element.

If the number is greater than the middle element of the range,
that means, it is in the range from the middle to the end element.

If the number is less than or equal to the middle element,
that means, it is in the range from the initial to the middle element.

Shorten the interval until you achieve a single-element sequence.

Check if this element is equal to the wanted number.

-----
Wyszukiwanie binarne
-----
Sprawdzamy czy liczba z ciągu B znajduje się w NIEMALEJĄCYM ciągu A.

Ustalamy poczatkowy i ostatni index przeszukiwanego przedzialu.
Na podstawie tych indexow ustalamy index srodkowego elementu.

Jesli szukana liczba jest wieksza od srodkowego elementu przedzialu,
to znaczy ze znajduje sie w przedziale od srodkowego do koncowego elementu.

Jesli szukana liczba jest mniejsza badz rowna srodkowemu elementowi, 
to znaczy ze znaduje sie w przedziale od poczatkowego do srodkowego elementu.

Skracamy przedzial przeszukiwan, az osiagniemy jednoelementowy ciag.
Sprawdzamy czy ten wyraz jest równy liczbie z ciagu B.
"""

def binary_search(number_to_find, seq):
    begin_idx = 0
    end_idx = len(seq) - 1

    while begin_idx < end_idx:
        mid_idx = (begin_idx + end_idx) // 2
        if number_to_find > seq[mid_idx]:
            begin_idx = mid_idx + 1
        elif number_to_find <= seq[mid_idx]:
            end_idx = mid_idx

    return seq[begin_idx] == number_to_find


sequence = [1, 2, 3, 4, 6, 7, 9, 12, 20, 21]

n = int(input("How many numbers would you like to find?"))

find: list[int] = []

for i in range(n):
    find.append(int(input(f"{i+1}. ")))

for number in set(find):
    if binary_search(number, sequence):
        print(f"{number} found")
    else:
        print(f"{number} not found :(")
