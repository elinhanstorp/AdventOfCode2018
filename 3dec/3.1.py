
f=open("input3.txt", "r")

contents = f.readlines()

pixels={}

for square in contents:

    s = square.split()
    xy=s[2].split(',')
    wh=s[3].split('x')

    xPos=int(xy[0])
    xy[1]=xy[1][:-1]
    yPos=int(xy[1])

    width=int(wh[0])
    hight=int(wh[1])

    for x in range(width):
        XX= int(x+xPos)
        for y in range(hight):
            YY= int(y+yPos)
            #print( (XX,YY))

            if (XX,YY) in pixels:
                pixels[(XX,YY)] += 1
            else:
                pixels[(XX,YY)] = 1


#    print(pixels)
#    exit(0)


summa=0
SumOne=0

#print(pixels)

for pix in pixels:
    if pixels[pix] > 1:
        summa+=1
    # if pixels[pix] == 1:
    #     SumOne+=1

#Too low: 32613
# print(len(pixels))
print(SumOne)
#print(summa)
