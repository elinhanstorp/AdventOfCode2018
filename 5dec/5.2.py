f=open("input5.txt", "r")

contents = f.readline()

#print(contents)

#testinput = "nNXxRriAaImMZPpREAaaArqQtTRpPeZzYiIyVqQ"
LetterDict={}


theChar="a"
Alphabet=True

while Alphabet:

    testinput = contents # "nNXxRriAaImMZPpREAaaArqQtTRpPeZBbzYiBbIyVqQ"  #change to contents
    if theChar=="z":
        Alphabet=False

    i=len(testinput)-1

    while i > -1:
        tempChar=testinput[i]

        extraChar =theChar
        if (tempChar == theChar) or (tempChar == extraChar.upper()):
            testinput= testinput[:i]+testinput[i+1:]

        i-=1


    #Del 2:
    StillMatchingChars=True

    while StillMatchingChars:
        #print(len(testinput))
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

    # print("And then final length:")
    # print(len(testinput))
    LetterDict[theChar] = len(testinput)

    if StillMatchingChars == False:
        nextChar = chr(ord(theChar)+1)
        theChar = nextChar
        #print(theChar)



ShortestLength=3000000
for x in LetterDict:

    #print(LetterDict[x])
    if LetterDict[x] < ShortestLength:
        ShortestLength = LetterDict[x]

print("Shortest polynom:")
print(ShortestLength-1)

#to high : 13049
