


file = open("Вокзал.txt", "r+", encoding="utf-8")



dest = input(print("Пункт назначения: "))



for line in file:
    d = ""
    c = 0
    co = 0
    for char in line:
        if char == " ":
            c = 1
            co += 1
        if co > 1:
            break
        if c > 1:
            d += char
        if c == 1:
            c = 2
    if d == dest:
        print(line)

file.close()
af = 0
file = open("Вокзал.txt", "r+", encoding="utf-8")

for line in file:
    cost = ""
    c = 0
    co = 0
    for char in line:
        if len(cost) > 2:
            break
        if char == " ":
            c += 1
            co += 1
        if c == 5:
            cost += char
        if c == 4:
            c += 1
    if int(cost) < 50:
        print(line)