f=open("input5.txt", "r")

contents = f.readline()

#print(contents)

#testinput = "nNXxRriImMZPpRErqQtTRpPeZzYiIyVqQ"

testinput = contents

# print(testinput)
# # print(testinput[3])
# i=2
# testinput= testinput[:i]+testinput[i+2:]
# print(testinput)
# print(testinput[3])

StillMatchingChars=True
Count=0

while StillMatchingChars:
    Count +=1
    i=len(testinput)-2

    StillMatchingChars = False
    while i > -1:
        if i == len(testinput)-1:
            i-=1
        tempChar1=testinput[i]
        tempChar2=testinput[i+1]

        if(tempChar1.islower() and tempChar2.isupper()) or (tempChar2.islower() and tempChar1.isupper()):
            #print(tempChar1+tempChar2)
            if(tempChar1.lower() == tempChar2.lower()):
                #print(tempChar1+tempChar2)
                testinput= testinput[:i]+testinput[i+2:]
                StillMatchingChars=True

        i-=1

print("The number of units that is left is:")
print(len(testinput)-1)

#to high: 11541
