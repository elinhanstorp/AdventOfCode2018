import datetime
f=open("input4.txt", "r")

contents = f.readlines()

InputList=[]

for time in contents:
    InputList.append(time)


sortedList= sorted(InputList)
#print(sortedInputList)


guardSleep={}
count = 0
SleepStart=(0,0)
SleepDone=(0,0)
GuardID = "#X"
tempBool = False

for data in sortedList:
    dataS=data.split(" ")
    #print(dataS)
    time = dataS[1][:-1]
    timeSplit = time.split(":")
    timme = int(timeSplit[0])
    minut = int(timeSplit[1])
    #timeObj=time(int(time[0:1]),int(time[3:4]))


    #testTime=datetime.time(22,54,0)

    if "asleep" in dataS[3]:
        # print("asleep in dataS[3] och ser ut:")
        # print(dataS)
        SleepStart=(timme,minut)
        #print("hej i asleep")
    elif "up" in dataS[3]:
        # print("up in dataS[3] och ser ut:")
        # print(dataS)
        SleepDone=(timme,minut)
        #print("hej i wake up")
        while (timme,minut) != SleepStart:
            #print(guardSleep)
            if minut == 0:
                print("Minute is now on 0 and about to take away 1 (-1) and the result is:")
                tempBool = True
            minut-=1
            if tempBool == True:
                print(minut)

            if (timme,minut) in guardSleep[GuardID]:
                 guardSleep[GuardID][(timme,minut)] += 1
                 # print("More than 1 on the same minute!:")
                 # print(guardSleep[GuardID][(timme,minut)])
            else:
                guardSleep[GuardID][(timme,minut)] = 1

    elif "#" in dataS[3]:
        GuardID = dataS[3]
        # print("# included in [3]:")
        # print(dataS)
        if GuardID not in guardSleep:
            guardSleep[GuardID] = {}
    else:
        print("Something wrong?, dataS[3]:")
        print(dataS[3])

GreatestSum =0
GreatestGuard="#1"

#print(guardSleep)

for guard in guardSleep:
    #print(guardSleep[guard])
    tempNbr=0
    for sleepNbr in guardSleep[guard]:
        tempNbr+=guardSleep[guard][sleepNbr]

        # print(guardSleep[guard][sleepNbr])
        # print("sovda timmar / minut pa dygnet:")
        # print(sleepNbr)
    if tempNbr > GreatestSum:
        GreatestSum = tempNbr
        GreatestGuard = guard
        # print("GreatestSum is:")
        # print(GreatestSum)

MostFreqventMinuteSize=0
MostFreqventMinute=0

for sleepMinut in guardSleep[GreatestGuard]:
    #print(guardSleep[GreatestGuard][sleepMinut])
    tempNbr=guardSleep[GreatestGuard][sleepMinut]

    if tempNbr > MostFreqventMinuteSize:
        MostFreqventMinuteSize = tempNbr
        MostFreqventMinute = sleepMinut
        # print("hejsan hopp::")
        # print(MostFreqventMinute)



#print(len(guardSleep))

print("Guard: ")
print(GreatestGuard)
print("sov storsta antal sovda timmar:")
print(GreatestSum)
#print(guardSleep["#641"])
print("Number of slept times is:")
print(MostFreqventMinuteSize)
print("The minute it is happening on is:")
print(MostFreqventMinute)


    # while
    # guardSleep[GuardID][(timme,minut)] = 1
    # guardSleep[GuardID][(timme,minut+1)] = 1


    # x=testTime.minutex
    # y=x+1
    # testTime.minute = testTime.replace(01,40,0)
    # print(testTime.minute )
    #print(timeObj)
    #print(guardSleep)
    # count += 1
    # if count == 30:
    #     print(len(guardSleep))
    #     exit(0)


    #put all data from guards in dic/matrix
        #each minute they sleep add 1 to value.
    #sum all minutes tex 1+1+4+2+1 = den vakt som sover mest
    #kolla viken box som ar fler dagar pa. ovan 4
