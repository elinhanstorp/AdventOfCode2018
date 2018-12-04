import datetime
f=open("input4.txt", "r")

contents = f.readlines()

InputList=[]

for time in contents:
    InputList.append(time)


sortedList= sorted(InputList)

guardSleep={}
count = 0
SleepStart=(0,0)
SleepDone=(0,0)
GuardID = "#X"
tempBool = False

for data in sortedList:
    dataS=data.split(" ")
    time = dataS[1][:-1]
    timeSplit = time.split(":")
    timme = int(timeSplit[0])
    minut = int(timeSplit[1])

    if "asleep" in dataS[3]:

        SleepStart=(timme,minut)
    elif "up" in dataS[3]:
        SleepDone=(timme,minut)

        while (timme,minut) != SleepStart:

            if minut == 0:
                print("Minute is now on 0 and about to take away 1 (-1) and the result is:")
                tempBool = True
            minut-=1
            if tempBool == True:
                print(minut)

            if (timme,minut) in guardSleep[GuardID]:
                 guardSleep[GuardID][(timme,minut)] += 1
            else:
                guardSleep[GuardID][(timme,minut)] = 1

    elif "#" in dataS[3]:
        GuardID = dataS[3]
        if GuardID not in guardSleep:
            guardSleep[GuardID] = {}
    else:
        print("Something wrong?, dataS[3]:")
        print(dataS[3])


GlobalGreatestGuard="#1"
GlobalMostFreqventMinute=0
GlobalMinute=0
MostFreqventMinuteSize=0
MostFreqventMinute=0

for guard in guardSleep:

    for sleepMinut in guardSleep[guard]:
        tempNbr=guardSleep[guard][sleepMinut]

        if tempNbr > MostFreqventMinuteSize:
            MostFreqventMinuteSize = tempNbr
            MostFreqventMinute = sleepMinut

    if MostFreqventMinuteSize > GlobalMostFreqventMinute:
        GlobalMostFreqventMinute=MostFreqventMinuteSize
        GlobalMinute = sleepMinut
        GlobalGreatestGuard=guard


# print("sov storsta antal sovda timmar:")
# print(GreatestSum)
# print("Number of slept times is:")
# print(MostFreqventMinuteSize)


print("GlobalGuard: ")
print(GlobalGreatestGuard)
print("The minute it is happening on is:")
print(GlobalMinute)
print("And this is the guard info:")
print(guardSleep[GlobalGreatestGuard])
