
f=open("input4.txt", "r")

contents = f.readlines()

InputList=[]

for time in contents:
    InputList.append(time)


sortedInputList= sorted(InputList)
print(sortedInputList)
