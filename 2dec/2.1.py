
f=open("input2.txt", "r")

contents = f.readlines()

nbrOf2=0
nbrOf3=0
# resultList=[]
# notFound = True



for line in contents:

    tempList={}

    #puts all char in a list with the number of times it appers
    for ch in line:

        if tempList.get(ch):
                tempList[ch]+=1
        else:
                tempList[ch]=1

    #checks if any apperes twice or three times
    twoNotFound = True
    threeNotFound = True
    for ch in tempList:
        if tempList[ch]==2 and twoNotFound:
            nbrOf2+=1
            twoNotFound=False
        if tempList[ch]==3 and threeNotFound:
            nbrOf3+=1
            threeNotFound=False

    twoNotFound = True
    threeNotFound = True


print("The checksum is:")
print(nbrOf2 * nbrOf3)
