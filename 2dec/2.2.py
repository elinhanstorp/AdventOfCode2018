
f=open("input2.txt", "r")

contents = f.readlines()

for testline in contents:

    for line in contents:

        if testline == line:
            continue

        NbrDiff=0
        diffPos=-1

        for i in range(len(line)):
            if testline[i] != line[i]:
                NbrDiff+=1
                diffPos=i

            if NbrDiff > 1:
                break

        if NbrDiff == 1:
            print("the string is: ")
            print(testline[:diffPos]+testline[diffPos+1:])
            exit(0)
