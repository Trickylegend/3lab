
file = open("Учеба.txt", "r+", encoding="utf-8")

dict = {}
for line in file:
    sub = ""
    str = ""
    sum = 0
    bef = ""
    i = 1
    last = 0


    str = line.split(" ")
    sub = str[0][0:-1]
    last = str[i].find("(", 0, -1)
    print(str)

    for i in range(len(str)):
        i+=1
        if (str[-i][-1] == ":"):
            break
        last = str[-i].find("(", 0, -1)
        bef = int(str[-i][0: last])
        sum += bef
        # print("Кол-во часов: ", bef)
    dict[sub] = sum



print("\n", dict)
