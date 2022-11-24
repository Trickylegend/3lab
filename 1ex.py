







f1 = open("F1.txt", "r+", encoding="utf-8")
f2 = open("F2.txt", "r+", encoding="utf-8")

while(1):
    str = input(print("Введите строку: "))
    if (str == ""):
        break
    else:
        str += "\n"
        f1.writelines(str)




for line in f1:
    c = 0
    for i in line:
        if(i == " "):
            c = 1
            break
    if (c == 0):
        f2.write(line)

min = 1000
mins = ""

for line in f2:
    if(len(line) < min):
        min = len(line)
        mins = line


print(mins)
f1.close()
f2.close()