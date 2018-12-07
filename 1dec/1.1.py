print("hej")

f=open("input1.txt", "r")

contents = f.readlines()

summa=0

for nbr in contents:

    if nbr[0] == "+" :
        summa += int(nbr[1:])
    elif nbr[0] == "-":
        summa -= int(nbr[1:])
    else:
        print("nbr:" + nbr)

print("Den totala summan blir:")
print(summa)
