def sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

fieldsNpricesSTRING = []

with open("dzialki22.txt", "r", encoding="UTF-8") as file:
    fieldsNpricesSTRING = [strr.strip() for strr in file.readlines()]

fieldsNpricesARRstr = [s.split() for s in fieldsNpricesSTRING]
fieldsNprices = [[int(area), int(price)] for area, price in fieldsNpricesARRstr]


goodFields = []

for item in fieldsNprices:
    if item[0] > 100:
        goodFields.append(item)

sort(goodFields)

goodFields = goodFields[:10]

res = 0
for field in goodFields:
    res += field[1]

print(goodFields)
print(len(goodFields))

print(res)