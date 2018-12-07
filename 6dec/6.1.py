import datetime
f=open("input6.txt", "r")

contents = f.readlines()

# put all point i matrix in forloop
#mark all point close to the border an infinite.
# go through all other point and check wich onw it is closest to.

#BiggestX = 358
#BiggestY = 359
matrix = [ [ "." ] * 360 ] * 360

i=1

for coordinates in contents:
    coordinate = coordinates.split(",")
    xPos = int(coordinate[0])
    yPos = int(coordinate[1])

    matrix[xPos][yPos] = 1
    i++
