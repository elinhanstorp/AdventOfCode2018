
f=open("input1.txt", "r")

contents = f.readlines()

summa=0
# resultList=[]
# notFound = True

resultObjectList={
    0:"reached"
}

while True:
    for nbr in contents:

        summa += int(nbr)

        if resultObjectList.get(summa) == "reached":
            print(summa)
            exit(0)
        else:
            resultObjectList[summa] = "reached"

        # if nbr[0] == "+" :
        #     summa += int(nbr[1:])
        # elif nbr[0] == "-":
        #     summa -= int(nbr[1:])



        # if summa in resultList:
        #     print("First to reach twice:")
        #     print(summa)
        #     notFound = False
        #     break
        # else:
        #     resultList.append(summa)
